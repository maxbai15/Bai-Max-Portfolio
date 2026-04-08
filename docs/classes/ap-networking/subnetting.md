# Subnetting and Maintaining Multiple LANs

## 1. Project Overview  

**Problem Statement:**  
Understand how subnetting determines communication within and between networks, and how multiple LANs can be designed and maintained.

**Objectives:**  

- Analyze how subnet masks determine whether devices are on the same network  
- Test communication between devices with different IP and subnet configurations  
- Design a multi LAN network with separate departments 
- Diagnose and resolve connectivity issues within a network  

**Success Criteria:**  

- Correctly determine whether devices are on the same subnet based on IP and subnet mask  
- Successfully demonstrate communication within the same subnet 
- Design a functional LAN network 
- Identify and fix network issues in a broken network  

## 2. Design & Planning 

### IP Addressing and Subnet Masks

Every device on a network has an IP address paired with a subnet mask. The subnet mask determines which portion of the IP address represents the network and which portion represents the host. Devices are on the same network if the network portion of their IP addresses matches. Devices are on different networks if the network portion differs. The subnet mask defines how many octets must match for communication to occur directly.  

### Subnetting 

Subnetting is based on binary, where subnet masks divide networks into smaller segments. This allows:

- Separation of devices into different networks  
- Improved organization and scalability  
- Control over which devices can communicate directly  


### Network Design for Multiple LANs

To support multiple departments, a network must be segmented into separate LANs:

- Each department is placed on its own subnet and switch  
- A central router connects the different LANs  
- This design improves security and scalability by isolating traffic  


## 3. Technical Development 

### Subnetting Challenges

<img width="749" height="196" alt="Screenshot 2026-03-24 at 2 35 30 PM" src="https://github.com/user-attachments/assets/32353a97-31b9-4fe9-b336-8e8340c2b6a4" />

Two IP addresses with the subnet mask 255.0.0.0 must have the same first octect to be on the same network.

<img width="751" height="212" alt="Screenshot 2026-03-24 at 2 35 39 PM" src="https://github.com/user-attachments/assets/4344c250-56e6-41f3-9a4c-780895bb452b" />

Two IP addresses with the subnet mask 255.255.0.0 must have the same first two octects to be on the same network.

<img width="757" height="182" alt="Screenshot 2026-03-24 at 2 35 51 PM" src="https://github.com/user-attachments/assets/11785f72-9a77-4e2f-9fe8-e9e9b10f11f2" />

The structure of the other IP addresses on the network would be 210.58.24.xxx, with the ending octect being from 1-255.

<img width="714" height="102" alt="Screenshot 2026-03-24 at 2 41 06 PM" src="https://github.com/user-attachments/assets/4ce85ff9-8fdc-42ab-b4b6-02db3e1501e8" />

The pattern is these numbers are based in binary where the bits are added from right to left.

### IPv4 Subnetting Mask

**IP Configuration:**

PC0 - 192.168.1.10, 255.255.255.0
PC1 - 192.168.1.25, 255.255.255.0
PC2 - 192.168.2.10, 255.255.255.0

**PC0 ping PC1 and PC2:**

<img width="305" height="272" alt="Screenshot 2026-03-26 at 8 16 34 AM" src="https://github.com/user-attachments/assets/2f9c9db1-f434-45eb-afce-f2a42276609c" />

Here, the ping to PC1 is successful since the subnet mask 255.255.255.0 means that the first 3 octets must be the same to be on the same network, and for PC0 and PC1 they are. In comparison, PC0 to PC2 fails since the third octect is not the same.

**PC0 ping PC2 diff subnet mask:**

Changed PC2 subnet mask to 255.255.0.0

<img width="302" height="138" alt="Screenshot 2026-03-26 at 8 18 32 AM" src="https://github.com/user-attachments/assets/94a9bce6-518e-4b8d-8ffe-db481df3c7b9" />

Changing only the cubnet mask of PC2 doesn't change much since the subnet mask of PC0 is still 255.255.255.0.

**Scenario A:**

Ping PC1 and PC2 from PC0 against whil all subnet masks are 255.0.0.0

<img width="283" height="294" alt="Screenshot 2026-03-26 at 8 20 01 AM" src="https://github.com/user-attachments/assets/8b766a84-14f6-4381-a9bc-3f9d2bac6e40" />

Changing all subnet masks to 255.0.0.0 allows for all the PC's to be on the same network since the first octect of the IPv4 is the same for all PC's. 

**Scenario B:**

PC0 - 172.16.1.10, 255.255.0.0
PC1 - 172.16.2.20, 255.255.0.0

<img width="292" height="154" alt="Screenshot 2026-03-26 at 8 21 34 AM" src="https://github.com/user-attachments/assets/658f239f-2f16-4f4a-bcee-32126cda0c97" />

Both PC's are on the same network since the subnet mask shows that the first 2 octects of the IPv4 have to be the same to be in the same network.

**Scenario C:**

**Look Similar but Different Network:**

PC0 - 172.16.1.10, 255.255.255.0
PC1 - 172.16.2.10, 255.255.255.0

<img width="357" height="135" alt="Screenshot 2026-03-26 at 8 29 43 AM" src="https://github.com/user-attachments/assets/30c6eace-cedb-4b0a-aac0-ec9d2acafa26" />

Here the two IP addresses look similar with only one number differing, but that number is important since the subnet mask shows that the first 3 octects must be the same to be on the same network. Since the 3rd octect differs, PC0 and PC1 are not on the same network.

**Look Different but Same Network:**

PC0 - 172.56.29.1, 255.0.0.0
PC1 - 172.16.2.20, 255.0.0.0

<img width="288" height="156" alt="Screenshot 2026-03-26 at 8 31 15 AM" src="https://github.com/user-attachments/assets/cf2fe022-7c07-4610-9bff-27997db86b53" />

The two PC's have IPv4 addresses that look different except the 1st octect, but based on the subnet mask, only the 1st octect has to be the same for the PC's to be on the same network.

### Designing A Real Network

Scenario A: Design a network for a company with two departments that must remain seperate.

**Devices before Connections:**

<img width="1518" height="516" alt="Screenshot 2026-03-27 at 9 16 19 AM (1)" src="https://github.com/user-attachments/assets/1ce73d5c-7596-4ab6-b53d-14dfac46bfc3" />

Above is the devices utilized before connections. It is split into two different departments, accounting and marketing. Each department has its own switch and pcs, but they all connect to a central router.

**Devices Connected:**

<img width="1204" height="473" alt="Screenshot 2026-03-27 at 9 24 56 AM" src="https://github.com/user-attachments/assets/f3a1d2e4-ef03-4a51-8eef-9a931283c223" />

Above shows the good connection between all devices, except wireless for now.

**Final Design:**

<img width="1221" height="479" alt="Screenshot 2026-03-27 at 9 50 35 AM" src="https://github.com/user-attachments/assets/906ac783-05bc-49ad-96d3-67137e9ee016" />

In the final design, a wireless laptop and router were added to allow workers to work outside of the office. In the design there is two different switches for each department, so that they can have seprate networks for scalability and security. Each department has PC's that workers use connected to their respective switches. Ultimately, both switches connect to a central router that is connected to the main server that houses the information for the entire company. I chose a client-server model because it allows for centralized security around the main server, where all the information is stored.

### Diagnosing Broken Network

**Ping Failure:**

<img width="885" height="705" alt="Screenshot 2026-03-31 at 12 41 12 PM" src="https://github.com/user-attachments/assets/963b530f-c7a2-41c3-a5a6-8da9578dd1d9" />

First, pinging the IP address across the network tests to see if connectivity is up. Since the ping fails, there is a failed connection somewhere in the network.

**Checking Router Configuration:**

<img width="813" height="205" alt="Screenshot 2026-03-31 at 12 42 26 PM" src="https://github.com/user-attachments/assets/77946dcc-6fc1-4d79-b49f-25f69ef32be0" />

Checking the configuration of the router, it shows that the Gigabit connection 0/0/1 is down. This means that the connection problem is with the router and the second switch as the port isn't up.

**Solution:**

<img width="878" height="709" alt="Screenshot 2026-03-31 at 12 43 46 PM" src="https://github.com/user-attachments/assets/0878739b-0f31-42ee-8e09-2569a8a66233" />

The solution is a simple fix: configure the status of gigabit port 1 on the router to an up state. To do this enter the cli for the router and type the commands `enable` then `config t` to enter global configuration mode. After entering global configuration mode, enter port 1 by typing `int gi0/1` and then the command `no shut` to make the status of port 1 UP.

**Working Network:**

<img width="932" height="445" alt="Screenshot 2026-03-31 at 12 44 14 PM" src="https://github.com/user-attachments/assets/b4fbdb74-4a39-43fa-ac14-a5469bea4fcb" />

To diagnose the breakdown in the network, the first step is to test if there is really a breakdown. To do this, simply ping two different devices across the network to see if they are able to reach each other. After figuring out the devices weren't able to reach each other, the next step was to check the IP configuration of the devices, switches, and router. Checking the router last, the port 1 on the router was down, meaning there was no connectivity to switch 2 and the devices on that side. As a result of this, the fix was to simply go into the cli of router 1 and set the status of port 1 to active.

## 4. Testing & Evaluation 

| Concept | Test Performed | Verification Result |
|-------|---------------|---------------------|
| Same Subnet | Compared IPs with different subnet masks (255.0.0.0, 255.255.0.0, 255.255.255.0) | Verified that required matching octets determine whether devices are on the same network |
| Same Subnet Communication | Pinged PC1 from PC0 with matching subnet (192.168.1.x /24) | Verified successful communication when network portion matches |
| Different Subnet Communication | Pinged PC2 from PC0 with different subnet (192.168.2.x /24) | Verified communication fails when devices are on different networks without a router |
| Subnet Mask Change | Changed subnet mask of one device only | Confirmed communication still fails if both devices do not share the same network mask |
| Connectivity Testing | Used ping to test network communication | Identified failure in connectivity between devices |
| Router Troubleshooting | Checked router interface status | Found disabled interface causing network failure |
| Network Fix | Enabled port on router using `no shut` | Verified full network connectivity restored after interface activation |


## 5. Reflection  

This project helped me understand how subnetting controls communication within and between networks. By experimenting with different subnet masks, I learned how the network portion of an IP address determines whether devices can communicate directly. I observed that even small changes in an IP address or subnet mask can completely change whether two devices are considered part of the same network. 

Designing a network with multiple LANs also showed how subnetting is used in real world scenarios to separate departments for better organization and security. By connecting different LANs through a router, I saw how communication between networks depends entirely on proper routing. This helped me understand why routers are essential in larger networks and how they allow multiple smaller networks to function as part of a larger system.

The troubleshooting portion of the project was  useful because it demonstrated how to diagnose network problems. By starting with a simple ping test and then checking configurations, I was able to identify that a router interface was down. Fixing the issue by enabling the interface showed how small configuration errors can cause major connectivity problems. Overall, this project strengthened my understanding of subnetting and network design.
