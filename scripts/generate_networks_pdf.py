#!/usr/bin/env python3
"""Generate Computer Networks PDF for TCS NQT Preparation"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from utils.pdf_generator import TCSNQTPDFGenerator

def main():
    pdf = TCSNQTPDFGenerator(
        output_path=os.path.join(os.path.dirname(__file__), '..', '03-Core-CS-Subjects', 'PDFs', 'Computer-Networks.pdf'),
        title="Computer Networks",
        subject="TCS NQT - Core CS Subjects"
    )
    pdf.add_cover_page()

    # =========================================================================
    # SECTION 1: OSI & TCP/IP Models (12 Questions)
    # =========================================================================
    pdf.add_topic_header("Section 1: OSI & TCP/IP Models",
        "The OSI model has 7 layers while TCP/IP has 4 layers. Understanding each layer's role and protocols is fundamental.")
    q = 1

    pdf.add_question(q, "Which layer of the OSI model is responsible for end-to-end error recovery and flow control?",
        {'A': 'Network Layer', 'B': 'Data Link Layer', 'C': 'Transport Layer', 'D': 'Session Layer'},
        "C) Transport Layer",
        "The Transport Layer (Layer 4) provides end-to-end error recovery, flow control, and reliable data transfer using protocols like TCP.",
        "Easy"); q+=1

    pdf.add_question(q, "How many layers does the TCP/IP model have?",
        {'A': '4', 'B': '5', 'C': '6', 'D': '7'},
        "A) 4",
        "TCP/IP has 4 layers: Application, Transport, Internet, and Network Access (Link).",
        "Easy"); q+=1

    pdf.add_question(q, "Which OSI layer converts data into frames?",
        {'A': 'Physical Layer', 'B': 'Data Link Layer', 'C': 'Network Layer', 'D': 'Transport Layer'},
        "B) Data Link Layer",
        "The Data Link Layer (Layer 2) encapsulates packets into frames and handles MAC addressing.",
        "Easy"); q+=1

    pdf.add_question(q, "Which protocol operates at the OSI Presentation Layer?",
        {'A': 'HTTP', 'B': 'TCP', 'C': 'SSL/TLS', 'D': 'IP'},
        "C) SSL/TLS",
        "The Presentation Layer (Layer 6) handles data encryption, compression, and translation. SSL/TLS operates at this layer.",
        "Medium"); q+=1

    pdf.add_question(q, "The Session Layer (Layer 5) is responsible for:",
        {'A': 'Routing packets', 'B': 'Establishing, managing, and terminating sessions', 'C': 'Error detection in frames', 'D': 'Data encryption'},
        "B) Establishing, managing, and terminating sessions",
        "The Session Layer manages dialog control between applications, including establishing, maintaining, and terminating communication sessions.",
        "Easy"); q+=1

    pdf.add_question(q, "Which layer of TCP/IP model corresponds to the OSI Network Layer?",
        {'A': 'Application Layer', 'B': 'Transport Layer', 'C': 'Internet Layer', 'D': 'Network Access Layer'},
        "C) Internet Layer",
        "The Internet Layer in TCP/IP maps to the Network Layer in OSI. It handles logical addressing and routing using IP.",
        "Easy"); q+=1

    pdf.add_question(q, "Which device operates at OSI Layer 3?",
        {'A': 'Hub', 'B': 'Switch', 'C': 'Router', 'D': 'Repeater'},
        "C) Router",
        "Routers operate at Layer 3 (Network Layer) and make forwarding decisions based on IP addresses.",
        "Easy"); q+=1

    pdf.add_question(q, "In the OSI model, which layer is closest to the end user?",
        {'A': 'Application Layer', 'B': 'Presentation Layer', 'C': 'Session Layer', 'D': 'Transport Layer'},
        "A) Application Layer",
        "The Application Layer (Layer 7) is the topmost layer and interacts directly with user applications.",
        "Easy"); q+=1

    pdf.add_question(q, "Which PDU (Protocol Data Unit) is associated with the Transport Layer?",
        {'A': 'Bits', 'B': 'Frames', 'C': 'Packets', 'D': 'Segments'},
        "D) Segments",
        "Layer 1: Bits, Layer 2: Frames, Layer 3: Packets, Layer 4: Segments.",
        "Medium"); q+=1

    pdf.add_question(q, "Which protocol is NOT an Application Layer protocol?",
        {'A': 'FTP', 'B': 'SMTP', 'C': 'TCP', 'D': 'HTTP'},
        "C) TCP",
        "TCP is a Transport Layer protocol. FTP, SMTP, and HTTP are all Application Layer protocols.",
        "Easy"); q+=1

    pdf.add_question(q, "The OSI model was developed by:",
        {'A': 'IEEE', 'B': 'ISO', 'C': 'IETF', 'D': 'ANSI'},
        "B) ISO",
        "The OSI (Open Systems Interconnection) model was developed by the International Organization for Standardization (ISO).",
        "Easy"); q+=1

    pdf.add_question(q, "Which OSI layers are combined into the Application Layer of the TCP/IP model?",
        {'A': 'Layers 5, 6, 7', 'B': 'Layers 4, 5, 6', 'C': 'Layers 6, 7', 'D': 'Layers 1, 2'},
        "A) Layers 5, 6, 7",
        "The TCP/IP Application Layer combines the Session (5), Presentation (6), and Application (7) layers of the OSI model.",
        "Medium"); q+=1

    # =========================================================================
    # SECTION 2: IP Addressing & Subnetting (15 Questions)
    # =========================================================================
    pdf.add_page_break()
    pdf.add_topic_header("Section 2: IP Addressing & Subnetting",
        "IPv4 addressing, subnet masks, CIDR notation, and subnetting calculations are frequently tested topics.")

    pdf.add_question(q, "How many bits are in an IPv4 address?",
        {'A': '16', 'B': '32', 'C': '64', 'D': '128'},
        "B) 32",
        "IPv4 addresses are 32 bits long (4 octets of 8 bits each). IPv6 addresses are 128 bits.",
        "Easy"); q+=1

    pdf.add_question(q, "Which class of IP address has the default subnet mask 255.255.255.0?",
        {'A': 'Class A', 'B': 'Class B', 'C': 'Class C', 'D': 'Class D'},
        "C) Class C",
        "Class A: 255.0.0.0, Class B: 255.255.0.0, Class C: 255.255.255.0.",
        "Easy"); q+=1

    pdf.add_question(q, "The IP address 172.16.5.10 belongs to which class?",
        {'A': 'Class A', 'B': 'Class B', 'C': 'Class C', 'D': 'Class D'},
        "B) Class B",
        "Class B ranges from 128.0.0.0 to 191.255.255.255. 172.x.x.x falls in this range.",
        "Easy"); q+=1

    pdf.add_question(q, "What is the CIDR notation for subnet mask 255.255.240.0?",
        {'A': '/16', 'B': '/20', 'C': '/24', 'D': '/28'},
        "B) /20",
        "255.255.240.0 = 11111111.11111111.11110000.00000000, which has 20 one-bits, so it is /20.",
        "Medium"); q+=1

    pdf.add_question(q, "How many usable host addresses are available in a /26 subnet?",
        {'A': '30', 'B': '62', 'C': '64', 'D': '126'},
        "B) 62",
        "A /26 subnet has 2^6 = 64 addresses. Subtract 2 (network and broadcast) = 62 usable hosts.",
        "Medium"); q+=1

    pdf.add_question(q, "Which of the following is a private IP address range?",
        {'A': '10.0.0.0 - 10.255.255.255', 'B': '172.0.0.0 - 172.255.255.255', 'C': '192.0.0.0 - 192.255.255.255', 'D': '224.0.0.0 - 239.255.255.255'},
        "A) 10.0.0.0 - 10.255.255.255",
        "Private IP ranges: 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16. Option B is incorrect as it covers more than the private range.",
        "Medium"); q+=1

    pdf.add_question(q, "What is the broadcast address for the network 192.168.1.0/24?",
        {'A': '192.168.1.0', 'B': '192.168.1.1', 'C': '192.168.1.254', 'D': '192.168.1.255'},
        "D) 192.168.1.255",
        "For a /24 network, the broadcast address is the last address: all host bits set to 1 = 192.168.1.255.",
        "Easy"); q+=1

    pdf.add_question(q, "Given IP 192.168.10.65/28, what is the network address?",
        {'A': '192.168.10.0', 'B': '192.168.10.48', 'C': '192.168.10.64', 'D': '192.168.10.65'},
        "C) 192.168.10.64",
        "/28 means block size = 2^4 = 16. 65/16 = 4.06, so network starts at 4*16 = 64. Network address is 192.168.10.64.",
        "Medium"); q+=1

    pdf.add_question(q, "How many subnets can be created by borrowing 3 bits from the host portion?",
        {'A': '4', 'B': '6', 'C': '8', 'D': '16'},
        "C) 8",
        "Number of subnets = 2^n where n is borrowed bits. 2^3 = 8 subnets.",
        "Medium"); q+=1

    pdf.add_question(q, "Which IP address is a loopback address?",
        {'A': '192.168.1.1', 'B': '127.0.0.1', 'C': '10.0.0.1', 'D': '0.0.0.0'},
        "B) 127.0.0.1",
        "The entire 127.0.0.0/8 range is reserved for loopback. 127.0.0.1 is the most commonly used loopback address.",
        "Easy"); q+=1

    pdf.add_question(q, "What is the maximum number of hosts in a Class A network?",
        {'A': '254', 'B': '65,534', 'C': '16,777,214', 'D': '16,777,216'},
        "C) 16,777,214",
        "Class A has 24 host bits. 2^24 - 2 = 16,777,214 usable hosts.",
        "Medium"); q+=1

    pdf.add_question(q, "The address 169.254.x.x is used for:",
        {'A': 'Multicasting', 'B': 'APIPA (Automatic Private IP Addressing)', 'C': 'Loopback', 'D': 'Broadcasting'},
        "B) APIPA (Automatic Private IP Addressing)",
        "When DHCP fails, devices self-assign an address from 169.254.0.0/16 (APIPA range).",
        "Medium"); q+=1

    pdf.add_question(q, "In IPv6, how many bits is an address?",
        {'A': '32', 'B': '64', 'C': '96', 'D': '128'},
        "D) 128",
        "IPv6 addresses are 128 bits long, written as 8 groups of 4 hexadecimal digits.",
        "Easy"); q+=1

    pdf.add_question(q, "A company needs 500 host addresses. What is the minimum subnet mask?",
        {'A': '/22', 'B': '/23', 'C': '/24', 'D': '/25'},
        "B) /23",
        "/23 gives 2^9 - 2 = 510 usable hosts. /24 gives only 254, which is insufficient.",
        "Hard"); q+=1

    pdf.add_question(q, "What is the subnet mask for a /20 network?",
        {'A': '255.255.240.0', 'B': '255.255.248.0', 'C': '255.255.224.0', 'D': '255.255.192.0'},
        "A) 255.255.240.0",
        "/20 = 20 ones: 11111111.11111111.11110000.00000000 = 255.255.240.0.",
        "Medium"); q+=1

    # =========================================================================
    # SECTION 3: Transport Layer (10 Questions)
    # =========================================================================
    pdf.add_page_break()
    pdf.add_topic_header("Section 3: Transport Layer",
        "TCP and UDP are the key transport layer protocols. Understand their differences, handshakes, and control mechanisms.")

    pdf.add_question(q, "Which protocol provides reliable, connection-oriented communication?",
        {'A': 'UDP', 'B': 'TCP', 'C': 'IP', 'D': 'ICMP'},
        "B) TCP",
        "TCP (Transmission Control Protocol) is connection-oriented and provides reliable delivery with acknowledgments.",
        "Easy"); q+=1

    pdf.add_question(q, "How many steps are in a TCP connection establishment (handshake)?",
        {'A': '2', 'B': '3', 'C': '4', 'D': '5'},
        "B) 3",
        "TCP uses a 3-way handshake: SYN, SYN-ACK, ACK to establish a connection.",
        "Easy"); q+=1

    pdf.add_question(q, "TCP connection termination uses how many steps?",
        {'A': '2', 'B': '3', 'C': '4', 'D': '5'},
        "C) 4",
        "TCP uses a 4-way handshake for termination: FIN, ACK, FIN, ACK.",
        "Medium"); q+=1

    pdf.add_question(q, "Which of the following is NOT a feature of UDP?",
        {'A': 'Connectionless', 'B': 'Low overhead', 'C': 'Guaranteed delivery', 'D': 'Fast transmission'},
        "C) Guaranteed delivery",
        "UDP does not guarantee delivery. It is connectionless, low overhead, and fast but unreliable.",
        "Easy"); q+=1

    pdf.add_question(q, "Which port number is used by HTTP?",
        {'A': '21', 'B': '25', 'C': '80', 'D': '443'},
        "C) 80",
        "HTTP uses port 80. HTTPS uses 443, FTP uses 21, SMTP uses 25.",
        "Easy"); q+=1

    pdf.add_question(q, "Which TCP congestion control algorithm uses additive increase and multiplicative decrease?",
        {'A': 'Slow Start', 'B': 'AIMD (Congestion Avoidance)', 'C': 'Fast Retransmit', 'D': 'Fast Recovery'},
        "B) AIMD (Congestion Avoidance)",
        "AIMD increases the congestion window by 1 MSS per RTT (additive) and halves it on congestion (multiplicative decrease).",
        "Hard"); q+=1

    pdf.add_question(q, "The well-known port numbers range from:",
        {'A': '0-255', 'B': '0-1023', 'C': '0-65535', 'D': '1024-49151'},
        "B) 0-1023",
        "Well-known ports: 0-1023, Registered ports: 1024-49151, Dynamic/Private: 49152-65535.",
        "Medium"); q+=1

    pdf.add_question(q, "Which protocol is preferred for real-time video streaming?",
        {'A': 'TCP', 'B': 'UDP', 'C': 'SCTP', 'D': 'DCCP'},
        "B) UDP",
        "UDP is preferred for real-time applications like video streaming because low latency is more important than reliability.",
        "Easy"); q+=1

    pdf.add_question(q, "In TCP, what is the purpose of the window size field?",
        {'A': 'Error detection', 'B': 'Flow control', 'C': 'Routing', 'D': 'Encryption'},
        "B) Flow control",
        "The window size field in TCP header is used for flow control, telling the sender how much data the receiver can accept.",
        "Medium"); q+=1

    pdf.add_question(q, "What happens during TCP Slow Start?",
        {'A': 'Congestion window increases linearly', 'B': 'Congestion window increases exponentially', 'C': 'Congestion window decreases', 'D': 'Congestion window stays constant'},
        "B) Congestion window increases exponentially",
        "In Slow Start, the congestion window doubles every RTT (exponential growth) until it reaches the threshold.",
        "Hard"); q+=1

    # =========================================================================
    # SECTION 4: Network Layer (10 Questions)
    # =========================================================================
    pdf.add_page_break()
    pdf.add_topic_header("Section 4: Network Layer",
        "The Network Layer handles routing, logical addressing, and path determination using protocols like RIP, OSPF, and BGP.")

    pdf.add_question(q, "Which routing protocol uses hop count as its metric?",
        {'A': 'OSPF', 'B': 'BGP', 'C': 'RIP', 'D': 'EIGRP'},
        "C) RIP",
        "RIP (Routing Information Protocol) uses hop count with a maximum of 15 hops.",
        "Easy"); q+=1

    pdf.add_question(q, "OSPF is based on which algorithm?",
        {'A': 'Bellman-Ford', 'B': 'Dijkstra', 'C': 'Floyd-Warshall', 'D': 'Prim'},
        "B) Dijkstra",
        "OSPF (Open Shortest Path First) uses Dijkstra's shortest path algorithm. RIP uses Bellman-Ford.",
        "Medium"); q+=1

    pdf.add_question(q, "Which protocol is used to find the MAC address from an IP address?",
        {'A': 'RARP', 'B': 'ARP', 'C': 'ICMP', 'D': 'IGMP'},
        "B) ARP",
        "ARP (Address Resolution Protocol) maps IP addresses to MAC addresses. RARP does the reverse.",
        "Easy"); q+=1

    pdf.add_question(q, "BGP is classified as which type of routing protocol?",
        {'A': 'Interior Gateway Protocol', 'B': 'Exterior Gateway Protocol', 'C': 'Link State Protocol', 'D': 'Distance Vector Protocol'},
        "B) Exterior Gateway Protocol",
        "BGP (Border Gateway Protocol) is an Exterior Gateway Protocol used for routing between autonomous systems on the Internet.",
        "Medium"); q+=1

    pdf.add_question(q, "ICMP is primarily used for:",
        {'A': 'Data transfer', 'B': 'Error reporting and diagnostics', 'C': 'Routing', 'D': 'Address resolution'},
        "B) Error reporting and diagnostics",
        "ICMP (Internet Control Message Protocol) is used for error reporting (e.g., Destination Unreachable) and diagnostics (e.g., ping, traceroute).",
        "Easy"); q+=1

    pdf.add_question(q, "Which field in the IP header prevents packets from looping forever?",
        {'A': 'Checksum', 'B': 'TTL (Time to Live)', 'C': 'Protocol', 'D': 'Fragmentation Offset'},
        "B) TTL (Time to Live)",
        "TTL is decremented by 1 at each router. When it reaches 0, the packet is discarded, preventing infinite loops.",
        "Easy"); q+=1

    pdf.add_question(q, "What is the maximum hop count in RIP?",
        {'A': '10', 'B': '15', 'C': '16', 'D': '255'},
        "B) 15",
        "RIP has a maximum hop count of 15. A hop count of 16 means the destination is unreachable.",
        "Medium"); q+=1

    pdf.add_question(q, "NAT stands for:",
        {'A': 'Network Address Translation', 'B': 'Network Access Termination', 'C': 'Node Address Transfer', 'D': 'Network Allocation Table'},
        "A) Network Address Translation",
        "NAT translates private IP addresses to public IP addresses, allowing multiple devices to share a single public IP.",
        "Easy"); q+=1

    pdf.add_question(q, "Which type of routing is performed when routers exchange information dynamically?",
        {'A': 'Static routing', 'B': 'Default routing', 'C': 'Dynamic routing', 'D': 'Source routing'},
        "C) Dynamic routing",
        "Dynamic routing uses protocols (RIP, OSPF, BGP) to automatically discover and maintain routes.",
        "Easy"); q+=1

    pdf.add_question(q, "OSPF divides a network into:",
        {'A': 'Subnets', 'B': 'Areas', 'C': 'Domains', 'D': 'Zones'},
        "B) Areas",
        "OSPF uses areas to create a hierarchical routing structure. Area 0 is the backbone area.",
        "Medium"); q+=1

    # =========================================================================
    # SECTION 5: Data Link Layer (8 Questions)
    # =========================================================================
    pdf.add_page_break()
    pdf.add_topic_header("Section 5: Data Link Layer",
        "The Data Link Layer handles MAC addressing, framing, error detection (CRC, Hamming), switches, and VLANs.")

    pdf.add_question(q, "A MAC address is how many bits long?",
        {'A': '32', 'B': '48', 'C': '64', 'D': '128'},
        "B) 48",
        "MAC (Media Access Control) addresses are 48 bits (6 bytes), typically written as six pairs of hex digits.",
        "Easy"); q+=1

    pdf.add_question(q, "Which error detection method uses polynomial division?",
        {'A': 'Parity Check', 'B': 'Checksum', 'C': 'CRC', 'D': 'Hamming Code'},
        "C) CRC",
        "CRC (Cyclic Redundancy Check) uses polynomial division to detect errors. It is widely used in Ethernet.",
        "Medium"); q+=1

    pdf.add_question(q, "Hamming code can detect up to how many bit errors?",
        {'A': '1', 'B': '2', 'C': '3', 'D': '4'},
        "B) 2",
        "Hamming code can detect up to 2-bit errors and correct 1-bit errors.",
        "Medium"); q+=1

    pdf.add_question(q, "A switch operates at which OSI layer?",
        {'A': 'Layer 1', 'B': 'Layer 2', 'C': 'Layer 3', 'D': 'Layer 4'},
        "B) Layer 2",
        "Switches operate at Layer 2 (Data Link Layer) and forward frames based on MAC addresses.",
        "Easy"); q+=1

    pdf.add_question(q, "VLAN stands for:",
        {'A': 'Virtual Local Area Network', 'B': 'Very Large Area Network', 'C': 'Virtual Link Access Network', 'D': 'Variable Length Address Network'},
        "A) Virtual Local Area Network",
        "VLANs logically segment a physical network into separate broadcast domains for better management and security.",
        "Easy"); q+=1

    pdf.add_question(q, "Which protocol is used for VLAN tagging?",
        {'A': 'IEEE 802.3', 'B': 'IEEE 802.1Q', 'C': 'IEEE 802.11', 'D': 'IEEE 802.1X'},
        "B) IEEE 802.1Q",
        "IEEE 802.1Q adds a 4-byte VLAN tag to Ethernet frames for VLAN identification.",
        "Medium"); q+=1

    pdf.add_question(q, "What is the minimum number of redundant bits needed for Hamming code to correct single-bit errors in a 4-bit data word?",
        {'A': '2', 'B': '3', 'C': '4', 'D': '5'},
        "B) 3",
        "Using the formula 2^r >= m + r + 1, where m=4: 2^3 = 8 >= 4+3+1 = 8. So r = 3 redundant bits.",
        "Hard"); q+=1

    pdf.add_question(q, "ARP maps:",
        {'A': 'MAC address to IP address', 'B': 'IP address to MAC address', 'C': 'Domain name to IP address', 'D': 'Port number to IP address'},
        "B) IP address to MAC address",
        "ARP (Address Resolution Protocol) resolves a known IP address to a MAC address on the local network.",
        "Easy"); q+=1

    # =========================================================================
    # SECTION 6: Application Layer (10 Questions)
    # =========================================================================
    pdf.add_page_break()
    pdf.add_topic_header("Section 6: Application Layer",
        "Application layer protocols like HTTP, DNS, DHCP, FTP, and SMTP are essential for TCS NQT.")

    pdf.add_question(q, "DNS resolves:",
        {'A': 'IP to MAC address', 'B': 'Domain name to IP address', 'C': 'MAC to IP address', 'D': 'Port to IP address'},
        "B) Domain name to IP address",
        "DNS (Domain Name System) translates human-readable domain names (e.g., google.com) to IP addresses.",
        "Easy"); q+=1

    pdf.add_question(q, "Which port does DNS use?",
        {'A': '23', 'B': '53', 'C': '80', 'D': '443'},
        "B) 53",
        "DNS uses port 53 for both TCP and UDP. UDP is used for queries, TCP for zone transfers.",
        "Medium"); q+=1

    pdf.add_question(q, "DHCP is used to:",
        {'A': 'Resolve domain names', 'B': 'Automatically assign IP addresses', 'C': 'Transfer files', 'D': 'Send emails'},
        "B) Automatically assign IP addresses",
        "DHCP (Dynamic Host Configuration Protocol) automatically assigns IP addresses, subnet masks, gateways, and DNS servers.",
        "Easy"); q+=1

    pdf.add_question(q, "FTP uses which port(s)?",
        {'A': 'Port 20 only', 'B': 'Port 21 only', 'C': 'Ports 20 and 21', 'D': 'Port 22'},
        "C) Ports 20 and 21",
        "FTP uses port 21 for control (commands) and port 20 for data transfer.",
        "Medium"); q+=1

    pdf.add_question(q, "SMTP is used for:",
        {'A': 'Receiving emails', 'B': 'Sending emails', 'C': 'Browsing the web', 'D': 'File transfer'},
        "B) Sending emails",
        "SMTP (Simple Mail Transfer Protocol) is used for sending emails. POP3/IMAP are used for receiving.",
        "Easy"); q+=1

    pdf.add_question(q, "HTTPS uses which port by default?",
        {'A': '80', 'B': '143', 'C': '443', 'D': '8080'},
        "C) 443",
        "HTTPS (HTTP Secure) uses port 443. HTTP uses port 80.",
        "Easy"); q+=1

    pdf.add_question(q, "Which HTTP method is used to retrieve data from a server?",
        {'A': 'POST', 'B': 'GET', 'C': 'PUT', 'D': 'DELETE'},
        "B) GET",
        "GET retrieves data, POST submits data, PUT updates data, DELETE removes data.",
        "Easy"); q+=1

    pdf.add_question(q, "Which protocol retrieves emails from a mail server and downloads them to the client?",
        {'A': 'SMTP', 'B': 'POP3', 'C': 'HTTP', 'D': 'FTP'},
        "B) POP3",
        "POP3 (Post Office Protocol v3) downloads emails from the server to the client. IMAP keeps emails on the server.",
        "Medium"); q+=1

    pdf.add_question(q, "The DHCP process follows which sequence?",
        {'A': 'Discover, Offer, Request, Acknowledge', 'B': 'Request, Offer, Discover, Acknowledge', 'C': 'Offer, Discover, Request, Acknowledge', 'D': 'Discover, Request, Offer, Acknowledge'},
        "A) Discover, Offer, Request, Acknowledge",
        "DHCP uses DORA: Discover (client), Offer (server), Request (client), Acknowledge (server).",
        "Medium"); q+=1

    pdf.add_question(q, "Telnet uses which port?",
        {'A': '21', 'B': '22', 'C': '23', 'D': '25'},
        "C) 23",
        "Telnet uses port 23. SSH (secure alternative) uses port 22.",
        "Medium"); q+=1

    # =========================================================================
    # SECTION 7: Network Security (8 Questions)
    # =========================================================================
    pdf.add_page_break()
    pdf.add_topic_header("Section 7: Network Security",
        "Encryption, firewalls, SSL/TLS, and common attack types are important for TCS NQT.")

    pdf.add_question(q, "Which type of encryption uses a single key for both encryption and decryption?",
        {'A': 'Asymmetric encryption', 'B': 'Symmetric encryption', 'C': 'Hashing', 'D': 'Digital signature'},
        "B) Symmetric encryption",
        "Symmetric encryption (e.g., AES, DES) uses the same key for encryption and decryption. It is faster but requires secure key exchange.",
        "Easy"); q+=1

    pdf.add_question(q, "RSA is an example of:",
        {'A': 'Symmetric encryption', 'B': 'Asymmetric encryption', 'C': 'Hash function', 'D': 'Firewall'},
        "B) Asymmetric encryption",
        "RSA uses a public-private key pair. The public key encrypts, and the private key decrypts.",
        "Easy"); q+=1

    pdf.add_question(q, "A firewall operates at which OSI layer(s)?",
        {'A': 'Only Layer 3', 'B': 'Only Layer 7', 'C': 'Layers 3-7 (depending on type)', 'D': 'Only Layer 2'},
        "C) Layers 3-7 (depending on type)",
        "Packet-filtering firewalls work at Layer 3-4, while application firewalls work at Layer 7.",
        "Medium"); q+=1

    pdf.add_question(q, "SSL/TLS provides:",
        {'A': 'Only encryption', 'B': 'Only authentication', 'C': 'Encryption, authentication, and data integrity', 'D': 'Only data integrity'},
        "C) Encryption, authentication, and data integrity",
        "SSL/TLS provides all three: encryption (confidentiality), authentication (certificates), and data integrity (MAC).",
        "Medium"); q+=1

    pdf.add_question(q, "Which attack involves intercepting communication between two parties?",
        {'A': 'DDoS', 'B': 'Man-in-the-Middle', 'C': 'Phishing', 'D': 'SQL Injection'},
        "B) Man-in-the-Middle",
        "A Man-in-the-Middle (MITM) attack intercepts communication between two parties, potentially altering the data.",
        "Easy"); q+=1

    pdf.add_question(q, "DES uses a key of how many bits?",
        {'A': '32', 'B': '56', 'C': '128', 'D': '256'},
        "B) 56",
        "DES (Data Encryption Standard) uses a 56-bit key. AES uses 128, 192, or 256-bit keys.",
        "Medium"); q+=1

    pdf.add_question(q, "A digital certificate is issued by:",
        {'A': 'ISP', 'B': 'Certificate Authority (CA)', 'C': 'DNS Server', 'D': 'Firewall'},
        "B) Certificate Authority (CA)",
        "A CA issues digital certificates that verify the identity of websites and organizations.",
        "Easy"); q+=1

    pdf.add_question(q, "Which protocol provides secure remote login?",
        {'A': 'Telnet', 'B': 'FTP', 'C': 'SSH', 'D': 'HTTP'},
        "C) SSH",
        "SSH (Secure Shell) provides encrypted remote login on port 22. Telnet is unencrypted.",
        "Easy"); q+=1

    # =========================================================================
    # SECTION 8: Numerical Problems (8 Questions)
    # =========================================================================
    pdf.add_page_break()
    pdf.add_topic_header("Section 8: Numerical Problems",
        "Bandwidth, propagation delay, throughput, and subnetting calculation problems commonly appear in TCS NQT.")

    pdf.add_question(q, "A network has a bandwidth of 10 Mbps and a propagation delay of 20 ms. What is the bandwidth-delay product?",
        {'A': '100,000 bits', 'B': '200,000 bits', 'C': '2,000,000 bits', 'D': '20,000 bits'},
        "B) 200,000 bits",
        "Bandwidth-delay product = Bandwidth x Propagation delay = 10 x 10^6 x 20 x 10^-3 = 200,000 bits.",
        "Medium"); q+=1

    pdf.add_question(q, "A packet of 1000 bytes is sent over a link with bandwidth 1 Mbps. What is the transmission delay?",
        {'A': '1 ms', 'B': '8 ms', 'C': '10 ms', 'D': '80 ms'},
        "B) 8 ms",
        "Transmission delay = Packet size / Bandwidth = (1000 x 8 bits) / (1 x 10^6 bps) = 8 x 10^-3 s = 8 ms.",
        "Medium"); q+=1

    pdf.add_question(q, "If a channel has a bandwidth of 3000 Hz and SNR of 31 dB, what is the maximum data rate (Shannon)?",
        {'A': '10,000 bps', 'B': '20,000 bps', 'C': '30,000 bps', 'D': '60,000 bps'},
        "C) 30,000 bps",
        "Shannon capacity = B x log2(1 + SNR). SNR in ratio = 10^(31/10) ~ 1000. C = 3000 x log2(1001) ~ 3000 x 10 = 30,000 bps.",
        "Hard"); q+=1

    pdf.add_question(q, "A network 200.1.0.0/24 is divided into 4 equal subnets. How many hosts per subnet?",
        {'A': '30', 'B': '62', 'C': '64', 'D': '126'},
        "B) 62",
        "4 subnets need 2 extra bits: /26. Hosts per subnet = 2^6 - 2 = 62.",
        "Medium"); q+=1

    pdf.add_question(q, "What is the propagation delay for a 2000 km link with a propagation speed of 2 x 10^8 m/s?",
        {'A': '1 ms', 'B': '10 ms', 'C': '100 ms', 'D': '1 s'},
        "B) 10 ms",
        "Propagation delay = Distance / Speed = 2,000,000 / (2 x 10^8) = 0.01 s = 10 ms.",
        "Medium"); q+=1

    pdf.add_question(q, "Using Nyquist theorem, a noiseless channel with bandwidth 4000 Hz using 4 signal levels has max data rate of:",
        {'A': '8000 bps', 'B': '16,000 bps', 'C': '32,000 bps', 'D': '64,000 bps'},
        "B) 16,000 bps",
        "Nyquist rate = 2 x B x log2(L) = 2 x 4000 x log2(4) = 2 x 4000 x 2 = 16,000 bps.",
        "Hard"); q+=1

    pdf.add_question(q, "In a sliding window protocol, if the window size is 7, how many frames can be sent before receiving an ACK?",
        {'A': '6', 'B': '7', 'C': '8', 'D': '14'},
        "B) 7",
        "The window size determines the maximum number of unacknowledged frames that can be in transit. Window size 7 means 7 frames.",
        "Medium"); q+=1

    pdf.add_question(q, "A router receives a packet with TTL=1. What does the router do?",
        {'A': 'Forward the packet', 'B': 'Discard and send ICMP Time Exceeded', 'C': 'Store the packet', 'D': 'Broadcast the packet'},
        "B) Discard and send ICMP Time Exceeded",
        "When TTL reaches 0 after decrement, the router discards the packet and sends an ICMP Time Exceeded message to the source.",
        "Medium"); q+=1

    pdf.generate()
    print(f"Total questions: {q - 1}")

if __name__ == '__main__':
    main()
