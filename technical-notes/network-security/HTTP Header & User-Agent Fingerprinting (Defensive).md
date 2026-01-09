# HTTP Header & User-Agent Fingerprinting (Defensive Detection)

## Overview

HTTP Header and User-Agent fingerprinting is a defensive network security technique used to identify, classify, and detect clients based on how they construct HTTP requests.

Even when traffic is encrypted with HTTPS, **HTTP headers and User-Agent behavior (when visible at endpoints, proxies, or logs)** can reveal valuable metadata about the originating client.

This technique is widely used in:
- SOC environments
- Web Application Firewalls (WAFs)
- Network Detection & Response (NDR)
- Malware and bot detection systems

---

## What Is HTTP Fingerprinting?

HTTP fingerprinting analyzes patterns in:
- HTTP request headers
- Header ordering
- Header presence or absence
- User-Agent strings
- Request behavior consistency

Unlike content inspection, fingerprinting focuses on **how** a request is made rather than **what** is requested.

---

## User-Agent Fingerprinting

The **User-Agent (UA)** header identifies the client software making the request.

### Examples
- Browser:
  ```
  Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0.0.0
  ```
- curl:
  ```
  curl/8.4.0
  ```
- Suspicious / Malware-like:
  ```
  Mozilla/4.0
  Python-urllib/3.9
  Go-http-client/1.1
  ```

### Defensive Observations
- Legitimate browsers have **complex, consistent UA strings**
- Malware often uses:
  - Default library UAs
  - Outdated browser identifiers
  - Static or generic strings
- Sudden UA changes from the same IP can indicate automation

---

## HTTP Header Analysis

### Common Headers in Legitimate Browsers
- Host
- User-Agent
- Accept
- Accept-Encoding
- Accept-Language
- Connection
- Upgrade-Insecure-Requests

### Common Anomalies in Suspicious Traffic
- Missing common headers
- Minimal header sets
- Non-standard casing or ordering
- Inconsistent headers across requests

Example suspicious request:
```
GET /update HTTP/1.1
Host: example.com
User-Agent: Python-urllib/3.9
```

---

## Header Ordering Fingerprinting

Header order is often **deterministic** for:
- Browsers
- HTTP libraries
- Malware frameworks

Example:
- Chrome sends headers in a predictable order
- curl sends fewer headers in a fixed sequence
- Malware may send headers in unusual or inconsistent order

This allows defenders to fingerprint clients **even if the User-Agent is spoofed**.

---

## Browser vs curl vs Malware (High-Level Comparison)

| Feature | Browser | curl | Malware-like |
|------|--------|------|-------------|
| User-Agent | Complex | Simple | Generic / Fake |
| Header Count | High | Medium | Low |
| Header Order | Stable | Stable | Irregular |
| Accept-Language | Present | Often missing | Missing |
| Behavior | Human-like | Scripted | Automated |

---

## HTTPS Considerations

While HTTPS encrypts payload data:
- Headers are visible at endpoints
- Proxies, WAFs, and reverse proxies can log headers
- Malware often exposes itself **before encryption** or at controlled endpoints

This makes HTTP fingerprinting a **critical complement** to TLS/JA3 analysis.

---

## Defensive Use Cases

HTTP fingerprinting is used to:
- Detect bots and scrapers
- Identify malware beaconing over HTTP/HTTPS
- Correlate with JA3/TLS fingerprints
- Enrich threat intelligence
- Support incident response investigations

---

## Limitations

- User-Agent strings can be spoofed
- Advanced malware may mimic real browsers
- Requires correlation with:
  - TLS fingerprints
  - DNS behavior
  - Timing analysis
  - IP reputation

Fingerprinting is strongest when used as **part of a layered defense**.

---

## Key Takeaways

- HTTP headers leak valuable behavioral metadata
- User-Agent analysis remains a powerful detection signal
- Header ordering is harder to fake than UA strings
- Best results come from combining:
  - HTTP fingerprinting
  - TLS fingerprinting
  - DNS and timing analysis

---

## Ethical Notice

This document is written from a **defensive security perspective only**.  
It does not provide guidance on evasion or malicious activity.

---

## Status

Completed  
Defensive security documentation  
Aligned with SOC and blue-team practices
