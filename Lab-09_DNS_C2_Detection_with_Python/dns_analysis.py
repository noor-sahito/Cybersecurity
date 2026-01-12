import subprocess
from collections import Counter, defaultdict
from statistics import pstdev

pcap_file = "dns_real.pcap"

print("[*] Extracting DNS queries with timestamps and source IPs...\n")

cmd = [
    "tshark",
    "-r", pcap_file,
    "-Y", "dns && dns.qry.name",
    "-T", "fields",
    "-e", "frame.time_epoch",
    "-e", "ip.src",
    "-e", "dns.qry.name"
]

result = subprocess.run(cmd, capture_output=True, text=True)

lines = [l for l in result.stdout.splitlines() if l.strip()]

domain_counts = Counter()
ip_domain_map = defaultdict(set)
domain_timestamps = defaultdict(list)

for line in lines:
    try:
        time_epoch, src_ip, domain = line.split("\t")
        time_epoch = float(time_epoch)

        domain_counts[domain] += 1
        ip_domain_map[src_ip].add(domain)
        domain_timestamps[domain].append(time_epoch)

    except ValueError:
        continue

# =========================
# DNS FREQUENCY REPORT
# =========================
print("DNS DOMAIN FREQUENCY REPORT\n")

for domain, count in domain_counts.most_common():
    print(f"[OK] {domain} → {count} queries")

# =========================
# SOURCE IP → DOMAIN MAP
# =========================
print("\nSOURCE IP → DOMAIN MAPPING\n")

for ip, domains in ip_domain_map.items():
    print(f"{ip} queried:")
    for d in domains:
        print(f"   └─ {d}")

# =========================
# IMPROVED BEACONING CHECK
# =========================
print("\nDNS BEACONING CHECK (Improved)\n")

for domain, times in domain_timestamps.items():

    # Ignore internal / AD / reverse DNS domains
    if (
        domain.endswith(".local")
        or domain.endswith(".in-addr.arpa")
        or "_ldap" in domain
        or "_msdcs" in domain
    ):
        continue

    if len(times) < 5:
        continue  # not enough data

    times.sort()
    intervals = [times[i+1] - times[i] for i in range(len(times)-1)]

    # Ignore bursty traffic (very small gaps)
    if min(intervals) < 1:
        continue

    deviation = pstdev(intervals)

    # Low deviation = periodic behavior
    if deviation < 1:
        print(f"[🚨 POSSIBLE BEACONING] {domain}")
        print(f"    Intervals (seconds): {[round(i,2) for i in intervals]}")
