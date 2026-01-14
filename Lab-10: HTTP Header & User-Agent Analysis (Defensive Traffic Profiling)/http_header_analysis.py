import subprocess
from collections import Counter

PCAP_FILE = "traffic.pcap"

def extract_http_headers():
    """
    Extract HTTP request headers using tshark
    """
    cmd = [
        "tshark",
        "-r", PCAP_FILE,
        "-Y", "http.request",
        "-T", "fields",
        "-e", "ip.src",
        "-e", "http.host",
        "-e", "http.request.method",
        "-e", "http.user_agent"
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.stdout.splitlines()

def analyze_headers(lines):
    user_agents = Counter()
    hosts = Counter()

    for line in lines:
        fields = line.split("\t")
        if len(fields) != 4:
            continue

        ip, host, method, user_agent = fields

        if user_agent:
            user_agents[user_agent] += 1
        if host:
            hosts[host] += 1

    return user_agents, hosts

def print_top(counter, title, limit=10):
    print(f"\n=== {title} ===")
    for item, count in counter.most_common(limit):
        print(f"{count:5}  {item}")

def main():
    print("[*] Extracting HTTP headers from PCAP...")
    lines = extract_http_headers()

    print("[*] Analyzing headers...")
    user_agents, hosts = analyze_headers(lines)

    print_top(user_agents, "Top User-Agents")
    print_top(hosts, "Top Hosts")

    print("\n[*] Potential Anomalies (User-Agents seen only once):")
    for ua, count in user_agents.items():
        if count == 1:
            print(f"  {ua}")

if __name__ == "__main__":
    main()
