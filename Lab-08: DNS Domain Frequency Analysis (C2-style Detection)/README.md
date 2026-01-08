# Lab-08: DNS Domain Frequency Analysis (C2-Style Detection)

## Objective

The objective of this lab is to analyze **DNS traffic** captured in a PCAP file and identify **potential Command-and-Control (C2) communication patterns** using Python.

This lab focuses on detecting **abnormal domain access behavior**, such as:

- Excessive DNS queries to the same domain
- Beaconing-like communication patterns
- Domains that may indicate malware or automated activity

Python is used as a **defensive analysis tool** in combination with **tshark** to extract and process DNS data.

---

## Tools & Technologies Used

- **Python 3**
- **tshark** (Wireshark CLI)
- `subprocess` module
- `collections.Counter`
- PCAP file containing DNS traffic

---

## Key Concepts Covered

- DNS traffic analysis
- C2-style domain behavior
- Beaconing detection via frequency analysis
- Python for cybersecurity automation
- Using tshark programmatically

---

## Lab Environment

- **Traffic Type:** DNS
- **Data Source:** Packet Capture (`.pcap`)
- **Analysis Method:** Offline (PCAP-based)
- **Network Type:** Controlled / lab environment

---

## Lab Workflow

1. Load a DNS PCAP file
2. Extract DNS query names using tshark
3. Count domain frequencies using Python
4. Flag suspicious domains based on query volume
5. Analyze results from a defender’s perspective

---

## Files Included

- `dns_analysis.py` – Python script for DNS frequency analysis  
- `observations.md` – Findings and security insights  
- `README.md` – Lab overview and methodology  

---

## Ethical Notice

This lab is **strictly defensive and educational**.  
No malware, exploitation, or live attacks are performed.

---

## Lab Status

Completed  
Defensive cybersecurity practice  
Safe and ethical analysis
