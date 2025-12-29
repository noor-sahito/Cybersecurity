# Observations – DNS & HTTP Traffic Analysis

## Capture Summary
- A short packet capture was performed while browsing standard websites.
- Traffic was analyzed using Wireshark with protocol-based filters.
- The focus was on **DNS resolution** and **HTTP communication**.

---

## DNS Traffic Observations
- DNS queries were observed when a domain name was accessed in the browser.
- The client sent DNS queries to a DNS server over **UDP port 53**.
- DNS responses contained the resolved IP addresses for the requested domains.
- DNS traffic was transmitted in **plaintext**, making queried domain names visible.

**Security Insight:**  
Unencrypted DNS traffic can expose browsing behavior and can be monitored or manipulated by attackers.

---

## HTTP Traffic Observations
- HTTP requests were observed over **TCP port 80**.
- Common HTTP methods such as **GET** were visible in the captured packets.
- Requested
