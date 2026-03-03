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

**Loopback Screenshot:**

<img width="1396" height="416" alt="Image 2-24-26 at 9 14 AM" src="https://github.com/user-attachments/assets/57fe8b00-7062-4d18-9fe8-43866c2a6d65" />

The traffic does not leave the machine as it is a software loopback to the same machine. It doesn't need a default gateway either as it isn't going outside of the network.

**Screenshot of ping sent to another VM(same network):**

<img width="1368" height="426" alt="Image 2-24-26 at 9 17 AM" src="https://github.com/user-attachments/assets/27b91ed5-1485-4f50-b0cb-ef521e8279d5" />

Because the UTM VM and Ubuntu VM are on the same network a default gateway isn't required as it isn't going outside of the network. Being on the same subnet allows for the two devices to reach each other within the network. To test whether or not a gateway was used, use the traceroute command to see the hops taken to reach the other device.

**Screenshot of ping sent outside the network:**

<img width="1564" height="254" alt="Image 2-24-26 at 9 19 AM" src="https://github.com/user-attachments/assets/04cee227-a189-4a27-8b88-780e7656d3b7" />

When you ping an external address like 8.8.8.8, Ubuntu uses its default gateway because it cannot deliver the packet directly. This direct delivery is impossible because the destination IP address does not match any local subnet masks assigned to the VM's network. The default gateway handles the first step by receiving the packet and forwarding it beyond the local network toward the internet. 

The routing table acts as a network address map that a device consults to determine the  path for any outgoing data packet. When a packet’s destination is not within the local subnet, the default gateway serves as the  exit point, receiving that traffic and forwarding it toward external networks or the internet. Direct delivery is possible only when the destination IP address falls within the sender's own subnet, allowing the devices to communicate directly via their physical MAC addresses. On the other hand, router involvement is required whenever the destination address is on a remote network or different subnet.

### Who Can See You

**Ubuntu IPv4 Screenshot:**

<img width="2216" height="616" alt="Image 2-25-26 at 10 09 AM" src="https://github.com/user-attachments/assets/50dbbd19-5451-410d-aa49-18497165619f" />

**Display Public IP Screenshot:**

<img width="886" height="94" alt="Image 2-25-26 at 10 13 AM" src="https://github.com/user-attachments/assets/c18f56f2-4fe2-4691-8bcb-dd487ac4d4bb" />

My public IP address is different from my private IP address as shown by the two screenshots above. They are not the same to shield my device from being seen by random devices when connecting to public spaces like the internet or other networks. It also allows multiple devices on a private network to shared one public IP address whenever connecting to the broader web or other networks.

**Ping Partner Private IP Address Screenshot:**

<img width="1176" height="340" alt="Image 2-25-26 at 10 29 AM" src="https://github.com/user-attachments/assets/fb67258f-1bc9-4c20-924c-636f2915f2a5" />

**Ping Partner Public IP Address Screenshot:**

<img width="1218" height="216" alt="Image 2-25-26 at 10 30 AM" src="https://github.com/user-attachments/assets/39a38eae-c904-4b17-9188-4bd0c17af321" />

In this experiment, the success of the private IP ping indicates that both partners are on the same local subnet, allowing the machines to communicate directly. On the other hand, the failure of the public IP ping is because most private networks have routers and firewalls that are configured to block an unwanted external traffic as a security measure to hide the network from potential outside threats. This means that while the public address is valid and active, the device at that address is intentionally filtering the traffic rather than responding to it. This demonstrates that private addresses are for open internal communication, while public addresses are guarded by protective barriers to prevent unauthorized external access to private networks.

Private IPv4 addresses are reused in millions of networks because they are designed for internal identification only, allowing an infinite number of local networks to use the same common ranges without conflict. These addresses are not routed on the public internet because they are not globally unique. If every internal device required its own public IP, the internet would have collapsed years ago because the available IPv4 addresses are insufficient for the amount modern devices. Additionally, businesses typically use one public IP to represent many internal devices to help with the problem of limited address space, relying on a router to translate traffic for an entire network. This drastically simplifies WAN design by allowing large internal infrastructures to connect to the global internet through a single point that masks the private network from outsiders.

### Following A Packet Across A Router

**Screenshot of Packet Tracer Devices and Wiring:**

<img width="1083" height="461" alt="Screenshot 2026-02-26 at 12 25 52 PM" src="https://github.com/user-attachments/assets/71d8e7bf-946b-4e21-9a9f-451434be612d" />

The screenshot above shows the setup of the devices with the correct copper-straight through wiring connections. Currently the connectio between the switches and routers is red since nothing has been configured yet(the router or ip addresses on the devices).

**Screenshot of PC Configurations:**

<img width="699" height="708" alt="Screenshot 2026-02-26 at 12 26 36 PM" src="https://github.com/user-attachments/assets/f1c16874-e247-40f0-87cc-948ef0e6972e" />

<img width="699" height="703" alt="Screenshot 2026-02-26 at 12 26 59 PM" src="https://github.com/user-attachments/assets/c39f51b5-f89c-4e00-b461-eeec3cb0a9e9" />

The screenshot above shows the IP configuration of the PC's and the default gateway.

**Screenshot of Router Configurations:**

<img width="644" height="295" alt="Screenshot 2026-02-26 at 12 28 05 PM" src="https://github.com/user-attachments/assets/100f3ee9-a8dd-431c-b0fd-1e3c60c11f0f" />

The screenshot above demonstrates the IP configuration of the router.

**Screenshot of Successful Configuration:**

<img width="1296" height="599" alt="Screenshot 2026-02-26 at 12 28 33 PM" src="https://github.com/user-attachments/assets/1163fe76-ef1a-42a2-8fb0-fca2af0f6236" />

The screenshot above demonstrates how the configuration of PC's and Routers was successful as the connection all devices is now up and ready.

#### Observe Network Communications

**PDU PC0 to Router:**

https://github.com/user-attachments/assets/1fd84b76-1d03-4b1b-a2cd-867dbec26c3f

During this PDU,a packet was sent within the same netwrok  from PC0 to the router. Before the the packet travel an ARP event happend to find where the packet would go. This occurred because PC0 knew the destination IP address but lacked the MAC address. The packet remained at PC0 until the ARP request was broadcast across the local network and the router responded with its MAC address. After the MAC address was found, the packet moved from PC0 to Switch0 and finally to the Router. The packet remained entirely on the left side as it was able to travel exactly where it needed to within its own subnet.

**PDU PC0 to PC1:**

https://github.com/user-attachments/assets/b1ae82a5-10d3-4347-862c-e481fdbe39ba

When sending a packet from PC0 to PC1, the Layer 3 IP header remains constant along with the final destination IP address. Since the destination IP address isn't within the subnet, the packet must travel through the router first, default gateway. When leaving PC0, the destination MAC address is set to the router's interface rather than the final PC, as the router is the necessary exit point for traffic leaving the local subnet. Upon reaching the router, the original frame is stripped away and a new one is created using the router's. This process demonstrates that while IP addresses are preserved from start to finish to identify the original sender and final receiver, MAC addresses must change at different hops to facilitate local delivery across different physical segments.

**PDU PC0 to PC1 without Router:**

When the packet went, it failed to reach the PC1 because it wasn't properly transported. Without a router, the packet will not be able to exit the local subnet as it has no default gateway to exit, meaning the packet would be stopped before even exiting the local network.

### Data Using Routing Tool

**Ubuntu IP Route Screenshot:**

<img width="1394" height="302" alt="Image 3-2-26 at 9 43 AM" src="https://github.com/user-attachments/assets/6cdb966d-467f-4a01-8cb9-621715247b84" />

#### Traceroute Predictions

For the traceroute to the other VM, the first hop should go directly to the destination of the other VM as they are on the same network. It would not go through the default gateway since it is not trying to exit the newtork. There should be only one other hop directly to the other VM.

For the traceroute to 8.8.8.8 it is another story since trying to reach 8.8.8.8 would be going outside the network. The first hop should be to the default gateway as the ping is going outside the network. Multiple hops should happen as the ping makes its way to the 8.8.8.8 server with the last hop being 8.8.8.8. I expect the same for a ping to google.com too.

**Traceroute other VM Screenshot:**

<img width="1368" height="146" alt="Image 3-2-26 at 10 00 AM" src="https://github.com/user-attachments/assets/a79bc187-877a-41a3-b4ee-9349391f4390" />

**Traceroute 8.8.8.8 Screenshot:**

<img width="2562" height="568" alt="Image 3-2-26 at 9 59 AM" src="https://github.com/user-attachments/assets/f0b93951-6f85-43bc-bfbd-e6867ba639a6" />


**Traceroute google.com Screenshot:**

<img width="2130" height="1150" alt="Image 3-2-26 at 9 57 AM" src="https://github.com/user-attachments/assets/d25c7f4c-651f-448c-9a9f-0cffdeb4e0cd" />

For all the screenshots above, like predicted before, the only hop for the other VM ping is that other VM since the two devices are in the same network. Additionally, both the 8.8.8.8 and google.com traceroute go through the default gateway first to exit the network. A difference beteween the two though is the number of hops since they take different paths to reach the final destination with google.com needing more hops than 8.8.8.8.

Analyzing the traceroute 8.8.8.8 specifically, the first hop is to the deafult gate which is a private IP address. Aditionally, the second hop is still to a private IP address as it still remains within the overall network of Charlotte Latin(this hop is likely to a router or default gateway of the entire Latin network). After that the next IP addresses all become public as it needs to enter different public services to reach all the way to the 8.8.8.8 DNS server(a public server).

**IP route Screenshot:**

<img width="1108" height="256" alt="Image 3-2-26 at 10 07 AM" src="https://github.com/user-attachments/assets/21790da5-0889-4c49-8345-2354d52a1b50" />

**TTL Experiment Screenshot:**

<img width="1734" height="230" alt="Image 3-2-26 at 10 08 AM" src="https://github.com/user-attachments/assets/d9dba17d-cecf-4aee-ba9b-4a96b0a5bbe9" />

In the above, traceroute is ran again to find 8.8.8.8, but it is limited to 3 maxmimum hops. As a result, it only shows the first 3 hops that would normally happen and stops after that since only 3 hops are allowed.

The path of data from a device can be determined using traceroute. In a network, the first hop represents your default gateway, which is the local router that provides your exit point from the network. Private IPs appear early in the path because your traffic must first navigate the internal LAN. Multiple destinations often share the same first several hops because they all use the same path through the private network before reaching the broader public internet or other networks. A key difference between traceroute and the routing table decision is that the routing table decision only shows one immediate next step whereas the traceroute shows the history of the path taken. For example, in the traceroute 8.8.8.8 screenshot above there are multiple different ip addresses, representing the history of hops taken whereas the IP route screenshot two screenshots above shows one IP address, the next hop.

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

