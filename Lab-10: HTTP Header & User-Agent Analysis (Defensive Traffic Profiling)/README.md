# Lab-10: HTTP Header & User-Agent Analysis (Defensive Traffic Profiling)

## Objective

The objective of this lab is to analyze HTTP request headers—specifically **User-Agent** and **Host** fields—to identify abnormal or suspicious client behavior using Python and packet capture (PCAP) data.

This lab demonstrates how **unencrypted HTTP metadata** can be leveraged by defenders to detect:
- Unusual or rare User-Agents
- Automated tools and scripts
- Potential malware or scanning activity
- Header anomalies that deviate from normal browser traffic

---

## Tools & Technologies Used

- **Python 3**
- **tshark** (Wireshark CLI)
- **PCAP file** containing HTTP traffic
- Python modules:
  - `subprocess`
  - `collections.Counter`

---

## Data Source

- Packet Capture (`.pcap`) containing HTTP requests
- Extracted fields:
  - Source IP
  - Host header
  - HTTP method
  - User-Agent string

---

## Key Concepts Covered

- HTTP header inspection
- User-Agent fingerprinting
- Frequency-based anomaly detection
- Identifying rare or suspicious clients
- Defensive traffic analysis using metadata

---

## Lab Methodology

1. Use `tshark` to extract HTTP request headers from a PCAP file
2. Parse the extracted data using Python
3. Count occurrences of User-Agents and Hosts
4. Identify:
   - Most common User-Agents
   - Rare User-Agents (potential anomalies)
5. Analyze results from a defensive security perspective

---

## Files Included

- `http_header_analysis.py` – Python script for header extraction and analysis  
- `observations.md` – Findings and defensive insights  
- `README.md` – Lab overview and methodology  

---

## Ethical Notice

This lab is **strictly defensive and educational**.  
No exploitation, malware development, or offensive activity is performed.

---

## Lab Status

**Completed**  
Defensive cybersecurity practice  
Safe and ethical traffic analysis
