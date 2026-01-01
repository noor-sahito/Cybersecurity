# Observations – MITM Attack Simulation

## Overview

This document records the observations made during **Lab-04: Man-in-the-Middle (MITM) Attack Simulation**.  
The focus of this lab was to analyze network traffic behavior under HTTP and HTTPS communication and evaluate the feasibility of MITM attacks in each case.

The lab was conducted in a **controlled and ethical environment** using passive traffic analysis only.

---

## Observation 1: HTTP Traffic Interception

When accessing websites over **HTTP**, the captured network traffic revealed the following:

### Key Findings
- HTTP requests and responses were transmitted in **plaintext**
- URLs, request methods (GET/POST), and headers were fully visible
- Cookies and session-related data could be observed
- No encryption or authentication mechanisms were present

### Security Impact
- An attacker positioned between the client and server can:
  - Read sensitive information
  - Modify transmitted data
  - Inject malicious content
- HTTP traffic is **highly vulnerable** to MITM attacks

---

## Observation 2: HTTPS Traffic Interception

When accessing websites over **HTTPS**, a clear difference in traffic behavior was observed:

### Key Findings
- TLS handshake packets were visible
- Server certificate exchange and cipher suite negotiation occurred
- Application data appeared as **encrypted TLS payload**
- No readable content (URLs, credentials, or data) was exposed

### Security Impact
- Even if traffic is intercepted:
  - Data remains confidential
  - Content cannot be modified without detection
- HTTPS significantly **reduces MITM attack effectiveness**

---

## Observation 3: TLS Handshake Visibility

The TLS handshake phase revealed important metadata:

- Client Hello and Server Hello messages were visible
- TLS version and cipher suite selection could be identified
- Certificate validation ensured server authenticity

However:
- Actual application data remained encrypted after the handshake
- Session keys were never exposed in plaintext

This confirms that TLS effectively protects against passive MITM attacks.

---

## Comparative Analysis

| Traffic Type | Data Visibility | Encryption | MITM Risk |
|-------------|----------------|------------|-----------|
| HTTP        | Fully visible  | None       | High      |
| HTTPS       | Encrypted      | TLS        | Very Low  |

---

## MITM Attack Feasibility Summary

### Successful Conditions
- Unencrypted communication (HTTP)
- Lack of authentication
- Absence of integrity checks

### Failed Conditions
- Encrypted communication (HTTPS)
- Proper TLS certificate validation
- Secure key exchange mechanisms

---

## Security Insights

- MITM attacks rely heavily on weak or missing encryption
- HTTPS with TLS prevents:
  - Credential theft
  - Data manipulation
  - Session hijacking
- Encryption alone is not enough—**certificate validation** is equally critical

---

## Real-World Relevance

These observations explain why MITM attacks are commonly found in:
- Public Wi-Fi environments
- Rogue access points
- DNS spoofing scenarios

They also highlight why modern browsers warn users when HTTPS is missing or misconfigured.

---

## Conclusion

This lab demonstrates that **MITM attacks are trivial against HTTP traffic** but **largely ineffective against properly implemented HTTPS**.  
The observations reinforce the importance of encryption, authentication, and integrity protection in modern network security.

Understanding these behaviors is essential for detecting MITM threats and designing secure communication systems.

---

**Lab Status:** Completed  
**Nature:** Educational and ethical simulation
