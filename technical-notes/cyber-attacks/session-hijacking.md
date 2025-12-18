# Session Hijacking

##  What is Session Hijacking?
Session hijacking is a cyber attack in which an attacker takes control of a valid user session by stealing or predicting the **session identifier (Session ID)** used by a web application. Once the session ID is compromised, the attacker can impersonate the legitimate user without knowing their username or password.

Session hijacking mainly targets **authenticated sessions** after a successful login.

---

##  How Session Hijacking Works (Step-by-Step)

1. A user logs into a website or application.
2. The server creates a unique **session ID** and stores it in:
   - Cookies
   - URL parameters
   - HTTP headers
3. The attacker intercepts or steals the session ID using various techniques.
4. The attacker reuses the session ID to access the application.
5. The server assumes the attacker is the legitimate user.

---

##  Common Session Hijacking Techniques

### 1. Session Sniffing
- Attacker captures network traffic using tools like **Wireshark**
- Common on unsecured public Wi-Fi networks
- Works when data is sent over **HTTP instead of HTTPS**

### 2. Cross-Site Scripting (XSS)
- Malicious JavaScript is injected into a webpage
- Script steals session cookies and sends them to the attacker

### 3. Session Fixation
- Attacker forces a victim to use a known session ID
- Once the victim logs in, the attacker uses the same session ID

### 4. Man-in-the-Middle (MITM)
- Attacker secretly intercepts communication between user and server
- Often performed on fake or compromised Wi-Fi hotspots

### 5. Session Hijacking via Malicious Links
- Victim clicks a crafted link containing a session token
- Common in phishing attacks and social engineering

---

##  Tools Commonly Used
- **Wireshark** – packet capturing and traffic analysis
- **Burp Suite** – intercepting and modifying HTTP requests
- **Ettercap** – MITM attacks
- **Browser Developer Tools** – cookie inspection

---

##  Real-World Example
If a user logs into a website over public Wi-Fi without HTTPS, an attacker can capture the session cookie. By injecting this cookie into their browser, the attacker gains access to the victim’s account without authentication.

---

##  Prevention and Mitigation

### For Developers
- Always use **HTTPS (TLS/SSL)**
- Set cookies with:
  - `HttpOnly`
  - `Secure`
  - `SameSite` attributes
- Regenerate session ID after login
- Implement session expiration and logout handling
- Use strong random session identifiers

### For Users
- Avoid public Wi-Fi for sensitive logins
- Always log out after use
- Enable two-factor authentication (2FA)
- Keep browsers and OS updated

---

## Related Attacks
- Cross-Site Scripting (XSS)
- Man-in-the-Middle (MITM)
- Phishing Attacks
- Credential Harvesting

---

##  Key Takeaway
Session hijacking allows attackers to bypass authentication completely by abusing session
