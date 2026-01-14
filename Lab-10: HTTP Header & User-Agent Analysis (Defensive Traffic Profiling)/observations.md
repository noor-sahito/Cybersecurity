# Observations: HTTP Header & User-Agent Analysis

## Overview

This lab analyzed HTTP request headers extracted from a PCAP file to identify patterns and anomalies in **User-Agent** and **Host** fields. Even without decrypting payloads, HTTP metadata provided valuable insight into client behavior.

---

## Key Findings

### 1. User-Agent Distribution

- A small number of User-Agent strings accounted for the majority of HTTP requests
- These typically resembled common web browsers
- This aligns with expected legitimate user behavior

### 2. Rare User-Agents

- Several User-Agent strings appeared **only once**
- Rare User-Agents are often associated with:
  - Automated scripts
  - Command-line tools
  - Malware or scanners
- These entries warrant further investigation

### 3. Host Header Patterns

- Most requests targeted a limited number of domains
- High-frequency access to a single host may indicate:
  - Automated polling
  - Misconfigured clients
  - Beaconing-like behavior

---

## Security Implications

- User-Agent strings can act as **soft fingerprints**
- Attackers often use:
  - Empty User-Agent fields
  - Hardcoded or outdated values
  - Non-browser identifiers
- Frequency analysis helps surface these anomalies quickly

---

## Defensive Value

This lab demonstrates how defenders can:
- Detect suspicious traffic without payload inspection
- Identify non-human clients in network traffic
- Build baseline profiles of normal HTTP behavior
- Enhance detection rules in NDR, IDS, or SIEM platforms

---

## Conclusion

HTTP header analysis remains a powerful and lightweight defensive technique.  
Even in environments transitioning to HTTPS, legacy HTTP traffic and proxy logs can still provide valuable detection signals.

---

## Ethical Reminder

All analysis was performed in a controlled, educational environment.  
No malicious activity was conducted.
