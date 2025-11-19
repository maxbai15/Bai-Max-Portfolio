# Physical Addressing and Logical Addressing

## 1. Project Overview  

**Problem Statement:**  
Understand how networks physically connect and communicate by exploring OSI Layers 1-3, building Ethernet cables, comparing network modes, designing topologies, and simulating a SOHO network.

**Objectives:**  

- Explore OSI Layer 1 and Layer 2 using Ubuntu commands
- Build and test Ethernet cables 
- Compare shared and bridged network modes and their IP addressing
- Design and label common network topologies (star, bus, ring, mesh, hybrid)
- Create and simulate a SOHO network with proper IP addressing and firewall configuration

**Success Criteria:**  

- Complete documentation of OSI Layers 1 & 2 exploration with labeled screenshots
- Successfully constructed and tested Ethernet cables with video demonstrations
- Clear comparison table showing Shared vs. Bridged mode IP addressing
- Toplogy diagrams with color-coded connections
- Functional SOHO network simulation with connectivity tests 

## 2. Design & Planning – OSI Layers and Network Design

### Understanding OSI Layers 1 and 2

The OSI Model organizes networking into seven layers, from physical hardware at the bottom to applications at the top. The first two layers form the foundation of all network communication.

**Layer 1: The Physical Layer**

The Physical Layer is the bottom layer of the OSI model and deals with hardware - the actual equipment that sends and receives electrical or optical signals. This layer is like the road system for data and includes:

- Cables (Ethernet, fiber optics, coaxial)
- Connectors and ports
- Wireless signals (Wi-Fi, Bluetooth)
- Network Interface Cards (NICs) or virtual interfaces

When a computer sends data, it turns it into bits (1s and 0s) and pushes them across these physical pathways.

**Layer 2: The Data Link Layer**

The Data Link Layer sits directly above the Physical Layer and is responsible for making sure that data travels safely and accurately between devices on the same local network. Here, data is packaged into units called frames. Each frame includes:

- The data being sent
- The source MAC address (the sender's unique hardware ID)
- The destination MAC address (the receiver's hardware ID)
- Error-checking information to detect damage during transmission

**How the Two Layers Work Together:**

Layer 1 provides the physical foundation, dealing with the actual hardware (cables, switches, NICs) and converting data into raw electrical, optical, or radio signals for transmission over the physical medium. It has no intelligence and simply moves the signal. Layer 2 operates on top of this functional Layer 1 connection, organizing the raw bits into frames and using MAC addresses for reliable, node-to-node data transfer on the local network segment. Thus, Layer 1 provides the path, while Layer 2 manages access to that path and ensures the data reaches the correct local destination intact, including error detection and control.

### Network Topologies

A network topology is the way that computers, devices, and other pieces of technology are arranged and connected within a network. It's like a map or blueprint that shows how data travels from one device to another. The topology you choose affects how well a network performs in terms of speed, cost, reliability, and scalability.

**Common Network Topologies:**

| Topology Type | Description | Common Use |
|---------------|-------------|------------|
| Star | One central switch or hub in the middle with all computers connecting to that central point | Office networks and home Wi-Fi routers |
| Bus | A single straight line ("backbone cable") with all computers branching off | Early Ethernet networks |
| Ring | Devices form a circle with connections between neighbors, data travels one way (or both in dual-ring) | Some legacy fiber networks and token ring systems |
| Mesh | Every device connects to multiple others, showing redundancy - if one path breaks, another can still carry data | Data centers and IoT or wireless mesh networks |
| Hybrid | Combine two or more types (for example, multiple Star networks connected in a Bus layout) | Large organizations with multiple departments or floors |

### SOHO Network Design

A SOHO (Small Office / Home Office) network is the kind of network setup most people use at home or in a small business. It connects multiple devices so they can share internet access, files, and other resources.

**Core SOHO Components:**

| Device | Function |
|--------|----------|
| Modem | Connects your network to your Internet Service Provider (ISP) |
| Router | Directs (routes) traffic between your local devices and the internet; assigns IP addresses |
| Switch | Expands the number of wired ports for computers and printers |
| Access Point (AP) | Provides Wi-Fi to laptops, tablets, and phones |
| Devices | Endpoints like computers, printers, and smart TVs that use the network |

**SOHO Network Diagram:**
![IMG_2469](https://github.com/user-attachments/assets/9ee018d8-c7a4-4e5c-b39d-4c922ea593ea)


## 3. Technical Development – Implementing Authentication & Security

### Understanding Physical Addressing

In this activity, sort different devices into four different network types: Personal Area Network(PAN), Local Area Network(LAN), Metropolitan Area Network(MAN), Wide Area Network(WAN).
Typically, in daily life, all four different networks are used. For the PAN, it is whenever you are connecting or using different personal device, like an iPhone. For LAN's, it is often
used in your workplaces or at school. MAN's are used to connect different network across city areas, like traffic signals. Finally, WAN's are used to connect the whole world together, like the internet. 
Each network scales up and connects with both larger and smaller ones.

**Step 1: Physical MAC Addressing**

**Screenshot of NIC(Ethernet Port, Main Controller Chip, PCIe Connector):**

![IMG_2482](https://github.com/user-attachments/assets/510825a5-1674-4937-b88c-b0633757ef2a)

**Screenshot of NIC(Ethernet Port, Main Controller Chip, PCIe Connector):**

![IMG_2483](https://github.com/user-attachments/assets/4cf6a726-5a92-4653-8ce1-f170b1bb68fa)

On a local network, MAC addresses provide a unique physical address, allowing data packets be sent to the correct destination. A MAC address is considered a physical address because it is a unique identifier hardcoded into a device's  
 NIC during manufacturing. Seeing a physical NIC shows you this address is tied directly to the hardware itself. 

**Step 2: Interpreting MAC Address**

**Screenshot MAC Address**

<img width="726" height="362" alt="Screenshot 2025-11-19 at 12 47 33 PM" src="https://github.com/user-attachments/assets/f3a12c0b-7d6e-4151-8461-2473a1dac421" />

Mac Address: ```fe:9c:d4:b2:67:53```
OUI: ```fe:9c:d4```

Vendor/company information not found, this can happen with virtualization vendors.

A physical NIC's MAC address comes from the manufacturer, while a virtual NIC's MAC is either generated by the hypervisor or is manually configured. Both use the same structure and are unique 
identifiers, but physical MACs are tied to hardware, while virtual MACs are software-based and don't need a physical vendor ID. A virtual NIC still needs a MAC address because it's essential for 
the device to communicate on a local network, where devices use MAC addresses to identify each other at the data link layer. 

**MAC Address Table Lookup**
| Full MAC Address | OUI(first 3 pairs) | Vendor/Company Name | Type of Vendor | Notes |
|--------------|--------------|---------------------|-------|----|
| F0:18:98:AA:BB:CC | F0:18:98 | Apple, Inc. | MA-L (Mac Address Block Large) | n/a |
| 3C:5A:B4:11:22:33 | 3C:5A:B4 | Google, Inc. | MA-L | n/a |
| 60:45:BD:12:34:56 | 60:45:BD | Microsoft | MA-L | n/a |
| A4:BA:DB:22:33:44 | A4:BA:DB | Dell Inc. | MA-L | n/a |
| 04:1A:04:55:66:77 | 04:1A:04 | WaveIP | MA-L | n/a |
| 00:50:56:AA:BB:CC | 00:50:56 | VMware, INC. | MA-L | n/a |
| 52:54:00:12:34:56 | 52:54:00 | Not Found | LLA (Locally Administered Addresses) | n/a |

A VM's MAC address typically reveals the manufacturer of the virtual network interface card (NIC), which corresponds to the hypervisor vendor (ex. VMware, Microsoft). 
It does not provide information about the specific underlying physical hardware model or its manufacturer, as the address is virtual and can often be manually changed or spoofed. 

**Step 3: Connecting Physical and Digital**

Mac Address: ```fe:9c:d4:b2:67:53```
OUI: ```fe:9c:d4```
Device Identifier: ```b2:67:53```

The Organizational Unique Identifier (OUI) is a 24-bit globally unique number that serves as the first half of a device's MAC address. It connects a Network Interface Card (NIC) to its 
manufacturer because the Institute of Electrical and Electronics Engineers (IEEE) assigns specific OUIs to individual vendors.
Manufacturers must use unique OUIs to ensure that every network-enabled device in the world has a universally unique MAC address, which is essential for network communication protocols 
(like Ethernet and Wi-Fi) to function correctly and avoid address conflicts.

Every NIC needs its own unique second half (the device identifier) because, combined with the manufacturer's unique first half (OUI), it creates a globally unique identifier for that 
specific hardware device. This mechanism, controlled by the IEEE and manufacturers, prevents two devices on the same LAN from having the same MAC address. Uniqueness is important for frame delivery
because network switches use MAC addresses to build forwarding tables and send data frames to the exact, intended recipient; duplicate addresses would cause confusion, leading to 
inconsistent communication.

The Data Link Layer (Layer 2) of the OSI model uses MAC addresses to facilitate communication between devices within the same local network segment. MAC addresses never leave the local network 
because they are designed for local identification, not routing across the broader internet. When a frame needs to move to a different network, a router strips off the source and 
destination MAC addresses and replaces them with the MAC addresses relevant to the next hop on the journey to the destination.


### Cable Constructing and Testing

This lab involved building and testing Ethernet cables using the T568B wiring standard at the Physical Layer (Layer 1) of the OSI Model. Professional technicians make their own cables to create precise lengths, verify quality, and save on cost.

**T568B Wire Order Standard:**

| Pin | Wire Color (T568B) | Pair Function |
|-----|-------------------|---------------|
| 1 | White/Orange | Transmit + |
| 2 | Orange | Transmit - |
| 3 | White/Green | Receive + |
| 4 | Blue | Unused / Power |
| 5 | White/Blue | Unused / Power |
| 6 | Green | Receive - |
| 7 | White/Brown | Unused |
| 8 | Brown | Unused |

**Stripping, Arranging, and Crimping**

**Step 1: Prepare the Cable**

Using the Solsop Pass Through RJ45 Crimp Tool Kit,measured approximately 12 inches of Cat5e cable, made a clean cut, and used the stripper to remove about one inch of the outer plastic jacket to expose four twisted pairs (eight wires total).

**Stripped Cable Screenshot:**
![IMG_2443](https://github.com/user-attachments/assets/2dff8c0b-fc2c-44d1-a5db-71797b720861)

**Step 2: Untwist and Arrange the Wires**

Carefully untwisted the four pairs and arranged them in the T568B color order: White/Orange, Orange, White/Green, Blue, White/Blue, Green, White/Brown, Brown. The wires were straightened until flat and parallel, then trimmed evenly to about ½ inch in length.

**Wires Aligned Screenshot:**
![IMG_2444](https://github.com/user-attachments/assets/e89b720a-0c58-43a8-bedd-66b29fdf51ad)


**Step 3: Insert Wires into RJ45 Connector**

The eight wires were carefully slid into the RJ45 connector while maintaining the correct color order. Each wire reached the front of the connector and was visible through the clear plastic, with the outer cable jacket extending slightly inside for strength.

**Wires in Connector Screenshot:**
![IMG_2447](https://github.com/user-attachments/assets/3436c222-6b79-4459-b7e0-a53104ecb77f)


**Step 4: Crimp the Connector**

The RJ45 connector was inserted into the crimping slot of the Solsop tool and the handles were squeezed firmly until a click was heard. The crimp tool pressed the metal contacts into the wires and cut off the excess ends. Both ends of the cable were completed using this process.

**Crimped Cable:**
![IMG_2445](https://github.com/user-attachments/assets/9ef6ca98-8fe0-44b1-a9a2-2c7de94fb05e)

**Stripping Demonstration Video:**
[Watch Stripping Demonstration Video](https://drive.google.com/file/d/1-tTdKACN1vwTsymJvSr26JxXThnXaDwM/view?usp=drive_link)

**Testing the Cable**

Both ends of the cable were plugged into the cable tester (main unit and remote unit). The indicator lights labeled 1-8 blinked in order, confirming that all eight wires were properly connected and aligned. The cable passed the test successfully.

**Cable Testing Demonstration Video:**
[Watch Stripping Demonstration Video](https://drive.google.com/file/d/1VIbKhOj6Mh3acULylwbgUWajKaUgGylk/view?usp=sharing)


**Cable Construction Reflection:**

The most challenging step in creating the cable was maintaining the correct wire order while inserting them into the RJ45 connector because the wires were very thin and kept moving out of alignment. Maintaining the correct wire order is critical for network reliability because even one incorrect wire will prevent the cable from passing the test and result in failed data transmission since the transmit and receive pairs must match on both ends. Building and testing cables connects directly to the Physical Layer (Layer 1) of the OSI Model because this layer deals with the actual hardware and physical signals that carry data, and the cable is the physical medium that those electrical signals travel through. In a real network, if a cable is built incorrectly but not tested, it could cause intermittent connection failures, slow data transfer speeds, or complete network outages that would be difficult to troubleshoot since the problem is hidden inside the cable. Labeling the cable and using these professional tools mirrored real-world industry practices because network technicians must clearly identify and organize cables in large installations, and use  standardized wiring schemes ensures compatibility across different manufacturers and systems.

### Lab 3: Exploring IP Addresses in Shared and Bridged Mode

This lab explored how network configuration settings affect IP addressing and how virtual machines connect to the internet by comparing Shared (NAT) and Bridged network modes.

**Part 1: Shared (NAT) Mode**

**Step 1: Confirm Shared Mode and Find Internal IP**

Command:
```bash
ip a
```

In Shared (NAT) mode, the VM uses a private IP address from a virtual subnet (for example, 192.168.64.x). The UTM software acts as a translator between the VM and the real internet.

**Internal IP Address:** 192.168.64.2/24

**Understanding the Output:**

| Term | Explanation |
|------|-------------|
| inet | This line shows the IPv4 address (192.168.64.6) |
| 192.168.64.6 | Internal (private) IP address assigned by the virtual network inside UTM (the NAT network) |
| /24 | Represents the subnet mask (255.255.255.0), meaning the first 24 bits identify the network |
| brd 192.168.64.255 | The broadcast address for this subnet |
| scope global dynamic enp0s1 | "Global" means this IP can reach outside the VM (through NAT), "dynamic" means it was assigned automatically (DHCP) |

**Shared Mode ip a Screenshot:**
<img width="668" height="334" alt="Screenshot 2025-11-14 195711" src="https://github.com/user-attachments/assets/309c7871-f152-4414-9afb-4a703f733707" />


**Step 2: Find External (Public) IP Address**

Using Firefox, navigated to https://whatismyipaddress.com and recorded the external IP address.

**External IP Address:** 173.95.44.210

This external (public) IP address represents how the rest of the internet sees the connection, and it's different from the internal IP.

**Shared Mode External IP Screenshot:**
<img width="669" height="329" alt="Screenshot 2025-11-14 195758" src="https://github.com/user-attachments/assets/643c44ad-4215-4094-99f6-4dbac5c3a998" />

**Part 2: Bridged Mode**

**Step 1: Switch to Bridged Mode**

In UTM, the network mode was changed from Shared (NAT) to Bridged (Advanced), and the VM was restarted.

**Step 2: Verify Bridged Mode and Find Internal IP**

Command:
```bash
ip a
```

**New Internal IP Address:** 10.24.0.168

This new address comes directly from the local network's router. The VM is now a separate device on the same network as the Mac.

**Bridged Mode ip a Screenshot:**
<img width="668" height="290" alt="Screenshot 2025-11-14 195834" src="https://github.com/user-attachments/assets/1fd70d50-dfd1-47c1-a80d-7b9e8ea7338b" />


**Step 3: Find External IP in Bridged Mode**

Using Firefox again, navigated to https://whatismyipaddress.com.

**External IP in Bridged Mode:** 173.95.44.210 (stayed the same)

**Bridged Mode External IP Screenshot:**
<img width="662" height="403" alt="Screenshot 2025-11-14 195848" src="https://github.com/user-attachments/assets/f6537e5f-9a03-4e1f-8baf-e9ecb94a3b9e" />


**Shared and Bridged Mode Reflection:**

In Shared mode, the internal and external IP addresses are different. The internal IP address that starts with 192.168.64.2 belongs to the local network while the IP address starting with 173.95.44.210 belongs to the internet. The virtual machine uses NAT when connecting to the internet to conserve IP addresses as it allows multiple private IPs to connect to the same public internet IP. Being in shared mode makes it easier to connect multiple VMs on one computer because they will all share the same private IP that is connected to the internet. The internal IP address changed from 192.168.64.2 in Shared mode to 10.24.0.168 in Bridged mode because the VM was now getting its IP directly from the local network router instead of from UTM's virtual network. The external IP address remained the same at 173.95.44.210 because both modes ultimately connect to the internet through the same physical network connection. In Bridged mode, the virtual machine acts more like a separate computer on the network rather than a computer behind another device because it gets its own IP address directly from the router just like any other device. An organization might choose Bridged mode instead of Shared (NAT) mode when they need VMs to be directly accessible from other devices on the network or when they're running servers that need to be reached from outside. Security or management challenges that could come with using Bridged mode include the VM being more exposed to network attacks since it's directly on the network, and IT administrators need to manage more IP addresses and ensure each VM is properly configured with firewalls.

**Comparison Table:**

| Mode | Internal (Private) IP | External (Public) IP | Notes |
|------|----------------------|---------------------|-------|
| Shared (NAT) | 192.168.64.2 | 173.95.44.210 | VM hidden behind Mac's connection |
| Bridged | 10.24.0.168 | 173.95.44.210 | VM appears as separate device |

### Network Topologies

This activity involved creating labeled drawings for five common network topologies, each showing how devices connect and communicate.

**Star Topology:**

One central switch or hub in the middle with all computers connecting to that central point. Commonly used in office networks and home Wi-Fi routers.

**Star Topology Diagram:**
![IMG_2470](https://github.com/user-attachments/assets/850f01bd-843e-484a-abd7-064c84ed7179)


**Bus Topology:**

A single straight line ("backbone cable") with all computers branching off. This was common in early Ethernet networks but is now outdated.

**Bus Topology Diagram:**
![IMG_2471](https://github.com/user-attachments/assets/d58ff331-dee6-48e7-8cef-265150ef91db)


**Ring Topology:**

Devices form a circle with connections between neighbors, and data travels one way (or both in dual-ring). Used in some legacy fiber networks and token ring systems.

**Ring Topology Diagram:**
![IMG_2472](https://github.com/user-attachments/assets/0868ea49-7da6-41c0-9ee8-e346b5be5ea9)


**Mesh Topology:**

Every device connects to multiple others, showing redundancy. If one path breaks, another can still carry data. Commonly used in data centers and IoT or wireless mesh networks.

**Mesh Topology Diagram:**
![IMG_2473](https://github.com/user-attachments/assets/7645e649-7fae-4e57-9244-52e62cb2a3ee)


**Hybrid Topology:**

Combines two or more types. Used in large organizations with multiple departments or floors.

**Hybrid Topology Diagram:**
![IMG_2474](https://github.com/user-attachments/assets/cd5db95c-a778-4148-8153-2e3abf620790)


**Topology Reflection:**

Star topology would be easiest to set up for a small business because it only requires one central switch and individual cables to each device, making installation and troubleshooting straightforward since each connection is independent. Mesh topology would be the most reliable if one connection fails because every device has multiple paths to reach other devices, so if one link goes down the data can automatically reroute through another path. Mesh topology would also be most expensive to implement because it requires the most cables and network interfaces since every device must connect to multiple other devices, dramatically increasing hardware costs. The school uses a hybrid topology, most likely combining star topologies on each floor (with switches connecting classroom computers) that are then connected together using a bus or ring backbone between floors, because this approach provides both the simplicity of star topology locally and the scalability needed for a large building. The physical layout of a topology affects speed and reliability because the number of hops data must make impacts latency , and the redundancy of connections determines fault tolerance , with more direct connections generally improving speed while more redundant paths improve reliability but increase complexity and cost.

### Building and Testing a SOHO Network

This lab involved designing a realistic SOHO network and simulating it using Ubuntu virtual machines to test connectivity and understand how devices communicate.

**Step 1: SOHO Network Design**

The network was designed for a small office with eight devices including 2 Ubuntu computers, 1 printer, 1 smartphone, 1 router, 1 switch, 1 access point, and 1 NAS device. The diagram shows clear labels for each device, IP addresses, and color-coded lines for wired (solid) and wireless (dashed) connections.

**SOHO Network Diagram:**
![IMG_2469](https://github.com/user-attachments/assets/9ee018d8-c7a4-4e5c-b39d-4c922ea593ea)


**Step 2: Simulate and Test in Ubuntu**

**Set Up and Identify IP Addresses**

Both partner VMs were set to Bridged mode and IP addresses were identified using `ip a`.

**IP Addresses:**

- Computer A: 10.12.26.47
- Computer B: 10.12.26.129

**IP -a Screenshot:**
<img width="727" height="276" alt="Screenshot 2025-11-14 at 8 22 53 AM" src="https://github.com/user-attachments/assets/e638a27c-98b7-4185-b5e0-b4a9c0c5e632" />


**Test Connectivity Between Computers**

Command:
```bash
ping 10.12.26.129
```

**Successful Ping Screenshot(mine and partners):**
<img width="700" height="219" alt="Screenshot 2025-11-14 at 8 23 08 AM" src="https://github.com/user-attachments/assets/489e4ef5-2f00-4b65-8276-f5297d52433d" />
<img width="701" height="437" alt="Screenshot 2025-11-14 at 8 22 37 AM" src="https://github.com/user-attachments/assets/937337ec-ed8f-4f8d-b2a0-6c88c23e091a" />


**Step 3: Network Diagnostic Commands**

**ARP Table:**
```bash
arp -a
```


**Routing Table:**
```bash
netstat -r
```
**ARP -a and Neststat -r Screenshot:**
<img width="743" height="368" alt="Screenshot 2025-11-14 at 8 40 09 AM" src="https://github.com/user-attachments/assets/d57a2d03-a8d4-4af2-8fa1-c9ebb8979c95" />

**Traceroute:**
```bash
sudo traceroute 8.8.8.8
```

Displays every "hop" packets take to reach Google's DNS server, visualizing how data travels through routers across different networks.

**Traceroute Screenshot:**
<img width="735" height="652" alt="Screenshot 2025-11-14 at 8 29 35 AM" src="https://github.com/user-attachments/assets/68122e16-4f38-467e-aee6-c7a7b57f6c23" />


These commands reveal how the SOHO network communicates by showing the MAC addresses of local devices (arp), the routing decisions being made (netstat -r), and the path data takes to reach external networks (traceroute). ARP relates to Layer 2 by mapping MAC addresses on the local network, while netstat and traceroute show Layer 3 activity with routing across multiple devices.

**Step 4: Firewall Configuration**

Command:
```bash
sudo ufw status
sudo ufw enable
```

The firewall was enabled to act as a security gate for the network, blocking unwanted connections and allowing safe traffic. Firewalls operate mainly at OSI Layers 3 and 4, filtering packets based on rules.
Enabling a firewall protects the system by only allowing trusted data to pass through, which prevents unauthorized access and potential security threats from reaching the computer.


**Active Firewall Screenshot:**
<img width="561" height="138" alt="Screenshot 2025-11-14 201848" src="https://github.com/user-attachments/assets/f51f8fd4-f14e-4f78-ae5b-d3d446e3a94b" />


**Step 5: Simple Web Server (Application Layer)**

**Computer B (Server):**
```bash
python3 -m http.server 8080
```

**Computer A (Client):**
Opened Firefox and navigated to `http://10.12.26.129:8080`

The browser displayed a list of files hosted by Computer A, demonstrating the Application Layer by showing how one device can serve files to another over HTTP, which is the same protocol that real websites use.

**Web Server Connection Screenshot:**
<img width="878" height="876" alt="Screenshot 2025-11-14 at 8 31 47 AM" src="https://github.com/user-attachments/assets/2670b703-0fe2-4b39-a500-cccda4c7a1b0" />



## 4. Testing & Evaluation – Network Verification

All networking concepts were tested and verified through practical lab activities.

| Concept | Test Performed | Verification Result |
|---------|---------------|---------------------|
| OSI Layer 1 | `ethtool enp0s1` | Confirmed physical connection speed, duplex mode, and link status |
| OSI Layer 2 | `ip link show`, `arp -n` | Identified MAC address and ARP table showing local device mapping |
| Network Traffic | `tcpdump -c 5` | Captured live packets showing source/destination MAC addresses |
| Cable Construction | Cable tester with indicator lights | All 8 wires passed test in correct order (T568B standard) |
| Shared Mode IP | `ip a` and whatismyipaddress.com | Internal: 192.168.64.2, External: 173.95.44.210 |
| Bridged Mode IP | `ip a` and whatismyipaddress.com | Internal: 10.24.0.168, External: 173.95.44.210 |
| VM Connectivity | `ping` between partner VMs | Successful replies with <1ms latency, 0% packet loss |
| Routing | `netstat -r`, `traceroute google.com` | Displayed routing table and multi-hop path to external servers |
| Firewall | `sudo ufw status` | Confirmed firewall active and protecting system |
| Application Layer | Python http.server | Successfully served files between VMs over HTTP |

## 5. Reflection  

Through these networking labs, I gained comprehensive hands on experience with the foundational layers of network communication and how physical infrastructure connects to logical addressing and data flow. The OSI Layers 1 and 2 exploration taught me that networking starts with physical hardware and MAC addresses before any IP addressing comes into play. Building and testing Ethernet cables showed me why proper Physical Layer construction is critical because even one misplaced wire completely breaks connectivity. The Shared versus Bridged mode comparison clarified how network address translation works and why organizations use NAT to conserve IPv4 addresses while adding security through network isolation. Shared mode hides the VM behind the host computer's IP address, which is safer but less flexible, while Bridged mode makes the VM appear as its own device with direct network access, which is more exposed but enables server functionality. 

Additionally, creating topology diagrams for star, bus, ring, mesh, and hybrid networks illustrated that network design involves tradeoffs between cost, reliability, and scalability. For example, star topology is simple and cheap but has a single point of failure at the central switch, while mesh topology is extremely reliable with redundant paths but expensive due to all the extra cabling and ports required. 

The SOHO network simulation brought everything together by requiring me to design a complete network with proper IP addressing, then test it using actual Ubuntu commands. Pinging between partner VMs proved Layer 3 connectivity, examining ARP tables showed Layer 2 MAC address mapping, running traceroute demonstrated how data crosses multiple networks to reach the internet, and enabling the firewall added essential security filtering. The Python web server activity was particularly interesting because it showed me how Application Layer protocols like HTTP depend entirely on other layers and the result of connectivity.
