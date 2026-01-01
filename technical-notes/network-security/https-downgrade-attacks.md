# HTTPS Downgrade Attacks – Network Security Analysis

## Overview
An **HTTPS downgrade attack** is a type of network attack where an attacker forces a victim’s secure HTTPS connection to fall back to insecure HTTP. Once downgraded, the attacker can intercept, read, or manipulate sensitive data transmitted between the client and the server.

This attack is commonly performed as part of a **Man-in-the-Middle (MITM)** scenario.

---

## Objective of Downgrade Attacks
The attacker aims to:
- Remove encryption from web traffic
- Expose sensitive data such as:
  - Login credentials
  - Session cookies
  - Personal information
- Bypass TLS protections without the user noticing

---

## How HTTPS Downgrade Attacks Work

### Initial User Request
- User enters a website URL without explicitly specifying `https://`
- Example:
  ```
  example.com
  ```

---

### Attacker Intercepts the Connection
- Attacker positions themselves between client and server
- Common methods:
  - Rogue Wi-Fi access point
  - ARP spoofing
  - DNS spoofing

---

### Forced Downgrade to HTTP
- Attacker blocks or modifies HTTPS redirection
- User is silently redirected to:
  ```
  http://example.com
  ```
- Browser displays the site without encryption

---

### Data Interception
- Since HTTP traffic is plaintext:
  - Credentials are visible
  - Cookies can be stolen
  - Content can be modified in transit

 *User often does not notice the downgrade.*

---

## Common HTTPS Downgrade Techniques

### SSL Stripping
- Attacker strips HTTPS links from web pages
- Forces all connections to remain HTTP
- Popularized by tools like **sslstrip**

---

### Protocol Downgrade
- Attacker interferes during TLS handshake
- Forces weaker or deprecated encryption methods
- Exploits legacy configurations

---

### Redirect Manipulation
- HTTPS redirects (301/302) are blocked or altered
- User never reaches secure endpoint

---

## Downgrade Attacks in Wireshark
When observing traffic:
- Initial HTTPS request may be missing
- Only HTTP requests are visible
- Credentials appear in plaintext
- No TLS handshake packets are observed

 *This behavior was observable in HTTP traffic during Lab-03.*

---

## Security Risks
HTTPS downgrade attacks enable:
- Credential theft
- Session hijacking
- Data tampering
- Malware injection
- Privacy violations

They are especially dangerous on **public Wi-Fi networks**.

---

## Prevention and Mitigation Techniques

### Enforce HTTPS Everywhere
- Websites must redirect HTTP → HTTPS immediately
- Avoid mixed-content resources

---

### HTTP Strict Transport Security (HSTS)
- Instructs browsers to **always use HTTPS**
- Prevents downgrade attempts even before first request

---

### Certificate Validation
- Browsers must validate TLS certificates
- Invalid certificates should trigger warnings

---

### User Awareness
- Users should check:
  - HTTPS lock icon
  - Certificate details
- Avoid logging in on unsecured networks

---

## Relation to Other Security Concepts
- HTTPS downgrade attacks are a **subset of MITM attacks**
- TLS handshake protection prevents downgrade
- HSTS directly blocks SSL stripping attacks

---

## Relation to Practical Labs
In **Lab-03 (HTTP vs HTTPS Comparison)**:
- HTTP traffic exposed request data in plaintext
- HTTPS traffic protected payload using TLS
- This contrast demonstrates the real-world impact of downgrade attacks

---

## Conclusion
HTTPS downgrade attacks exploit insecure configurations and user trust to bypass encryption. By forcing traffic from HTTPS to HTTP, attackers gain full visibility into sensitive communications. Strong TLS enforcement, HSTS, and proper certificate validation are essential defenses against these attacks.

Understanding downgrade attacks is critical for secure network design and traffic analysis.
