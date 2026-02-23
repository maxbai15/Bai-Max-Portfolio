# Determining Security Controls in a LAN

## 1. Project Overview  

**Problem Statement:**  
Understand different security vulnerabliites, both logically and physically, and tehcniques to help mitigate risks.

**Objectives:**  

- Observe how ARP functions inside a LAN and what information it exposes
- Simulate internal LAN traffic between two virtual machines
- Learn how enterprise LAN security controls mitigate internal attacks
- Connect specific vulnerabilities to appropriate technical security controls

**Success Criteria:**  

- Successfully understanding different vulnerabilites, like DHCP snooping MAC Address Flooding.
- Understanding different security controls, like VLAN segmentation
- Determining physical vulnerabilties and ways to counteract

## 2. Design & Planning 

Before applying security controls, it is necessary to understand why internal LAN attacks are possible in the first place. Many core networking protocols were designed around efficiency and trust rather than security. Once a device gains physical or logical access to a switched LAN it can often observe and influence network behavior unless defensive controls are in place.

### Key LAN Security Concepts & Vocabulary

- **Internal LAN Threats:** Attacks that originate from inside the local network after a device is connected, rather than from an external attacker on the internet. 

- **Broadcast Domain:** A group of devices that receive the same broadcast traffic, such as ARP requests and DHCP discovery messages. Large broadcast domains increase exposure to internal attacks.

- **East–West Traffic:** Network traffic that flows between devices inside the LAN. 

- **Rogue Device:** An unauthorized device connected to the network that may intercept traffic and exploit the network.

#### VLAN Segmentation
Virtual Local Area Networks (VLANs) divide a physical switch into multiple logical networks, each with its own broadcast domain. This limits exposure to broadcast traffic and isolates sensitive systems.

#### DHCP Snooping
DHCP Snooping protects the network from rogue DHCP servers that attempt to assign malicious IP configurations. Allows trusted ports to send DHCP offers while unauthorized ones cannot. Keeps a MAC address table that becomes a basis for many different security mechanism


## 3. Technical Development 

### Layer 3 Identity

**VM#1(Ubuntu) Layer 3 Info**

<img width="2272" height="984" alt="Image 2-23-26 at 8 36 AM" src="https://github.com/user-attachments/assets/becf0f2f-5dfd-4169-89e2-6529a8c916e9" />

In VM#1, the `ip addr` command shows both the IPv4 and network address. `10.12.26.143/20` is the IPv4 address and `127.0.0.1/8` is the network. Additionally, the command `ip route` shows the default gate way which is `10.12.16.1`.

**VM#2(Linux) Layer 3 Info**

<img width="1706" height="748" alt="Image 2-23-26 at 8 38 AM" src="https://github.com/user-attachments/assets/bbc93358-50ac-47da-b226-f2cc5ccd3cc0" />

In VM#2, the `ip addr` command shows both the IPv4 and network address. `10.12.17.38/20` is the IPv4 address and `127.0.0.1/8` is the network(same as VM#1). Additionally, the command `ip route` shows the default gate way which is `10.12.16.1`(same as VM#1).

## 4. Testing & Evaluation 

| Concept | Test Performed | Verification Result |
|-------|---------------|---------------------|
| ARP Information | Observed ARP requests and replies using `arping` and `tcpdump`  | Confirmed that IP addresses are visible to any device in the same broadcast domain |
| Devices on Broadcast Domain  | Placed both VMs in bridged mode on the same LAN | Verified that ARP traffic is broadcast and received by other devices on the LAN |
| MAC Flooding Impact | Reviewed MAC flooding attack diagram and switch behavior | Verified excessive MAC addresses can overwhelm switch tables and disrupt traffic forwarding |
| VLAN Segmentation | Evaluated flat vs segmented network scenarios | Confirmed VLANs limit east–west traffic and isolate sensitive devices |
| Port Security | Analyzed scenario of unknown device entering the LAN | Helps port security prevent unauthorized MAC addresses from using switch ports |

## 5. Reflection  

This project helped me understand how internal LAN attacks occur and why security controls inside the network are important to help prevent rogue devices and attacks. By observing ARP traffic between two virtual machines, I was able to see firsthand how much information is exposed by default within a broadcast domain. ARP requests and replies revealed how easily devices on a network can connect without security controls

Analyzing different attack scenarios strengthened my deduction skills to figure out potential vulnerabilities and securities. The physical security portion of the project emphasized that technical controls alone are not sufficient. I learned that physical access often equals full system compromise since attackers can bypass authentication and easily steal data or mess up the network

Overall, this project connected physical security and logical controls to create complete security mindset against vulnerabilities. It showed me that secure networks depend on trust being carefully limited and continuously enforced at every layer.

