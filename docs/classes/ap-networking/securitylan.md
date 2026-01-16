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

#### Enterprise Physical Security Threat Analysis

**1. Unauthorized access to labs**  
This vulnerability occurs at laboratory entrances that are insufficiently controlled or monitored. If unauthorized individuals gain access to labs, they could steal research data or damage sensitive equipment. 

**2. No restricted zones**  
This vulnerability exists where public spaces such as lobbies or office areas are not clearly separated from restricted research or data center areas. Without proper zoning, an individual could move easily move from a low-critical area to a extremely-critical area.

**3. Insufficient physical protection of network closets**  
This vulnerability exists in network closets or server rooms that are unlocked, or poorly secured. Physical access to switches, servers, or patch panels allows attackers to connect rogue devices or disrupt network availability. 

**4. Lack of environmental controls**  
This vulnerability occurs when temperature and airflow systems are inadequate. Servers and network devices are highly sensitive to environmental conditions such as overheating which may halt research operations and violate regulatory requirements.

**5. Limited surveillance**  
This vulnerability exists when cameras and alarm systems are missing or insufficient in labs, data centers, or network rooms. Without surveillance, increases the risk of theft, sabotage, and delayed incident response.

**6. Weak visitor and personnel procedures**  
This vulnerability stems from inconsistent enforcement of visitor policies, resulting in rogue attackers gaining access to the site.

#### Physical Security Plan 

**1. Environmental Controls**
Redundant cooling systems, humidity control, and air filtration systems to constantly monitor temperature and prevent overheating in data centers. 

**2. Access Control**
Access to the facility is divided into security zones: public, restricted, and highly restricted. Badge based authentication is required at every door with the critical sections being highly-restricted to only a few staff members necessary.

**3. Surveillance and Detection**
Cameras are installed all around the facility, inside every room, and at every entrace. All surveillance feeds are monitored from a centralized security operations area, and access logs are retained for auditing and investigations. Alarms alert security staff to unauthorized access attempts. 

**4. Hardware Security**
All servers and network devices are housed in locked racks within secured rooms. Network closets remain locked, and physical access to switch ports and patch panels is restricted to only a few members.

**5. Personnel and Procedures**
Strict procedures are gone through to ensure visitors access to the facility. Visitors must be escorted at all times inside the facility and movemnet logged.


**Physical Security Diagram:**

<img width="1920" height="1080" alt="Screenshot 2026-01-12 at 9 33 42 AM" src="https://github.com/user-attachments/assets/08524d1d-5628-404b-a8ee-ac90ff2a4a51" />

### Risk Justification and Priority Controls

The highest priority physical controls for this pharmaceutical research facility is access control. Preventing unauthorized physical access to laboratories, data centers, and network infrastructure it extremely important to reduce the changes of unauthorized personnal tampering or stealing data.

Physical security directly supports network segmentation, access control lists, and monitoring systems. When devices are physically protected, technical controls cannot be easily bypassed or disabled. Together, these measures reduce attacks and violations to ensure the integrity and availability of critical research operations.


## 4. Testing & Evaluation 

## 5. Reflection  


