import subprocess
from collections import defaultdict
from statistics import pstdev, mean

PCAP_FILE = "2020-05-28-traffic-analysis-exercise.pcap"

print("[*] Extracting HTTP POST timestamps...")

cmd = [
    "tshark",
    "-r", PCAP_FILE,
    "-Y", "http.request.method == \"POST\"",
    "-T", "fields",
    "-e", "frame.time_epoch",
    "-e", "ip.src",
    "-e", "ip.dst",
    "-e", "http.host",
    "-e", "http.request.uri"
]

result = subprocess.run(cmd, capture_output=True, text=True)

# Group timestamps by communication flow
flows = defaultdict(list)

for line in result.stdout.splitlines():
    try:
        ts, src, dst, host, uri = line.split("\t")
        key = (src, dst, host, uri)
        flows[key].append(float(ts))
    except ValueError:
        continue

print("\n=== HTTP Beaconing Analysis (POST-based) ===\n")

for (src, dst, host, uri), times in flows.items():
    # Require enough samples to calculate meaningful intervals
    if len(times) < 4:
        continue

    times.sort()

    # Calculate time intervals between consecutive requests
    intervals = [times[i + 1] - times[i] for i in range(len(times) - 1)]

    avg_interval = mean(intervals)
    deviation = pstdev(intervals)

    # Detect low-and-slow beaconing with limited jitter
    if avg_interval > 20 and deviation < avg_interval * 0.3:
        print("[🚨 POSSIBLE BEACONING DETECTED]")
        print(f" Source → Destination: {src} → {dst}")
        print(f" Host: {host}")
        print(f" URI: {uri}")
        print(f" Average interval: {round(avg_interval, 2)} seconds")
        print(f" Std deviation: {round(deviation, 2)} seconds")
        print(f" Intervals: {[round(i, 2) for i in intervals]}\n")

print("[*] Beaconing detection complete.")
