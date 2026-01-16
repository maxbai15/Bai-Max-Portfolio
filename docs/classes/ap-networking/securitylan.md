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


### Common Security Controls

On a LAN, devices such as misconfigured printers of access points like routers or switches would be the easiest place for an attacker to compromise since those are usually where the security is the weakest since people have to commonly access those devices. Proximity doesn't equal safety since wireless connections are often more vunerable through open gates/doors through wi-f/network connections. In a LAN devices can often see traffic involving the device and also open doors/ports.

| Scenario Letter | Symptoms | Hypothesis | Justification |
|---------|---------------|---------------------|----------|
| Scenario A | A device recieves a default gateway that does not match the actual router | DHCP Misconfiguration | The deafult ip is conigured by DCHP, but it doesn't seem to be the right gateway so it was configured incorrectly |
| Scenario B | The switch CPU spkies many MAC addresses appear on one port | Cyberattack | Many MAC addresses flooding the server would disrupt the transportation of information to the right places, destroying the network |
| Scenario C | Clients receive IPs from an unexpected source. | DHCP Spoofing | Random unauthorized source assings IP address, meaning that it could potentially be a false DHCP offer |
| Scenario D | A new unknown device appears inside the broadcast domain | Bad Port Security | If ports don't have security control, any unknown device can easily enter the network and communicate through the broadcast domain |
| Scenario E | A host begins reaching other internal hosts it should never reach | Flat Network | Since any device can reach other ones, that means the network is flat with no VLAN segmentation. This means any device within the network can communicate with other ones on the same network |

### Security Controls Common Vulnerabilities

**ip addr and ip route VM#2**

![Image 12-17-25 at 10 32 AM](https://github.com/user-attachments/assets/da4509c6-b2c7-4874-bda5-a8b529692535)

**arping from VM#1**

![Image 12-17-25 at 10 49 AM](https://github.com/user-attachments/assets/f378ea71-d32b-4105-8d7b-3ee805ebdc25)

**tcpdump on VM#2**

![Image 12-17-25 at 10 50 AM](https://github.com/user-attachments/assets/a7fab037-cfcd-4cc4-86b5-d22dbd846552)

ARP reveals the Media Access Control (MAC) addresses associated with specific Internet Protocol (IP) addresses of devices on a local area network (LAN). It operates by broadcasting a request asking which device has a particular IP address and expects the corresponding device to respond with its unique hardware address.
ARP assumes devices are trustworthy because the original design philosophy of early networks, for which ARP was created, often prioritized functionality and efficiency over robust security, operating in what were considered inherently trusted local environments. The protocol has no built-in mechanisms for verification or authentication of responses; it simply accepts the first valid reply it receives as legitimate and caches the information for future use.
This lack of authentication makes ARP vulnerable to spoofing because a malicious actor can send a false ARP reply, claiming to have the MAC address for a different device's IP address. Legitimate devices on the network will update their ARP caches with this incorrect information, inadvertently sending traffic meant for the legitimate device to the attacker instead.
Bridged mode was likely required for this lab to work because it places the virtual machine directly onto the physical host's network, giving it a unique IP address on the same LAN as other devices. This configuration allows the virtual machine to participate in the broadcast domain and exchange ARP traffic directly with other physical and virtual hosts, which is essential for observing or performing ARP-related activities like spoofing within a realistic LAN environment.

**MAC Flooding Attack Diagram**

<img width="1394" height="798" alt="Screenshot 2025-12-18 at 12 47 13 PM" src="https://github.com/user-attachments/assets/2c0ff8fc-85a3-47c6-9979-629a3e0a3e0b" />

### Physical Security Controls

**Physical Security Diagram:**

<img width="1920" height="1080" alt="Screenshot 2026-01-12 at 9 33 42 AM" src="https://github.com/user-attachments/assets/08524d1d-5628-404b-a8ee-ac90ff2a4a51" />


## 4. Testing & Evaluation 

## 5. Reflection  

Through these addressing labs, I gained comprehensive understanding of how devices identify themselves at both the physical hardware level and the logical network level, and why both types of addressing are essential for modern networking. The physical addressing activities taught me that MAC addresses are permanently embedded into NICs during manufacturing and serve as the fundamental identifier for Layer 2 communication within local networks. I got to understand the physical components of the NIC along with the different identifiers for the MAC address. Additionally, I learned how Logical addressing through IP addresses works alongside MAC Addresses to provide connection since IP addresses complete the transformation of information for global connection.

I also developed a strong understanding of the difference between DHCP and static addressing, especially how DHCP provides convenience for devices that change networks, while static addressing is required for predictable and stable access to different networks and servers. Comparing VM #1 and VM #2 helped me see how different systems utilize different tools, Netplan and NetworkManager, for managing network configuration. One of the most important lessons I learned was how sensitive YAML files are; even minor mistakes in spacing or indentation can break the entire network configuration. Switching VM #2 from DHCP to a static IP and verifying connectivity made the concepts feel real and connected everything I learned to practical, real-world network administration. Overall, this project strengthened my understanding of how addressing works from the hardware level all the way up to routing across networks, and how essential careful configuration is in any professional networking environment.
