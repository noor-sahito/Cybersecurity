# Observations – HTTP vs HTTPS Traffic Comparison

## Capture Summary
- Network traffic was captured while visiting one HTTP website and one HTTPS website.
- Wireshark was used to analyze packet-level differences between unencrypted and encrypted communication.
- The analysis focused on **data visibility**, **encryption**, and **security implications**.

---

## HTTP Traffic Observations (Unencrypted)
- HTTP traffic was observed over **TCP port 80**.
- Request methods such as **GET** were clearly visible.
- Requested URLs, resource paths, and headers were readable in plaintext.
- Server responses, including status codes and headers, were also visible.

**Security Impact:**
- Any attacker monitoring the network can:
  - View visited URLs
  - Inspect transmitted data
  - Modify responses (MITM attack)
- HTTP provides **no confidentiality or integrity protection**.

---

## HTTPS Traffic Observations (Encrypted)
- HTTPS traffic was observed over **TCP port 443**.
- Wireshark displayed **TLS handshake messages** (Client Hello, Server Hello).
- After the handshake, application data appeared as **encrypted payload**.
- No readable URLs, parameters, or content were visible in the packets.

**Security Impact:**
- Encryption prevents attackers from reading or modifying transmitted data.
- Only metadata (IP addresses, ports, timing) remains visible.
- TLS ensures **confidentiality, integrity, and authentication**.

---

## Key Differences Observed

| Feature | HTTP | HTTPS |
|-------|------|-------|
| Encryption |  No |  Yes (TLS) |
| Data Visibility | Fully readable | Encrypted |
| Credential Safety | Unsafe | Protected |
| MITM Resistance |  Weak |  Strong |

---

## Security Analysis
- HTTP traffic is highly vulnerable to packet sniffing and manipulation.
- HTTPS significantly reduces attack surface by encrypting application data.
- Even though HTTPS hides content, traffic analysis can still reveal metadata.
- This explains why HTTPS is mandatory for modern applications handling sensitive data.

---

## Conclusion
This lab clearly demonstrates the security advantages of HTTPS over HTTP. While HTTP exposes sensitive information in plaintext, HTTPS protects data through TLS encryption. Understanding this difference is critical for identifying insecure systems and designing secure network architectures.
