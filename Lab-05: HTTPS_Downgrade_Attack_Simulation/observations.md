# Observations – HTTPS Downgrade Attack Simulation (Lab-05)

## Overview

This document records the observations made during **Lab-05: HTTPS Downgrade Attack Simulation**.  
The lab focused on identifying downgrade conditions by analyzing **HTTP vs HTTPS behavior** using `curl` and validating traffic at the network level using Wireshark.

The goal was to understand how downgrade attacks occur and how modern security mechanisms prevent them.

---

## Observation 1: HTTP Access Behavior

When accessing websites over **HTTP**, the following behaviors were observed:

- Some websites responded directly over **HTTP** without enforcing HTTPS.
- HTTP traffic was transmitted in **plaintext**.
- Request headers, URLs, and response codes were fully visible.
- These sites are **potentially vulnerable** to downgrade and MITM attacks.

**Example curl command:**
```
curl -I http://example.com
```

**Observation:**
- If no redirect occurs, the site does not strictly enforce HTTPS.
- This creates an opportunity for downgrade attacks.

---

## Observation 2: HTTP → HTTPS Redirection

For most modern websites:

- HTTP requests were automatically redirected to HTTPS.
- Response codes such as **301 (Moved Permanently)** or **302 (Found)** were observed.
- This behavior prevents users from remaining on an insecure connection.

**Example curl command:**
```
curl -I http://example.com
```

**Observation:**
- Presence of redirection significantly reduces downgrade risk.
- Redirect enforcement is a critical security control.

---

## Observation 3: HTTPS Enforcement and HSTS

When inspecting HTTPS responses:

- Some websites returned the **Strict-Transport-Security (HSTS)** header.
- HSTS instructs browsers to **never use HTTP** for future connections.

**Example curl command:**
```
curl -I https://example.com | grep -i strict-transport-security
```

**Observation:**
- Websites with HSTS enabled are **not vulnerable** to downgrade attacks.
- Even if an attacker attempts to redirect traffic to HTTP, the browser blocks it.

---

## Observation 4: HTTPS Traffic Characteristics

HTTPS traffic displayed the following properties:

- TLS handshake messages were visible.
- Cipher suite negotiation occurred successfully.
- Application data was fully **encrypted**.
- Payload contents were unreadable.

**Observation:**
- HTTPS effectively prevents attackers from reading or modifying traffic.
- Downgrade attempts fail when HTTPS is strictly enforced.

---

## Observation 5: Network-Level Verification (Wireshark)

Wireshark was used to validate curl-based observations:

- HTTP traffic appeared in plaintext.
- HTTPS traffic showed TLS handshakes and encrypted application data.
- No sensitive data was visible in HTTPS sessions.

**Observation:**
- Network-level evidence confirmed curl findings.
- HTTPS successfully protects confidentiality and integrity.

---

## Observation 6: Downgrade Risk Comparison

| Scenario | Downgrade Risk |
|--------|----------------|
| HTTP only | High |
| HTTP → HTTPS redirect | Low |
| HTTPS + HSTS | Very Low |
| HTTPS only | Very Low |

---

## Security Implications

From the observations:

- Downgrade attacks rely on **weak HTTPS enforcement**.
- Sites without redirects or HSTS are vulnerable.
- HTTPS with HSTS provides strong protection against downgrade and MITM attacks.

---

## Key Takeaways

- HTTPS downgrade attacks exploit insecure configurations, not HTTPS itself.
- `curl` is effective for policy-level analysis (redirects, headers).
- Wireshark confirms behavior at the protocol level.
- Strong HTTPS enforcement and HSTS are essential defenses.

---

## Conclusion

The observations from this lab clearly demonstrate that **modern HTTPS configurations effectively prevent downgrade attacks**. Using `curl` and Wireshark together provides a complete understanding of both application-level and network-level security behavior.

This lab reinforces the importance of HTTPS enforcement in real-world web security.
