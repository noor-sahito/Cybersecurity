# Lab-09: DNS C2 Detection with Python

## Objective

The objective of this lab is to **detect potential Command-and-Control (C2) style behavior** by analyzing DNS traffic using **Python**.  
This lab demonstrates how defenders can identify suspicious beaconing and abnormal domain access patterns through **DNS frequency analysis**.

Unlike earlier theoretical notes, this lab focuses on **hands-on detection logic implemented in code**.

---

## Why This Lab Matters

DNS is commonly abused by malware for:

- C2 beaconing
- Domain-based callbacks
- Stealthy communication channels

Even when payloads are encrypted, **DNS metadata remains visible**, making it a powerful detection point for defenders.

This lab shows how **simple Python automation** can surface suspicious behavior from packet captures.

---

## Tools & Technologies Used

- **Python 3**
- **tshark** (Wireshark CLI)
- `subprocess`
- `collections.Counter`
- DNS PCAP file (offline analysis)

---

## Lab Methodology

1. Capture or obtain a PCAP file containing DNS traffic
2. Extract DNS query names using `tshark`
3. Parse output programmatically in Python
4. Count domain query frequencies
5. Identify domains with abnormal or repetitive access patterns
6. Analyze results from a **defensive detection perspective**

---

## Files Included

- `dns_analysis.py`  
  Python script that extracts DNS queries and performs frequency analysis

- `observations.md`  
  Security findings and interpretation of suspicious patterns

- `README.md`  
  Lab overview, methodology, and objectives

---

## Key Detection Signals

- Excessive queries to the same domain
- Repetitive, periodic DNS lookups (beaconing behavior)
- Domains that stand out from normal browsing patterns
- Low-volume but highly consistent access patterns

---

## Example Use Case

```bash
python3 dns_analysis.py dns_traffic.pcap
```

The script outputs domain frequency counts, allowing analysts to quickly spot anomalies.

---

## Defensive Perspective

This lab is strictly **defensive and educational**.

- No malware is executed
- No live attacks are performed
- Analysis is done on offline packet captures
- Focus is on **detection, not exploitation**

---

## Lab Status

- Completed
- Defensive cybersecurity practice
- Safe and ethical analysis
