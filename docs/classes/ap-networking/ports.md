# Ports and Protocols

## 1. Project Overview  

**Problem Statement:**  
Understand how Layer 2 and Layer 3 communication functions inside a LAN and how packets move across routers and networks.

**Objectives:**  

- Analyze Layer 3 identity using IP addressing and default gateways  
- Simulate internal and external traffic between virtual machines on the same and different networks and subnets  
- Examine how traffic exits a subnet through a default gateway  
- Use traceroute to analyze packet paths and hop-by-hop routing behavior  

**Success Criteria:**  

- Correctly identify IPv4 addresses, subnet masks, and default gateways on multiple devices  
- Successfully demonstrate transporting of packets between devices
- Accurately interpret traceroute output
- Explain how routing tables enables communication within a network

## 2. Design & Planning 

Before performing any technical experiments, it is important to understand the basic information and concepts required for Layer 3 communication. 

### IP Addressing

Each device in the network must have a unique IP address.

- **IPv4 Address** identifies the device on a network
- Devices on the **same subnet** can communicate directly without using a router  
- Devices on **different subnets** require a **default gateway** to forward traffic

### Private vs Public IP Addresses

- **Private IPs** are used inside the LAN for internal communication and are not globally routable.  
- **Public IPs** are used to communicate with devices outside the local network.  
- **NAT** (Network Address Translation) allows multiple devices with private IPs to share a single public IP when accessing the internet.

### MAC Addresses

- Every network interface has a unique **MAC address** used for local delivery of frames.  
- **ARP** (Address Resolution Protocol) maps IP addresses to MAC addresses on the local subnet.  
- Before a packet is sent, a device broadcasts an ARP request to find the MAC of the destination.  
- MAC addresses change at each hop (like PC to router), while the IP address remains constant from source to destination.

### Default Gateway and Routing Tables

- The **default gateway** is the router interface that forwards traffic from the private network to external networks.  
- A **routing table** is used by each device to determine where to send a packet based on its destination IP
- **Traceroute** is a tool that tracks the path packets take from the source to a destination.  


## 3. Technical Development 

### Transport Layer Reliability

**PC1 and PC2 IP Configuration:**

<img width="1906" height="957" alt="Screenshot 2026-03-03 at 1 22 26 PM" src="https://github.com/user-attachments/assets/26625a34-9107-4c0c-a70d-7bbfabf25ed2" />

<img width="1914" height="949" alt="Screenshot 2026-03-03 at 1 22 53 PM" src="https://github.com/user-attachments/assets/01e3769e-f0cc-4960-868e-0b654434b96a" />

The internet layer is responsible for the ping command, as it handles logical addressing and routing. Ping does not use TCP or UDP; instead, it uses the ICMP (Internet Control Message Protocol), which is a separate protocol within the IP suite. Consequently, a successful ping does not prove TCP reliability, as ICMP is a connectionless protocol that operates independently of the handshake and error-recovery mechanisms found in TCP

**PC1 ping PC2 Successful:**

<img width="299" height="225" alt="Screenshot 2026-03-03 at 1 27 56 PM" src="https://github.com/user-attachments/assets/6e1da7c8-b90f-46c7-93fa-0828825390d4" />

**PC1 to PC2 PDU Path:**

https://github.com/user-attachments/assets/0eca56c9-9a46-4b82-99e7-0942a2639ccb

| Feature | TCP | UDP | 
|---|---|---|
| Connection Setup | Yes, involves a 3 way handshake | No, it is connectionless |
| Sequence Numbers | Yes, used to reassemble data in the correct order | No, packets are treated individually |
| Acknowledgment | Yes, the receiver confirms receipt of data segments. | No, the sender never knows if data arrived | 
| Retransmission | Yes, missing segments are resent automatically | No, lost data is simply lost | 
| Header Complexity | Contains many control fields | Contains only essential info | 

### Comparing Transmission Types

**View Listening TCP Ports(ss -tln):**

<img width="1842" height="344" alt="Image 3-6-26 at 8 19 AM" src="https://github.com/user-attachments/assets/dbd8b48d-846c-401a-82dc-a05e4608e7a8" />

**Sudo ss -tlpn screenshot:**

<img width="1892" height="306" alt="Image 3-6-26 at 8 20 AM" src="https://github.com/user-attachments/assets/66ecc646-92b1-4c5b-9bd7-c18c2a50a4b1" />

**View Listening UDP Ports (ss -uln):**

<img width="1880" height="322" alt="Image 3-6-26 at 8 22 AM" src="https://github.com/user-attachments/assets/636dc39e-2323-43e8-8a12-2e1c28d052c6" />

**Terminal A Listener screenshot:**

Use the command `nc -l 5000` to have Terminal A be silently listening.

<img width="944" height="60" alt="Image 3-6-26 at 8 27 AM" src="https://github.com/user-attachments/assets/422681ee-5196-4ae3-b66b-4ff794e222b5" />

**Terminal C Shows New Port from Terminal A:**

The new port 0.0.0.0:5000 shows that Terminal C can now see the port from Terminal A.

<img width="1442" height="416" alt="Image 3-6-26 at 8 29 AM" src="https://github.com/user-attachments/assets/59a02792-166e-4f4d-a661-10ed24743b8e" />

**Successful Communication between Terminal B and A(tcp):**

Message from Terminal B:
<img width="666" height="88" alt="Image 3-6-26 at 8 32 AM" src="https://github.com/user-attachments/assets/be9c0b09-c04f-4e5c-b897-15dcffb77109" />

Terminal A Receieves Message:

<img width="524" height="80" alt="Image 3-6-26 at 8 32 AM (1)" src="https://github.com/user-attachments/assets/3e7ebd4c-43eb-40cd-8cb4-f4947504860c" />

**Observe ESTAB state from Terminal C:**

<img width="1428" height="206" alt="Image 3-6-26 at 8 34 AM" src="https://github.com/user-attachments/assets/c126aaa6-e3e4-42e8-8f76-3d860df6509f" />

**Start UDP Listener Terminal A:**

<img width="694" height="70" alt="Image 3-6-26 at 8 35 AM" src="https://github.com/user-attachments/assets/918b2ed0-21c0-4356-a5c1-c73cc28c7f25" />

**Successful Communication between Terminal B and A(udp):**

Message from Terminal B:
<img width="752" height="102" alt="Image 3-6-26 at 8 36 AM" src="https://github.com/user-attachments/assets/83a90265-2a04-4b08-bb0a-83605647247d" />

Terminal A Recieves Message:

<img width="618" height="94" alt="Image 3-6-26 at 8 37 AM" src="https://github.com/user-attachments/assets/b632a039-27be-40bf-976f-b19232351739" />

**Observe UDP State from Terminal C:**

<img width="1428" height="332" alt="Image 3-6-26 at 8 38 AM" src="https://github.com/user-attachments/assets/3427efd8-2ced-455b-9a37-4eebd72ebdd1" />

### OSI Layer 5

**HTTP Transaction:**

<img width="858" height="480" alt="Image 3-9-26 at 9 04 AM" src="https://github.com/user-attachments/assets/16e4115b-2f3d-40e2-a824-cc1e512c82bb" />

**HTTPS Transaction:**

<img width="940" height="454" alt="Image 3-9-26 at 9 06 AM" src="https://github.com/user-attachments/assets/c04ccf11-1b94-4314-8f77-c63f9b37318b" />

**TLS Handshake:**

<img width="1012" height="452" alt="Screenshot 2026-03-09 at 9 18 03 AM" src="https://github.com/user-attachments/assets/1483d332-1b4e-407e-aa83-da6fda133c59" />

<img width="782" height="815" alt="Screenshot 2026-03-09 at 9 18 16 AM" src="https://github.com/user-attachments/assets/422df5f8-8a35-4876-b171-dbd64f03feb2" />

**Observe Persistent Connection:**

<img width="2044" height="376" alt="Image 3-9-26 at 9 31 AM" src="https://github.com/user-attachments/assets/4e824aee-aafe-4e53-97a8-2b94de61e4a2" />

### Application and Remote Access Protocols Across the Stack

**HTTP Stack Screenshot:**

<img width="727" height="148" alt="Screenshot 2026-03-11 at 12 43 37 PM" src="https://github.com/user-attachments/assets/db8d8aed-5c57-4cf8-8b7d-af1ac7c80985" />

**HTTPS Stack Screenshot:**

<img width="740" height="115" alt="Screenshot 2026-03-11 at 12 44 32 PM" src="https://github.com/user-attachments/assets/00195c9a-4879-45ea-88c5-9cc2926ddeb3" />

**nslookup Screenshot:**

<img width="388" height="253" alt="Screenshot 2026-03-11 at 12 48 16 PM" src="https://github.com/user-attachments/assets/0263f9e1-05c7-4018-80d1-c090ae4e50c1" />

**Connect via SSH Screenshot:**

<img width="908" height="524" alt="Screenshot 2026-03-11 at 12 49 49 PM" src="https://github.com/user-attachments/assets/4b947a22-29a2-46da-8b31-48e42bea23da" />

**SSH Connection ss -tn Screenshot:**

<img width="731" height="264" alt="Screenshot 2026-03-11 at 12 52 06 PM" src="https://github.com/user-attachments/assets/08bc1213-d9c4-41e5-bcab-05c25bc3a050" />

**Secure File Transer Screenshot:**

<img width="654" height="98" alt="Screenshot 2026-03-11 at 12 53 25 PM" src="https://github.com/user-attachments/assets/0cf0c5ab-234f-43e8-a368-01f611fa12b9" />

### Understanding HTTP Status Codes

| Status Code Range | Meaning | Example Code | Explanation |
|---|---|---|---|
| 1xx | Informational responses that indicate the request has been received and the server is continuing the process. | 100 Continue | This code means the server has received the initial part of the request and the client can continue sending the rest of it. |
| 2xx | Successful responses that indicate the request was received, understood, and processed correctly. | 200 OK | This code means the request was successful and the server returned the requested resource or response. |
| 3xx | Redirection messages that tell the client that the resource has moved or another action must be taken to complete the request. | 301 Moved Permanently | This code means the requested resource has been permanently moved to a new URL, and the client should update future requests to use that new address. |
| 4xx | Client error responses that indicate something was wrong with the request sent by the client. | 404 Not Found | This code means the server could not find the requested resource, usually because the URL is incorrect or the page no longer exists. |
| 5xx | Server error responses that indicate the server failed to fulfill a valid request. | 500 Internal Server Error | This code means the server encountered an unexpected problem that prevented it from completing the request. |

| Status Code | Name | What It Means | When It Happens |
|---|---|---|---|
| 200 | OK | The request was successful and the server returned the requested content. | Happens when a webpage loads correctly and the server delivers the page or data without errors. |
| 301 | Moved Permanently | The requested resource has been permanently moved to a different URL. | Happens when a website changes its address and automatically redirects users to the new location. |
| 302 | Found | The resource is temporarily located at a different URL. | Happens when a page temporarily redirects users, such as during maintenance or temporary content changes. |
| 404 | Not Found | The server cannot find the requested resource. | Happens when a user tries to access a page that does not exist or the URL was typed incorrectly. |
| 500 | Internal Server Error | The server encountered an unexpected condition that prevented it from completing the request. | Happens when there is a bug, misconfiguration, or failure in the server's software. |

HTTP status codes are handled at the application layer because they describe the result of a web request between a client and a web server. The application layer is responsible for protocols like HTTP that define how web browsers and servers communicate and interpret messages. In contrast, the transport layer is only responsible for reliably delivering data between devices, not interpreting what the data means. Because status codes describe the meaning and outcome of a request, they belong in the application layer where the communication rules of web applications are defined.

## 4. Testing & Evaluation 

| Concept | Test Performed | Verification Result |
|-------|---------------|---------------------|
| Direct Delivery | Pinged another VM on the same network/subnet | Verified that traffic was delivered directly without using the default gateway |
| Routed Traffic via Default Gateway | Pinged external IP (8.8.8.8) and google.com from Ubuntu VM | Confirmed packets were forwarded first to default gateway and multiple hops seen in traceroute including internal private IPs followed by public IPs |
| Private vs Public IP Communication | Pinged partner private IP and public IP | Private IP succeeded, indicating direct LAN communication. Public IP failed due to firewall/NAT restrictions, confirming isolation of private networks |
| Routing Table Function | Checked `ip route` and router configuration | Verified correct next hop decisions based on destination IP |
| Traceroute | Ran traceroute to determine path taken | List of paths, default gateway with many hops for external networks and a single hope for internal pings |
| TTL Experiment | Limited traceroute to 3 hops for external IP | Verified that TTL successfully restricted the traceroute path and showed only the first 3 hops |

## 5. Reflection  

This project helped me understand how Layer 3 communication functions within a LAN and across routers. By configuring multiple virtual machines and observing traffic between them, I saw firsthand how devices on the same network communicate directly using MAC addresses while devices on different networks rely on a default gateway to forward packets. The experiments with traceroute allowed me to see the hops when trying to reach external vs interal networks..

Working with private and public IPs reinforced the importance of network addressing and NAT. I learned that private IPs allow unrestricted internal communication, while public IPs are filtered, providing security to private networks. Observing the failure of packets to reach external devices without a router highlighted the critical role of routers in connecting private networks to other servers. This project also emphasized how ARP and MAC addresses are crucial in local navigation.

Overall, this project strengthened my understanding of packet movement, routing, and network design. It demonstrated the practical connections between IP configuration, routing tables, default gateways, and network visibility. By seeing the actual flow of packets, I gained a deeper understanding for how network controls combined with careful addressing and routing creates functional and secure networks.
