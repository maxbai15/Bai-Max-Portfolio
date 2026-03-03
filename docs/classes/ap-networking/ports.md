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

**PC1 ping PC2 Successful:**

<img width="299" height="225" alt="Screenshot 2026-03-03 at 1 27 56 PM" src="https://github.com/user-attachments/assets/6e1da7c8-b90f-46c7-93fa-0828825390d4" />

**PC1 to PC2 PDU Path:**

https://github.com/user-attachments/assets/0eca56c9-9a46-4b82-99e7-0942a2639ccb


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
