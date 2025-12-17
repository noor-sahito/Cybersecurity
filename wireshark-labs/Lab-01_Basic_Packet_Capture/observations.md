# Observations – Wireshark Lab 01  
**Basic Packet Capture & Analysis**


## IP Address Analysis

- IP addresses such as `192.168.1.1` and the range `192.168.0.0/16` are **private IP addresses**.
- These IPs belong to the **local network (LAN)** and are not routable on the public internet.
- `192.168.1.1` commonly represents the **default gateway (router)** in home or small office networks.
- `192.168.0.0/16` represents the **entire private LAN range** (from `192.168.0.0` to `192.168.255.255`).
- Private IP addresses are **safe to document publicly** as they are shared across millions of networks.


## Internal vs External Traffic

- Traffic within `192.168.0.0/16` represents **internal (local) communication**.
- The filter `!ip.addr == 192.168.0.0/16` is used to identify **external (internet) traffic**.
- Even when payloads are encrypted, **metadata such as IP addresses and ports remain visible**.
- Separating internal and external traffic is a key skill in **network monitoring and SOC analysis**.


## DNS and HTTPS Behavior

- DNS traffic reveals the **domain names** a system is attempting to access.
- HTTPS traffic uses **TCP port 443** and encrypts the application data.
- While HTTPS payloads cannot be read, destination IPs and connection patterns can still be analyzed.
- This demonstrates how encryption protects content but not all traffic information.
  

## TCP Flags Analysis

### SYN (Synchronize)
- Indicates a **request to initiate a TCP connection**.
- Commonly seen at the start of communication.
- Excessive SYN packets without ACK responses may indicate **SYN flood or scanning activity**.

### ACK (Acknowledgment)
- Confirms that data has been **successfully received**.
- Most TCP packets include the ACK flag once a connection is established.
- Indicates **normal and healthy communication**.

### RST (Reset)
- Forcefully terminates a TCP connection.
- Common reasons include closed ports, firewall rules, or rejected connections.
- Repeated RST packets may suggest **port scanning or blocked traffic**.


## TCP Three-Way Handshake

1. **SYN** – Client requests a connection  
2. **SYN + ACK** – Server accepts the request  
3. **ACK** – Client confirms the connection  

This handshake is mandatory for all TCP-based communication.


## Security Insights

- Private IP addresses cannot be accessed from the internet, making them safe for lab documentation.
- Traffic analysis focuses on **patterns, flags, and metadata**, not just payloads.
- TCP flag analysis helps identify:
  - Normal traffic
  - Failed connections
  - Potential attacks (e.g., scans, DoS attempts)


##  Conclusion

This lab provided practical exposure to packet capturing, traffic filtering, and TCP behavior analysis using Wireshark. It strengthened understanding of how local and external communication works and highlighted the importance of metadata analysis in cybersecurity investigations.
