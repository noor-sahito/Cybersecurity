# Lab-06: JA3 Fingerprinting & TLS Client Identification

## Objective

The objective of this lab is to understand **JA3 fingerprinting**, a technique used to identify TLS clients based on their TLS handshake characteristics.

This lab demonstrates:

- How TLS Client Hello messages can uniquely identify clients
- What JA3 fingerprints are and how they are generated
- How Wireshark can be used to extract JA3-related fields
- Why encryption does not fully prevent client identification

---

## Background

JA3 fingerprinting is a method used to identify TLS clients by hashing specific fields from the **TLS Client Hello** message.

Even though HTTPS encrypts application data, the **TLS handshake metadata remains visible**, allowing:

- Client identification
- Behavioral tracking
- Malware detection
- Bot and automation detection

JA3 is commonly used in:
- Network security monitoring
- Threat detection systems
- Intrusion detection systems (IDS)
- Traffic profiling and anomaly detection

---

## Tools Used

- **Wireshark** – TLS packet capture and analysis
- **Web Browser** – Generating TLS traffic
- **curl** – Generating alternative TLS client fingerprints
- **Local Network (Controlled Environment)**

>  This lab is educational only and performed in a controlled environment.

---

## Lab Environment

- **Client:** Web browser and curl
- **Network:** Local machine
- **Protocol:** TLS (HTTPS)
- **TLS Version:** TLS 1.2 / TLS 1.3 (depending on client)

---

## Lab Overview

In this lab:

1. TLS traffic is captured using Wireshark
2. Client Hello packets are analyzed
3. JA3-relevant fields are extracted
4. Differences between browser and curl TLS fingerprints are observed
5. Client identification is demonstrated without decrypting traffic

---

## High-Level Workflow

1. Start Wireshark capture
2. Generate HTTPS traffic using:
   - Browser
   - curl
3. Filter TLS Client Hello packets
4. Observe cipher suites, extensions, and supported groups
5. Understand how these values form a JA3 fingerprint

---

## Security Relevance

JA3 fingerprinting proves that:

- Encryption protects **data**, not **identity**
- TLS metadata can still leak client behavior
- Different tools create different TLS fingerprints
- Attackers and defenders both rely on fingerprinting

---

## Conclusion

This lab demonstrates how encrypted traffic can still reveal identifying information through TLS handshake metadata. JA3 fingerprinting is a powerful technique used in modern network security to detect threats, identify clients, and monitor encrypted traffic without breaking encryption.

---

## Lab Status

Completed  
Educational use only  
Safe and ethical practice
