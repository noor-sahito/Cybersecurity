## What is the OSI Security Architecture?

It’s a framework developed by ISO (International Organization for Standardization) that describes how to secure communications and data within the OSI model — the same 7-layer model used for networking (Physical → Application).

Main Goals of the OSI Security Architecture
	1.	Define security attacks — what threats exist.
	2.	Define security services — what protection is needed.
	3.	Define security mechanisms — how that protection is provided.

 1. Types of Security Attacks

There are two broad categories:

A. Passive Attacks (Listening/Monitoring)

 Goal: To read or observe data without changing it.
Examples:
	•	Eavesdropping / Interception
	•	Traffic analysis

Countered by: Encryption, secure routing, VPNs.

B. Active Attacks (Tampering/Disruption)

 Goal: To modify, destroy, or disrupt communication.
Examples:
	•	Masquerade (Impersonation)
	•	Replay Attack (resending captured data)
	•	Modification of Messages
	•	Denial of Service (DoS)

 Countered by: Authentication, Integrity Checks (MAC, hashing), Firewalls, IDS/IPS, Availability controls.


 2. Security Services (What we protect)

There are five main security services defined in the OSI model:

Security Service	Description	Example
1. Authentication	Verifies identity of users or systems.	Passwords, digital certificates, biometrics
2. Access Control	Controls who can access what.	ACLs, firewalls, role-based access
3. Data Confidentiality	Prevents unauthorized disclosure of information.	Encryption (AES, TLS, VPN)
4. Data Integrity	Ensures data isn’t altered during transmission.	Hashing, checksums, MAC
5. Non-repudiation	Prevents denial of sending/receiving messages.	Digital signatures, audit logs
3. Security Mechanisms (How we protect)

These are the tools and techniques used to implement the security services.

A. Specific Security Mechanisms

(Used directly to implement services)
	•	Encipherment (Encryption/Decryption)
	•	Digital Signatures
	•	Access Control Mechanisms
	•	Data Integrity Mechanisms (hashing, MAC)
	•	Authentication Exchange (passwords, certificates)
	•	Traffic Padding (adding fake data to hide patterns)
	•	Routing Control (secure routing paths)
	•	Notarization (third-party verification)


B. Pervasive Security Mechanisms

(Apply across all layers)
	•	Trusted Functionality (OS or hardware trusted components)
	•	Security Labels (classification levels, e.g., Secret, Confidential)
	•	Event Detection (IDS/IPS, anomaly detection)
	•	Security Audit Trail (logging and monitoring)
	•	Security Recovery (restore system to secure state after attack)

Mapping Example: OSI Layers vs Security

OSI Layer	Common Security Mechanisms
Application	Authentication, Encryption (SSL/TLS), Digital Signatures
Presentation	Data Encryption, Compression Security
Session	Session Authentication, Key Exchange
Transport	SSL/TLS, Port Security
Network	IPsec, Firewalls, Routing Control
Data Link	MAC address filtering, VLAN security
Physical	Physical Access Control, CCTV, Biometric locks
