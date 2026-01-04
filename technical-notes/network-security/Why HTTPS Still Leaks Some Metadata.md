# Why HTTPS Still Leaks Some Metadata

## Overview

HTTPS (HTTP over TLS) encrypts the contents of communication between a client and a server. While it provides strong confidentiality, integrity, and authentication, **HTTPS does not hide all information**. Certain metadata remains visible to observers on the network.

Understanding this metadata leakage is important for network security analysis, traffic monitoring, and privacy considerations.

---

## What HTTPS Protects

HTTPS encrypts the **application-layer data**, including:

- URLs and query parameters
- HTTP headers
- Cookies and authentication tokens
- Request and response bodies
- User credentials and form data

This ensures that attackers cannot read or modify the actual content being exchanged.

---

## What Metadata Is Still Visible

Even with HTTPS enabled, the following information remains observable:

### 1. IP Addresses
- Source IP (client)
- Destination IP (server)

These are required for routing packets across the network and cannot be encrypted.

---

### 2. Port Numbers
- Commonly:
  - Port **443** → HTTPS
  - Port **80** → HTTP

Port numbers reveal the type of service being accessed.

---

### 3. TLS Handshake Information
During the TLS handshake, observers can see:

- TLS version (e.g., TLS 1.2, TLS 1.3)
- Cipher suites offered and selected
- Certificate exchange (not private keys)
- Handshake timing

This information is visible before encryption is fully established.

---

### 4. Server Name Indication (SNI)
- The **SNI field** often reveals the domain name being accessed
- Used when multiple websites share the same IP address
- Encrypted only when **Encrypted Client Hello (ECH)** is supported and enabled

---

### 5. Traffic Patterns
Even though payloads are encrypted, attackers can infer information from:

- Packet sizes
- Packet timing
- Session duration
- Volume of data transferred

This can enable **traffic analysis attacks**.

---

## Why This Metadata Cannot Be Fully Hidden

Some metadata must remain visible for the internet to function:

- Routers need IP addresses to forward packets
- Servers need to know which service (port) to respond to
- TLS negotiation requires initial plaintext communication

Encryption focuses on **content protection**, not complete anonymity.

---

## Security and Privacy Implications

Because metadata is visible, attackers can:

- Identify visited services
- Detect HTTPS usage
- Perform traffic analysis
- Correlate user activity patterns

This is why HTTPS alone does not guarantee full privacy.

---

## How Modern Technologies Reduce Metadata Exposure

Some technologies aim to reduce metadata leakage:

- **TLS 1.3** – Encrypts more handshake data
- **Encrypted Client Hello (ECH)** – Hides SNI
- **VPNs** – Mask destination IPs
- **Tor** – Provides anonymity by routing traffic through multiple nodes

---

## Conclusion

HTTPS is essential for securing web communications, but it does not make traffic invisible. While the **content** is protected, **metadata such as IP addresses, ports, and traffic patterns remains exposed**.

Understanding these limitations is crucial for realistic threat modeling, network monitoring, and privacy-aware system design.
