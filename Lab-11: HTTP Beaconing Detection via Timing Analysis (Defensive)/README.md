# Lab-11: HTTP Beaconing Detection via Timing Analysis (Defensive)

## Objective
This lab focuses on detecting **HTTP-based Command-and-Control (C2) beaconing**
by analyzing **timing patterns** in HTTP POST requests.

Rather than relying on indicators such as IP reputation or known malware signatures,
this lab uses **statistical analysis of request intervals** to identify
low-and-slow beaconing behavior commonly used by advanced malware.

---

## Why This Matters
Modern malware often:
- Uses **legitimate protocols** (HTTP/HTTPS)
- Avoids large payloads
- Communicates at **regular or semi-regular intervals**
- Blends in with normal web traffic

Signature-based detection often fails against this technique.
Timing analysis provides a **behavioral detection approach**.

---

## Detection Technique
The lab detects beaconing by analyzing:
- Repeated HTTP POST requests
- Fixed or low-jitter intervals between requests
- Long average intervals with low variance

This pattern is typical of:
- C2 check-ins
- Exfiltration beacons
- Keep-alive malware traffic

---

## Tools Used
- `tshark` (packet extraction)
- Python 3
- `statistics` module for interval analysis

---

## Input
- PCAP file containing HTTP traffic
- HTTP POST requests extracted from the capture

---

## Output
The script flags potential beaconing flows and prints:
- Source and destination IPs
- Host and URI
- Average beacon interval
- Standard deviation of intervals

---

## Ethical Notice
This lab is intended for:
- Defensive security research
- Blue-team training
- Malware traffic analysis

No exploitation techniques are demonstrated.
