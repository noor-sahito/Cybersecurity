# Observations – DNS C2 Detection Using Python

## Overview

This lab analyzed DNS traffic from a packet capture (`dns_real.pcap`) to identify **potential Command-and-Control (C2)–style behavior** using Python and `tshark`.  
The analysis focused on **domain query frequency**, **source IP behavior**, and **temporal patterns** indicative of automated beaconing.

All analysis was conducted from a **defensive detection perspective**.

---

## Key Observations

### 1. DNS Domain Frequency Patterns

- Most domains appeared a limited number of times, consistent with **normal user browsing** and application behavior.
- A small subset of domains showed **repeated DNS queries**, which warranted further inspection.
- High query count alone was **not treated as malicious**, as legitimate services (CDNs, cloud providers) may generate frequent DNS lookups.

**Defensive Insight:**  
Domain frequency is a useful **triage signal**, but must be correlated with timing and source behavior to avoid false positives.

---

### 2. Source IP to Domain Mapping

- The script mapped **source IP addresses to the domains they queried**.
- Most internal IPs queried a **diverse set of domains**, consistent with normal endpoint activity.
- In some cases, a single IP repeatedly queried **one specific external domain**, a pattern commonly associated with:
  - Automated scripts
  - Background services
  - Potential beaconing behavior

**Defensive Insight:**  
A **low diversity of domains per host** can be an early indicator of automated communication and should be monitored.

---

### 3. Temporal Analysis & Beaconing Detection

The improved beaconing logic analyzed **time intervals between DNS queries** for each domain:

- Domains with fewer than 5 queries were excluded to reduce noise.
- Bursty traffic (sub-second intervals) was ignored, as it is common for legitimate applications.
- Domains exhibiting **low standard deviation in query intervals** were flagged.

#### Flagged Behavior:
- Domains with **consistent, periodic DNS query intervals**
- Low variance between queries (near-uniform timing)
- Repeated access from the same source IP

These characteristics closely resemble **beaconing behavior** used by malware to maintain contact with C2 infrastructure.

**Example Indicators:**
- Regular DNS queries every X seconds
- Stable interval patterns over time
- Lack of user-driven randomness

---

## False Positive Reduction Techniques Used

To improve accuracy, the following were excluded from beaconing analysis:

- Internal domains (`.local`)
- Reverse DNS (`.in-addr.arpa`)
- Active Directory–related records (`_ldap`, `_msdcs`)
- Domains with insufficient data points

**Defensive Insight:**  
Filtering known benign patterns is critical to ensure detections remain actionable and SOC-friendly.

---

## Security Significance

This analysis demonstrates that **DNS traffic alone**—even without payload inspection—can reveal:

- Automated communication patterns
- Potential C2 beaconing
- Suspicious host-domain relationships

The approach mirrors real-world detection techniques used in:
- Network Detection & Response (NDR)
- Threat hunting
- Blue team investigations

---

## Limitations

- This lab does **not confirm malware**, only suspicious behavior.
- Legitimate services (update agents, monitoring tools) can exhibit similar patterns.
- DNS encryption (DoH / DoT) would reduce visibility in real environments.

---

## Conclusion

By combining:
- DNS frequency analysis
- Source IP correlation
- Timing-based beacon detection

this lab provides a **practical and realistic demonstration** of how defenders can identify potential C2-style behavior using Python and packet data.

The methodology emphasizes **behavioral detection over signatures**, aligning with modern defensive security practices.

---

**Lab Status:**  
✔ Completed  
✔ Defensive analysis only  
✔ Ethical and educational
