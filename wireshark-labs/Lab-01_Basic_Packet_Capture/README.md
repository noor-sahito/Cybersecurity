# Wireshark Lab 01 – Basic Packet Capture & Analysis

##  Objective
The goal of this lab is to understand basic packet capturing using Wireshark and analyze common network traffic such as DNS and HTTPS. 
This lab focuses on identifying source and destination IP addresses, protocols in use, and understanding how encrypted traffic behaves.



 Tools & Environment
- Tool:** Wireshark  
- Operating System:** Windows / macOS  
- Network Type:** Local network (Wi-Fi / Ethernet)


Filters Used
```text
dns
tcp
udp
tcp.port == 443
ip.addr == 192.168.1.1
```


##  Procedure
1. Started Wireshark with the active network interface.
2. Generated traffic by browsing websites and using common applications.
3. Applied protocol-based filters to isolate traffic.
4. Observed packet details such as:
   - Source IP
   - Destination IP
   - Protocol
   - Packet length
5. Identified DNS queries and HTTPS traffic behavior.


##  Observations
- DNS packets reveal **domain names** being requested.
- HTTPS traffic uses **TCP port 443** and is encrypted.
- Packet payloads in HTTPS traffic are not readable due to encryption.
- Source and destination IPs help identify communication endpoints.


## Security Insight
- Even when data is encrypted, **metadata** (IP addresses, ports, protocols) is still visible.
- This demonstrates why attackers can analyze traffic patterns without decrypting payloads.
- Packet analysis is a core skill for **SOC analysts and network security engineers**.

  

##  Conclusion
This lab provided hands-on experience with Wireshark and basic packet analysis. 
It strengthened understanding of how network communication works and how encrypted traffic appears at the packet level.



##  Skills Gained
- Packet capturing
- Wireshark filtering
- Network traffic analysis
- Understanding encrypted communication (HTTPS)
- Cybersecurity fundamentals
