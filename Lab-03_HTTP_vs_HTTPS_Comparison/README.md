# Lab-03: HTTP vs HTTPS Traffic Comparison

## Objective
The objective of this lab is to compare **HTTP** and **HTTPS** network traffic using Wireshark to understand how encryption impacts data visibility and security. This lab demonstrates what information is exposed in unencrypted communication versus encrypted communication.

---

## Tools Used
- **Wireshark** – Network protocol analyzer
- Web browser (for generating HTTP and HTTPS traffic)

---

## Protocols Analyzed
- **HTTP (Hypertext Transfer Protocol)**
- **HTTPS (HTTP over TLS/SSL)**

---

## Lab Overview
In this lab, network traffic was captured while accessing:
- An **HTTP website** (unencrypted)
- An **HTTPS website** (encrypted)

The captured packets were analyzed to observe:
- Visibility of request methods, URLs, and headers
- TLS handshake behavior
- Differences in payload readability

---

## Security Focus
- HTTP traffic transmits data in **plaintext**, making it vulnerable to interception.
- HTTPS encrypts data using **TLS**, protecting sensitive information from attackers.
- This comparison highlights why modern web applications enforce HTTPS.

---

## Files Included
- `filters.txt` – Wireshark display filters for HTTP, HTTPS, and TLS traffic
- `observations.md` – Detailed comparison and security observations
- `README.md` – Lab description and objectives

---

## ✅ Conclusion
This lab provides a clear comparison between HTTP and HTTPS traffic and demonstrates the critical role of encryption in securing web communications. Understanding this difference is fundamental for detecting network attacks and designing secure systems.
