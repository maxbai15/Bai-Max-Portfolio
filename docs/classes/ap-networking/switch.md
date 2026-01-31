# Switch Security

## 1. Project Overview  

**Problem Statement:**  
Understand how switch level security mechanisms mitigate risk by limiting access, visibility, and trust within a LAN.

**Objectives:**  

- Identify common switch based attacks   
- Implement switch security controls such as VLAN segmentation and port security  
- Analyze potential external threats  
- Evaluate how switch controls mitigate attacks  

**Success Criteria:**  

- Correctly identify LAN based attack scenarios and their symptoms  
- Explain how switch security controls mitigate specific vulnerabilities  
- Demonstrate understanding of VLANs, port security, and internal threat containment  
- Verify that segmentation and switch controls limit unauthorized communication  


## 2. Design & Planning – Understanding Physical and Logical Addressing

Before implementing switch security controls, it is necessary to understand how internal threats will be limited using mechanisms directly configured on the switch to reduce implicit trust within the LAN by controlling how traffic is segmented.

### Switch Security Controls  

The following are some controls to help internal security within a switch:

**VLAN Segmentation:**  
The network will be logically divided into multiple VLANs based on user role and privilege level, such as students, teachers, administration, and servers. This reduces broadcast domain size and limits east–west traffic between devices that should not directly communicate.

**Port Security:**  
Switch ports connected to endpoint devices will have port security enabled. This limits the number of allowed MAC addresses per port and prevents unauthorized devices from gaining network access simply by plugging into an open jack.

**Monitoring and Visibility:**  
Switch show commands and configuration reviews will be used to identify misconfigurations, unknown devices, or abnormal behavior. Visibility into VLAN assignments and port states allows administrators to detect and mitigate potential internal threats.

**DHCP and ARP Trust Awareness:**  
Since DHCP and ARP are trusted by default, the mechanism acknowledges their vulnerabilities. DHCP snooping and Dynamic ARP Inspection are controls to protect against spoofing attacks.

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
|------------|---------------|---------|-------------------|
| <img src="https://github.com/user-attachments/assets/8d626b08-ae18-4c06-8f6c-870427fdeb26" alt="Flat network topology" style="width: 100%; min-width: 400px;" /> | The screenshot shows a flat network without VLAN segmentation. With a flat network, any connected device can see and communicate with other devices on the LAN. | VLAN Segmentation | VLANs separate devices into different broadcast domains so only authorized devices can communicate, reducing internal attack surface. |
| <img src="https://github.com/user-attachments/assets/85999a36-5ce7-48b4-b89c-c1a637916bae" alt="VLAN creation commands" style="width: 100%; min-width: 400px;" /><br><br><img src="https://github.com/user-attachments/assets/76dc7fcc-7b09-4e9c-b147-abeed2594d3e" alt="VLAN verification" style="width: 100%; min-width: 400px;" /> | The original flat network configuration allowed unrestricted communication between devices. | VLAN Creation and Assignment | Devices are assigned to different VLANs (Students and Servers), preventing low-privilege devices from accessing critical systems. |
| <img src="https://github.com/user-attachments/assets/18cf8fb9-0c1b-4745-979d-2f43ad10491d" alt="Port security configuration" style="width: 100%; min-width: 350px;" /><br><br><img src="https://github.com/user-attachments/assets/ee42f0a3-7df0-4676-9e32-e32d65d96e97" alt="Port security enabled" style="width: 100%; min-width: 350px;" /> | Without port security, any device plugged into a switch port gains immediate access to the network. | Port Security | Port security limits which MAC addresses can use a switch port, preventing rogue devices from joining the LAN. |
| <img src="https://github.com/user-attachments/assets/2595ddba-a93d-4397-8228-ab09912b69b8" alt="Switch configuration overview" style="width: 100%; min-width: 450px;" /> | Misconfigurations or unknown devices can go unnoticed without proper visibility into switch settings. | Switch Monitoring and Review | Reviewing switch configuration allows administrators to identify unknown devices, misconfigured ports, and potential internal threats. |

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

| Concept | Test Performed | Verification Result |
|-------|---------------|---------------------|
| Neighbor Discovery | Used `arp` from an internal VM | Confirmed that internal devices can learn gateway and other device information |
| Flat Network Risk | Observed communication between devices on the same switch without VLANs | Verified unrestricted east–west communication |
| VLAN Segmentation | Created VLAN 10 (Students) and VLAN 20 (Servers) and assigned ports | Confirmed devices could only communicate within their assigned VLAN |
| Port Security | Enabled port security on switch interfaces | Verified that only authorized devices could use protected ports |
| Switch Configuration Review | Used show commands to inspect switch state | Confirmed visibility into port status, VLANs, and potential misconfigurations |

## 5. Reflection  

This project strengthened my understanding of how critical switch security is in defending a LAN from internal threats. I learned that internal devices pose a greater risk than external attackers because they already exist inside the trust boundary of the network. Observing how much information is available through basic neighbor discovery reinforced why default switch behavior is not secure enough.

Designing and implementing VLAN segmentation helped me see how logical separation limits east–west traffic and protects critical systems such as servers and administrative devices. Port security further emphasized how physical access directly translates into network access if not controlled properly.

The testing phase showed that security controls must be layered. VLANs alone are not enough, and additional protections like DHCP snooping, DAI, and access control lists are necessary to defend against spoofing and lateral movement. Overall, this project demonstrated that switch security is a foundational component of network defense and that effective LAN security depends on limiting trust and continuously monitoring internal activity.
