# Why Can’t These Two Computers Talk to Each Other?

## Digital Portfolio Evidence #1: Physical Layer Check (Layer 1)

**Screenshot of ip a for both VM's**

<img width="740" height="303" alt="Image 11-18-25 at 10 53 AM" src="https://github.com/user-attachments/assets/cc9ff34c-f7de-46bb-9fef-af39f570f810" />
<img width="735" height="272" alt="Image 11-18-25 at 11 06 AM" src="https://github.com/user-attachments/assets/c7aac8c3-70c0-4564-8c2b-3864a5fadc2d" />


The physical layer appears to be functioning correctly. Both virtual machines show the wired interface `enp0s1` in `state UP` with valid MAC addresses. The Ethernet cable is properly connected between both Mac desktops, confirming that Layer 1 connectivity is established.


## Digital Portfolio Evidence #2: Data Link Layer Check (Layer 2)

**Screenshot of attempted ping**

<img width="693" height="293" alt="Image 11-18-25 at 11 07 AM" src="https://github.com/user-attachments/assets/ce607245-da11-464e-916d-1f426519f117" />
<img width="681" height="76" alt="Image 11-18-25 at 11 06 AM copy" src="https://github.com/user-attachments/assets/ea449ab6-a4b0-45d2-959b-6a4da14ae778" />


Layer 2 shows evidence of failure. The ping attempt resulted in "Destination Host Unreachable," which indicates that the system cannot resolve the partner's MAC address through ARP, meaning the two VMs are not on the same broadcast domain despite the physical connection.


## Digital Portfolio Evidence #3: Network Layer Check (Layer 3)

**Screenshot of ip addresses for VM's**

<img width="646" height="321" alt="Image 11-18-25 at 11 31 AM" src="https://github.com/user-attachments/assets/597a81c9-97e6-4a9a-8bb6-32f4f383e5e9" />
<img width="826" height="262" alt="Image 11-18-25 at 11 31 AM 2" src="https://github.com/user-attachments/assets/d30904fe-176e-4ed7-842a-ef39ffd852bf" />


Both virtual machines display identical or similar IP addresses (10.12.xx.xx), which initially suggests they might be on the same subnet. However, this is misleading since even though the IP addresses appear to be in the same subnet, they are actually on completely separate private networks that cannot communicate with each other. Layer 3 addressing cannot function properly because the VMs are fundamentally isolated at the data link layer and are not actually on the same subnet.


## Digital Portfolio Evidence #4: Ping Failure Confirmation

**Screenshot of Ping Failure Confirmation**

<img width="645" height="205" alt="Image 11-18-25 at 11 37 AM" src="https://github.com/user-attachments/assets/46a6acf0-4611-4c3a-ae66-d5d8a90b3bf4" />
<img width="612" height="240" alt="Image 11-18-25 at 11 37 AM 2" src="https://github.com/user-attachments/assets/0239aafa-840b-47a3-b163-4c1499f10a7d" />


The ping failure occurs at Layer 3 (Network Layer) and is a result of Layer 2 not working properly. While Layer 1 is physically functional, the virtual networking architecture prevents Layer 2 broadcast traffic from reaching between the two VMs, and Layer 3 routing cannot occur because the VMs exist in separate virtual networks with no route to find the MAC address of the other.


## Reflection Paragraph

The two computers could not communicate despite being connected with a working Ethernet cable because they weren't on the same virtual network. Although Layer 1 was functioning correctly with the cable properly connected and interfaces showing "state UP," the failure occurred primarily at Layer 2, resulting  Layer 3 failure too. Though both VMs had IP addresses in the same apparent subnet (10.12.xx.xx), they were actually on completely different private networks with no Layer 2 broadcast domain connection, resulting in no Layer 3 routing path between them. UTM prevents direct communication in host-only mode to maintain security and isolation between virtual machines. To allow communication, we would need to configure both VMs to use bridged networking mode, allowing MAC addresses to locate each other and result in a routing path between the two VM's. In a real SOHO network, routers provide Layer 3 routing between different subnets and assign devices to the same network, while switches create a Layer 2 broadcast domain, ensuring that devices on the same subnet can discover each other's MAC addresses and communicate directly.
