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

## 4. Testing & Evaluation – Network Verification

## 5. Reflection  
