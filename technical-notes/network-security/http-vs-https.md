# HTTP vs HTTPS – Network Security Perspective

## Overview
HTTP and HTTPS are protocols used for web communication. While both serve the same purpose of transferring data between a client and a server, they differ significantly in terms of **security**. This document explains their differences from a network security point of view.

---

## HTTP (Hypertext Transfer Protocol)
- Operates over **TCP port 80**
- Data is transmitted in **plaintext**
- No encryption, authentication, or integrity protection
- Easily readable by anyone monitoring network traffic

### Security Risks of HTTP
- Packet sniffing can expose:
  - URLs
  - Query parameters
  - Session tokens
- Vulnerable to **Man-in-the-Middle (MITM)** attacks
- Attackers can modify or inject malicious content
- Not suitable for sensitive data transmission

---

## HTTPS (HTTP Secure)
- Operates over **TCP port 443**
- Uses **TLS (Transport Layer Security)** for encryption
- Provides:
  - Confidentiality
  - Integrity
  - Server authentication

### How HTTPS Secures Communication
1. TLS handshake is initiated
2. Server presents a digital certificate
3. Encryption keys are securely exchanged
4. All application data is encrypted

After the handshake, transmitted data is unreadable to attackers.

---

## Key Differences

| Feature | HTTP | HTTPS |
|------|------|------|
| Encryption |  No |  Yes (TLS) |
| Data Visibility | Plaintext | Encrypted |
| Authentication |  No |  Server identity verified |
| MITM Protection |  Weak |  Strong |
| Recommended Usage |  Deprecated |  Standard |

---

## Security Analysis
- HTTP should never be used for login pages or sensitive data
- HTTPS significantly reduces attack surface on public networks
- Even with HTTPS, metadata such as IP addresses and ports remain visible
- Modern security standards mandate HTTPS by default

---

## Relation to Practical Labs
In **Lab-03 (HTTP vs HTTPS Traffic Comparison)**, HTTP traffic was observed as readable in Wireshark, while HTTPS traffic showed encrypted payloads after the TLS handshake. This practical observation reinforces the theoretical security advantages of HTTPS.

---

## Conclusion
HTTP lacks essential security features and is vulnerable to multiple network attacks. HTTPS, through TLS encryption, provides secure communication and is the standard for modern web applications. Understanding this difference is fundamental for network security analysis and secure system design.
