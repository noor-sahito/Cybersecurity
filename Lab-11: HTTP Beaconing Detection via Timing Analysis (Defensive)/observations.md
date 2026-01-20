# Observations – HTTP Beaconing Timing Analysis

## Key Findings
This lab demonstrates that HTTP beaconing can be identified
by analyzing **request timing patterns**, even when the traffic
uses legitimate protocols and methods.

Several HTTP POST flows exhibited:
- Regular communication intervals
- Low variance between intervals
- Long average delays between requests

These characteristics are consistent with C2 beaconing behavior.

---

## Why Timing Matters
Normal user-driven HTTP traffic is:
- Bursty
- Irregular
- Influenced by human interaction

Beaconing traffic, in contrast:
- Is automated
- Occurs at predictable intervals
- Minimizes noise to avoid detection

Timing analysis exposes this difference.

---

## Detection Strengths
- Does not rely on known IOCs
- Effective against encrypted traffic
- Identifies stealthy, low-bandwidth C2 channels
- Works even when domains and IPs appear benign

---

## Limitations
- Legitimate scheduled jobs may produce false positives
- Thresholds must be tuned per environment
- Short PCAPs may not provide enough data points

---

## Defensive Takeaway
This lab reinforces a critical blue-team principle:

> **Behavioral patterns outlive indicators.**

By focusing on timing, defenders gain visibility
into threats that intentionally avoid traditional detection.
