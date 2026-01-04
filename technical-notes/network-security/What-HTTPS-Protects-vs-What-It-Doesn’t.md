# What HTTPS Protects vs What It Doesn’t

## Overview

HTTPS (Hypertext Transfer Protocol Secure) is designed to protect data exchanged between a client and a server. While HTTPS provides strong security guarantees, it does **not** make communication completely invisible. Understanding what HTTPS protects — and what it does not — is essential for realistic network security analysis.

---

## What HTTPS Protects

### 1. Data Confidentiality (Payload Encryption)

HTTPS encrypts the **content** of communication using TLS.

Protected data includes:
- HTTP request bodies
- HTTP response bodies
- Form submissions
- Login credentials
- Cookies marked as `Secure`
- API request and response data

 Result: Attackers cannot read the actual content of communication even if they capture the packets.

---

### 2. Data Integrity

HTTPS ensures that data is not altered in transit.

- TLS uses cryptographic checks (MAC / AEAD)
- Any modification to encrypted data invalidates the session

 Result: Attackers cannot silently modify requests or responses.

---

### 3. Server Authentication

HTTPS verifies the **identity of the server** using digital certificates.

- Certificates are issued by trusted Certificate Authorities (CAs)
- Browsers validate:
  - Certificate chain
  - Domain name match
  - Certificate expiration

 Result: Clients know they are talking to the legitimate server, not an impersonator.

---

### 4. Protection Against Passive Attacks

HTTPS protects against:
- Packet sniffing
- Credential harvesting
- Session hijacking (in most cases)
- Passive Man-in-the-Middle monitoring

 Result: Captured traffic appears as encrypted TLS Application Data.

---

## What HTTPS Does NOT Protect

### 1. IP Addresses

The following remain visible:
- Client IP address
- Server IP address

 Reason: IP routing requires source and destination addresses to be readable.

---

### 2. Domain Name (Usually)

Even with HTTPS:
- The **destination domain** is often visible through:
  - DNS queries
  - TLS SNI (Server Name Indication)

 Example:
- Observers can see `example.com`
- But cannot see `/login` or form data

---

### 3. Port Numbers

- Port 443 (HTTPS) is always visible
- Port numbers are part of the TCP header

 Result: Attackers know HTTPS is being used, just not the content.

---

### 4. Traffic Timing and Size (Traffic Analysis)

HTTPS does **not** hide:
- Packet sizes
- Timing patterns
- Request frequency
- Session duration

 Advanced attackers can infer behavior using traffic analysis techniques.

---

### 5. Certificate Information

TLS certificates are sent in plaintext during the handshake:
- Certificate issuer
- Domain name
- Validity period

 This metadata helps attackers fingerprint services.

---

### 6. Attacks on Endpoints

HTTPS does not protect against:
- Malware on the client
- Compromised servers
- Keyloggers
- Browser exploits
- Stolen private keys

 Encryption only protects data **in transit**, not endpoints.

---

## Summary Table

| Feature | Protected by HTTPS |
|------|------------------|
Payload content |  Yes |
Credentials |  Yes |
Session integrity |  Yes |
Server authentication |  Yes |
Client IP address |  No |
Server IP address |  No |
Domain name |  Partially |
Traffic patterns |  No |
Endpoint compromise |  No |

---

## Security Takeaway

HTTPS is a **critical security layer**, but it is not complete anonymity. It must be combined with:
- Secure DNS (DoH / DoT)
- VPNs (when appropriate)
- Proper certificate management
- Secure endpoint practices

Understanding HTTPS limitations helps security professionals design stronger, layered defenses.

---

## Conclusion

HTTPS protects **what matters most — the data itself** — but leaves enough metadata exposed to support routing and performance. Recognizing this balance is key to realistic threat modeling and network security analysis.
