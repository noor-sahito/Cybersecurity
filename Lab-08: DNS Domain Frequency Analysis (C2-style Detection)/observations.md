# Lab-08 Observations: DNS Domain Frequency Analysis

## DNS Traffic Overview

- The PCAP file contained multiple DNS queries generated over time
- DNS queries were extracted without inspecting payloads
- Analysis focused solely on **query frequency**

---

## Suspicious Patterns Observed

- Some domains were queried **far more frequently** than others
- High-frequency, repetitive queries are **not typical of human browsing**
- This behavior resembles **C2 beaconing**, where malware periodically contacts a server

---

## Why High-Frequency Domains Matter

Normal user behavior:
- Many domains
- Low repetition
- Irregular timing

C2-style behavior:
- Few domains
- High repetition
- Consistent querying patterns

This lab highlights **frequency as a powerful detection signal**.

---

## Defensive Security Implications

- DNS logs are extremely valuable for threat detection
- C2 traffic often relies on DNS for:
  - Initial communication
  - Fallback channels
  - Domain generation algorithms (DGA)

Python automation allows:
- Fast triage of PCAPs
- Detection of anomalies at scale
- SOC-friendly workflows

---

## Limitations

- Frequency alone does not confirm malware
- Legitimate services (CDNs, updates) may generate high DNS volume
- Further analysis is required:
  - Timing analysis
  - Domain reputation
  - JA3 / TLS correlation

---

## Conclusion

This lab demonstrates how **simple Python scripts combined with tshark** can uncover suspicious DNS behavior indicative of C2 communication.

Even without decrypting traffic or using advanced tools, defenders can identify anomalies using **basic frequency analysis**.

---

## Lab Status

Completed  
Educational analysis only  
Defensive cybersecurity focus
