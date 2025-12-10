# Determining Security Controls in a LAN

## 1. Project Overview  

**Problem Statement:**  
Understand how devices identify themselves on networks through physical (MAC) and logical (IP) addressing, and learn how to configure both dynamic and static IP addresses.

**Objectives:**  

- Identify and understand MAC addresses on physical NICs and virtual machines
- Explain the difference between physical and logical addressing
- Analyze DHCP versus static IP addressing and when to use each
- Configure static IP addresses using Netplan on a Linux VM

**Success Criteria:**  

- Complete NIC labeling with accurate identification
- Successful understanding of MAC addresses and different sections
- DHCP analysis from both VMs showing configuration differences
- Working static IP configuration on VM #2 verified with ip addr, ip route, and ping tests

## 2. Design & Planning – Understanding Physical and Logical Addressing

### MAC Addresses


## 3. Technical Development – Implementing Authentication & Security

### Common Security Controls

On a LAN, devices such as misconfigured printers of access points like routers or switches would be the easiest place for an attacker to compromise since those are usually where the security is the weakest since people have to commonly access those devices. Proximity doesn't equal safety since wireless connections are often more vunerable through open gates/doors through wi-f/network connections. In a LAN devices can often see traffic involving the device and also open doors/ports.

| Scenario Letter | Symptoms | Hypothesis | Justification |
|---------|---------------|---------------------|----------|
| Scenario A | A device recieves a default gateway that does not match the actual router | DHCP Misconfiguration | The deafult ip is conigured by DCHP, but it doesn't seem to be the right gateway so it was configured incorrectly |
| Scenario B | The switch CPU spkies many MAC addresses appear on one port | Cyberattack | Many MAC addresses flooding the server would disrupt the transportation of information to the right places, destroying the network |


## 4. Testing & Evaluation – Network Verification

## 5. Reflection  

Through these addressing labs, I gained comprehensive understanding of how devices identify themselves at both the physical hardware level and the logical network level, and why both types of addressing are essential for modern networking. The physical addressing activities taught me that MAC addresses are permanently embedded into NICs during manufacturing and serve as the fundamental identifier for Layer 2 communication within local networks. I got to understand the physical components of the NIC along with the different identifiers for the MAC address. Additionally, I learned how Logical addressing through IP addresses works alongside MAC Addresses to provide connection since IP addresses complete the transformation of information for global connection.

I also developed a strong understanding of the difference between DHCP and static addressing, especially how DHCP provides convenience for devices that change networks, while static addressing is required for predictable and stable access to different networks and servers. Comparing VM #1 and VM #2 helped me see how different systems utilize different tools, Netplan and NetworkManager, for managing network configuration. One of the most important lessons I learned was how sensitive YAML files are; even minor mistakes in spacing or indentation can break the entire network configuration. Switching VM #2 from DHCP to a static IP and verifying connectivity made the concepts feel real and connected everything I learned to practical, real-world network administration. Overall, this project strengthened my understanding of how addressing works from the hardware level all the way up to routing across networks, and how essential careful configuration is in any professional networking environment.
