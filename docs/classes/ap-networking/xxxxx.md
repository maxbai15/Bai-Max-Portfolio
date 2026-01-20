# Determining Security Controls in a LAN

## 1. Project Overview  

## 2. Design & Planning – Understanding Physical and Logical Addressing


## 3. Technical Development – Implementing Authentication & Security

### Common LAN Threats

In a switched LAN environment, a standard endpoint device like an unmanaged workstation is arguably the easiest target for an attacker to compromise. These devices often have less  security configurations than critical network infrastructure like firewalls or core switches. This contrasts with infrastructure devices which are generally better hardened and less exposed to direct threats.
A device being “inside” the network is generally far more dangerous for the entire organization than one outside. Internal positioning bypasses initial perimeter defenses like firewalls and intrusion prevention systems, granting an attacker direct access to internal resources, sensitive data, and the ability to move  across the network to compromise further systems. Outside devices must contend with multiple layers of security designed to detect and block unauthorized access attempts.
By default, a typical device inside a switched LAN has limited visibility into other devices' traffic. A switch learns which devices are on which ports and only forwards traffic intended for a specific destination to that port. However, an attacker can learn a great deal about the network's structure, the IP addresses and MAC addresses of other devices, open ports, and potentially intercept traffic if they use specific techniques like Address Resolution Protocol (ARP) spoofing or port mirroring. 

**Screenshot Showing Evidence of Neighbor Discovery:**

<img width="2780" height="1448" alt="Image 1-14-26 at 12 40 PM" src="https://github.com/user-attachments/assets/12f18adf-6e36-4859-836e-97054401a9bd" />

A attacker could directly utilize the infromation in the screenshot because it can see the default gateway and potentially use that to try and enter the network. Additionally, the arp command demonstrates how once inside the network, attackers would be able to see other devices within the network.

**Scenario Table:**

| Scenario | Symptoms | Hypothesis | Justification |
|---------|---------------|---------------------|----------|
| Scenario A | Multiple device have valid IP addresses but not gateway addresses that match the router, so they can't connect to internet | DHCP Conflict | Some devices might be getting assinged IP addresses from another router, causing certain devices to have valid IP addresses but the wrong default |
| Scenario B | High CPU performance because hundreds of MAC addresses appear on a single switch suddenly | MAC Address Flooding | Many MAC addresses flooding the server suddenly instead of gradually hints at an attack. Also it results in the slowing dont of the network which is what an attacker may try to do. |
| Scenario C | A few devices have been assigned IP addresses in the wrong subnet. DHCP is up, but the normal network documentation is different. | DHCP Spoofing | First, they are assigned the wrong IP addresses which could happen because of DHCP Spoofing. Additionally, the normal documentation differs which hints at this being an attack because it isn't an official assignment |
| Scenario D | An unseen device sunddenly communicates with multiple hosts on a network. Appears to come from a physical jack | Rogue Network Device | The unseen device enters during normal hours and is not authorized to be in the network. Assumed to come from a wall jack, it can easily enter the network since the physical ports are loose. |
| Scenario E | A student workstation with no admin rights is communicationg with restricted areas of the network | No VLAN Segmentation | Since no firewalls are trigged when the student workstation communicates with admin and server devices, their must be no segmentation since the lower level devices are able to enter restricted data. |

### Switch Security Controls

| VM Evidence | Vulnerability | Control | Why Mitigates Risk |
|---------|---------------|---------------------|----------|
| <img width="819" height="365" alt="Screenshot 2026-01-16 at 9 45 10 AM" src="https://github.com/user-attachments/assets/8d626b08-ae18-4c06-8f6c-870427fdeb26" /> | The first screenshot shows a flat network without vlan segmentation. The network has a switch with two end devices connected to it. With the flat segmentation, any device on the network can see other devices| VLAN Segmentation | Creating different VLANs will help to ensure all devices on the network can't see each other, only being split into networks where certain devices can see certain devices |
| <img width="465" height="264" alt="Screenshot 2026-01-16 at 9 52 17 AM" src="https://github.com/user-attachments/assets/85999a36-5ce7-48b4-b89c-c1a637916bae" />, <img width="444" height="166" alt="Screenshot 2026-01-16 at 9 48 51 AM" src="https://github.com/user-attachments/assets/76dc7fcc-7b09-4e9c-b147-abeed2594d3e" /> | The flat network from above | The screenshots demonstrate the commands for creating two different VLANs(10 - Students, 20 - Servers). The second screenshot demonstrates the successful VLAN creation with the end devices assigned to different VLANs | This helps mitigate risk since only devices on the same VLAN can now reach each other, protecting more critical devices like the server from just normal devices at the student level |
| <img width="254" height="82" alt="Screenshot 2026-01-16 at 9 57 55 AM" src="https://github.com/user-attachments/assets/18cf8fb9-0c1b-4745-979d-2f43ad10491d" />, <img width="285" height="330" alt="Screenshot 2026-01-16 at 9 59 51 AM" src="https://github.com/user-attachments/assets/ee42f0a3-7df0-4676-9e32-e32d65d96e97" /> | Unprotected port security is a vulnerability since any device connecting to a port on the network gains access to the network without any problem | The fire screenshot demonstrates how to enable this using switchport commands while the second screenshot is evidence of port security being enabled on both end devices for ports fa0/1 and fa0/2 | Port Security helps to mitigate risks because it protects from a rogue device joining the network by simply just plugging in a device to the port. Physical access is important here since an unprotected port is like an open gateway to the network. |
| <img width="1027" height="925" alt="Screenshot 2026-01-16 at 10 16 59 AM" src="https://github.com/user-attachments/assets/2595ddba-a93d-4397-8228-ab09912b69b8" /> | The show arp and dhcp doesn't work since no requests are being made and ip address isnt setup on devices. Screenshot shows the configuration of the different ports on the switch. From it, doesn't show any rogue network so far | Can use this to find unknown devices and problems in configuration | Can help to mitigate risks because a technician can see configuration of devices on the switch and potentially scout out different potential attackers or harms |

### Explain, Design, Defend

**Scenario B -- The Compromised Teacher Laptop**

A teacher’s laptop is infected with malware after opening a phishing email while connected to the school network.

1. What must the attacker already know or discover?

The attacker likely needed to discover the teacher's email address and possibly general information about the school or the teacher to craft a convincing phishing email. They must also know that the email system is an unguarded part of the network, making it easy to enter. 

2. Which device is most directly targeted?

Another end device is most directly the target since the goal of the attack is to compromise different machines to gain control of the network. Once the main device is compromised, it will try and control the whole network, most likely starting with other devices that are the most easily reachable, like other end devices.

3. What would legitimate users likely notice (if anything)?

Legitimate users would likely notice nothing abnormal. Many attacks, like malware, run quietly in the background to avoid detection. The teacher might notice a momentary system slowdown, but the attack itself is designed to be stealthy. 

4. Which of your virtual machines best resembles the attacker’s perspective?

The Ubuntu Desktop VM best resembles the attacker's perspective. An attacker often uses a general operating system with a graphical interface  to conduct the initial stages of a complex attack, such as crafting phishing emails and inflitrating the network. 

**Clean Network Sketch**

<img width="1308" height="732" alt="Screenshot 2026-01-20 at 1 41 02 PM" src="https://github.com/user-attachments/assets/4cf35c88-c0c0-48e5-b773-c6ca15d85e34" />

- Students -> Servers: Restricted, students are low privelage and shouldn't be able to communicate with the high access server VLAN unless absolutely necessary and give permission.
- Students -> Teachers: Allowed, students need to be able to communicate with teacher as both are relatively low privelage VLAN's
- Students -> Administration: Restricted, only in some cases should students be able to reach admin rights when absolutely necessary. Students don't need to see the critical information in this VLAN
- Teachers -> Servers: Restricted, requests to access the server should be requested through the admin VLAN to keep the segmentation and protect critical data
- Administration -> Servers: Allowed, administration should be able to access the whole network in order to change anything needed

In the diagram, the main switch needs protection as it is the entrance to the entire network. Once inside though, Switch 2 should have extra added security as it leads to the admin devices and servers, the backbone and highest privilege data within the network. Switch 1 should be the least trusted within the entire network as it is the easiest to penetrate with lower security for student and teach VLANs.

In the design, VLAN's alone do not fully secure the network since it is still possible to inflitrate the different networks once inside. Additionally, DHCP snooping is necessary as student and teacher VLANs are not that heavily protected which means DHCP spoofing can happen at these levels, slowing down the entire network. With the DHCP snooping implemented, DAI would also be implemented as DHCP snooping would prevent malicious packets from entering the network and messing up the network. Based on what a normal device can communicate with from the mini-threat scenarion, even though VLAN segmentation blocks broadcast traffic, inter layer traffic can still go across VLAN's, making ACL's necessary to help stop attacks from within. In general, the hardest threats to spot are ones that come from within the network. This is the case since they have already breached most of the security procedures, such as DHCP snooping and port security measures. These attacks can usually only be discovered once the network has already slowly started to fail or when data is already being stolen. 


## 4. Testing & Evaluation – Network Verification

## 5. Reflection  
