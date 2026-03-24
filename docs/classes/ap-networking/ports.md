# Ports and Protocols

## 1. Project Overview  

**Problem Statement:**  
Understand how the transport and application layers manage reliable communication and application sessions.

**Objectives:**  

- Compare reliable and unreliable transport protocols (TCP vs UDP)  
- Observe connection states and listening ports using system networking tools  
- Demonstrate application communication using TCP and UDP sockets  
- Analyze how higher layer protocols such as HTTP, HTTPS, and SSH operate 

**Success Criteria:**  

- Correctly identify listening and active ports using networking tools such as `ss -tn`  
- Successfully demonstrate communication using TCP and UDP with netcat  
- Accurately interpret connection states such as LISTEN and ESTAB  

## 2. Design & Planning 

### Transport Layer Protocols

Two primary protocols operate at the transport layer:

- **TCP (Transmission Control Protocol)** provides reliable, connection-oriented communication. It establishes a session using a three-way handshake and ensures data is delivered in order with acknowledgments and retransmissions.
- **UDP (User Datagram Protocol)** is connectionless and sends packets without acknowledgments or guaranteed delivery. It prioritizes speed and low overhead.

These protocols support different types of applications depending on whether reliability or speed is more important.

### Ports and Socket Communication

Applications communicate through **port numbers**, which allow multiple services to run on a single device with the same IP address. Ports enable a system to distinguish between different types of incoming traffic, such as web requests or DNS queries.

Key socket states include:

- **LISTEN** – The port is open and waiting for incoming connections.
- **ESTAB (Established)** – A TCP connection has been successfully formed between two endpoints.

### Application and Encryption Protocols

Other protocols depend on the transport layer to deliver their data.

Examples include:

- **HTTP** – Handles standard web requests and responses.
- **HTTPS** – Secures HTTP using TLS encryption.
- **DNS** – Resolves domain names into IP addresses.
- **SSH** – Provides secure remote access and command execution.

### Network Stack Behavior

Communication across the stack requires multiple layers to work together:

- **Layer 4 (Transport)** ensures data delivery between hosts.
- **Layer 5 (Session)** manages communication sessions between applications.
- **Layer 6 (Presentation)** handles encryption and formatting of data.
- **Layer 7 (Application)** defines how applications request and interpret information.

## 3. Technical Development 

### Transport Layer Reliability

**PC1 and PC2 IP Configuration:**

<img width="1906" height="957" alt="Screenshot 2026-03-03 at 1 22 26 PM" src="https://github.com/user-attachments/assets/26625a34-9107-4c0c-a70d-7bbfabf25ed2" />

<img width="1914" height="949" alt="Screenshot 2026-03-03 at 1 22 53 PM" src="https://github.com/user-attachments/assets/01e3769e-f0cc-4960-868e-0b654434b96a" />

The internet layer is responsible for the ping command, as it handles logical addressing and routing. Ping does not use TCP or UDP; instead, it uses the ICMP (Internet Control Message Protocol), which is a separate protocol within the IP suite. Consequently, a successful ping does not prove TCP reliability, as ICMP is a connectionless protocol that operates independently of the handshake and error-recovery mechanisms found in TCP

**PC1 ping PC2 Successful:**

<img width="299" height="225" alt="Screenshot 2026-03-03 at 1 27 56 PM" src="https://github.com/user-attachments/assets/6e1da7c8-b90f-46c7-93fa-0828825390d4" />

**PC1 to PC2 PDU Path:**

https://github.com/user-attachments/assets/0eca56c9-9a46-4b82-99e7-0942a2639ccb

| Feature | TCP | UDP | 
|---|---|---|
| Connection Setup | Yes, involves a 3 way handshake | No, it is connectionless |
| Sequence Numbers | Yes, used to reassemble data in the correct order | No, packets are treated individually |
| Acknowledgment | Yes, the receiver confirms receipt of data segments. | No, the sender never knows if data arrived | 
| Retransmission | Yes, missing segments are resent automatically | No, lost data is simply lost | 
| Header Complexity | Contains many control fields | Contains only essential info | 

### Comparing Transmission Types

A prediction is that TCP is connection oriented because it requires acknowledgement from both parties whereas UDP is connectionless because it doesn't require acknowledgement. Data sent over using UDP that is lost is just lost forever and not resent.

**View Listening TCP Ports(ss -tln):**

<img width="1842" height="344" alt="Image 3-6-26 at 8 19 AM" src="https://github.com/user-attachments/assets/dbd8b48d-846c-401a-82dc-a05e4608e7a8" />

**Sudo ss -tlpn screenshot:**

<img width="1892" height="306" alt="Image 3-6-26 at 8 20 AM" src="https://github.com/user-attachments/assets/66ecc646-92b1-4c5b-9bd7-c18c2a50a4b1" />

The process using port 22 is typically used for remote logins. If port 22 does not appear in your results, it suggests the SSH service is stopped. While a port exists as a logistical place available in the networking stack, a port is only listening when an active application has opened it to specifically monitor and accept incoming connection requests.

**View Listening UDP Ports (ss -uln):**

<img width="1880" height="322" alt="Image 3-6-26 at 8 22 AM" src="https://github.com/user-attachments/assets/636dc39e-2323-43e8-8a12-2e1c28d052c6" />

UDP sockets do not show a listen state, but above I can see ESTAB which represents that the connection is currently up.

**Terminal A Listener screenshot:**

Use the command `nc -l 5000` to have Terminal A be silently listening.

<img width="944" height="60" alt="Image 3-6-26 at 8 27 AM" src="https://github.com/user-attachments/assets/422681ee-5196-4ae3-b66b-4ff794e222b5" />

**Terminal C Shows New Port from Terminal A:**

The new port 0.0.0.0:5000 shows that Terminal C can now see the port from Terminal A.

<img width="1442" height="416" alt="Image 3-6-26 at 8 29 AM" src="https://github.com/user-attachments/assets/59a02792-166e-4f4d-a661-10ed24743b8e" />

**Successful Communication between Terminal B and A(tcp):**

Message from Terminal B:
<img width="666" height="88" alt="Image 3-6-26 at 8 32 AM" src="https://github.com/user-attachments/assets/be9c0b09-c04f-4e5c-b897-15dcffb77109" />

Terminal A Receieves Message:

<img width="524" height="80" alt="Image 3-6-26 at 8 32 AM (1)" src="https://github.com/user-attachments/assets/3e7ebd4c-43eb-40cd-8cb4-f4947504860c" />

**Observe ESTAB state from Terminal C:**

<img width="1428" height="206" alt="Image 3-6-26 at 8 34 AM" src="https://github.com/user-attachments/assets/c126aaa6-e3e4-42e8-8f76-3d860df6509f" />

**Start UDP Listener Terminal A:**

<img width="694" height="70" alt="Image 3-6-26 at 8 35 AM" src="https://github.com/user-attachments/assets/918b2ed0-21c0-4356-a5c1-c73cc28c7f25" />

**Successful Communication between Terminal B and A(udp):**

Message from Terminal B:
<img width="752" height="102" alt="Image 3-6-26 at 8 36 AM" src="https://github.com/user-attachments/assets/83a90265-2a04-4b08-bb0a-83605647247d" />

Terminal A Recieves Message:

<img width="618" height="94" alt="Image 3-6-26 at 8 37 AM" src="https://github.com/user-attachments/assets/b632a039-27be-40bf-976f-b19232351739" />

**Observe UDP State from Terminal C:**

<img width="1428" height="332" alt="Image 3-6-26 at 8 38 AM" src="https://github.com/user-attachments/assets/3427efd8-2ced-455b-9a37-4eebd72ebdd1" />

The evidence for the listen state is the output of ss -tln, which explicitly shows the listen status as it indicates the  listener is open and waiting for a connection. After connecting from Terminal B, the evidence for ESTAB appears in the ss -tn output, showing an ESTAB status demonstrates how the ports are connected. The primary change between the two commands is that ss -tln filters for listening sockets while ss -tn displays active connections ). This experiment proves TCP is connection-oriented because the state clearly transitions from a passive wait to a tracked connection between two different endpoints.

| Application | Protocol | Why | 
|---|---|---|
| Online Banking | TCP | Requires absolute reliability in data trasnfer when dealing with financial data |
| Zoom Call | UDP | Prioritizes low latency over reliability for live video calls |
| Netflix Streaming | TCP | Ensures the video file is transmitted entirely and safely | 
| File Download | TCP | Ensures files are transmitted entirely and safely | 
| DNS Query | UDP | Opimitzed for speed and low overhead | 

### OSI Layer 5

**HTTP Transaction:**

<img width="858" height="480" alt="Image 3-9-26 at 9 04 AM" src="https://github.com/user-attachments/assets/16e4115b-2f3d-40e2-a824-cc1e512c82bb" />

TCP is the protocol used with HTTP as it requires a three way handshake, ensuring all parties understand and recieve the data needed. The "200 OK" is the application layer to have the server confirm that the data is received.

**HTTPS Transaction:**

<img width="940" height="454" alt="Image 3-9-26 at 9 06 AM" src="https://github.com/user-attachments/assets/c04ccf11-1b94-4314-8f77-c63f9b37318b" />

The HTTPS is different as is requires signaling that the TLS (Transport Layer Security) is ready since it shows that this data sent needs extra encryption. This happens at the presentation layer to ensure that the data is secured before the confirmation at the application layer.

**TLS Handshake:**

<img width="1012" height="452" alt="Screenshot 2026-03-09 at 9 18 03 AM" src="https://github.com/user-attachments/assets/1483d332-1b4e-407e-aa83-da6fda133c59" />

<img width="782" height="815" alt="Screenshot 2026-03-09 at 9 18 16 AM" src="https://github.com/user-attachments/assets/422df5f8-8a35-4876-b171-dbd64f03feb2" />

**Observe Persistent Connection:**

<img width="2044" height="376" alt="Image 3-9-26 at 9 31 AM" src="https://github.com/user-attachments/assets/4e824aee-aafe-4e53-97a8-2b94de61e4a2" />

| Protocol | Layer | Purpose | 
|---|---|---|
| HTTP | 7(Application) | Provides the structure for web requests and responses, as seen in the 200 OK |
| HTTPS | 7(Application) | Acts as the secure version of HTTP |
| TLS | 6(Presentation) | Handles the encryption and decryption of data | 
| DNS | 7(Application) | Translates human-readable domain names into IP addresses | 
| TCP | 4(Transport) | Manages end-to-end communication and reliability | 

Layer 5 manages the communication state by establishing and maintaining dialogues between applications to ensure data streams remain organized during a session. Layer 6  is responsible for the formatting, compression, and encryption of the data, acting as a translator to ensure the receiving application can properly read and secure the information. Layer 7 governs specific application behavior and provides the interface for user services, such as interpreting an HTTP "200 OK" status or a DNS query. Layer 4 alone is insufficient because while it handles the reliable delivery of segments, it lacks the logic to understand the data's content and properly manage the data and convey the infromation.

### Application and Remote Access Protocols Across the Stack

**HTTP Stack Screenshot:**

<img width="727" height="148" alt="Screenshot 2026-03-11 at 12 43 37 PM" src="https://github.com/user-attachments/assets/db8d8aed-5c57-4cf8-8b7d-af1ac7c80985" />

**HTTPS Stack Screenshot:**

<img width="740" height="115" alt="Screenshot 2026-03-11 at 12 44 32 PM" src="https://github.com/user-attachments/assets/00195c9a-4879-45ea-88c5-9cc2926ddeb3" />

**nslookup Screenshot:**

<img width="388" height="253" alt="Screenshot 2026-03-11 at 12 48 16 PM" src="https://github.com/user-attachments/assets/0263f9e1-05c7-4018-80d1-c090ae4e50c1" />

DNS typically uses port 53 to handle name resolution requests between clients and servers. It primarily utilizes UDP because the small size of standard queries allows for rapid and low overhead communication. DNS does not require guaranteed delivery in most cases. If a packet is lost, the client application simply times out and retries the request, which is more efficient than managing TCP retransmissions. However, DNS will switch to TCP when the response data exceeds a certain limit.

**Connect via SSH Screenshot:**

<img width="908" height="524" alt="Screenshot 2026-03-11 at 12 49 49 PM" src="https://github.com/user-attachments/assets/4b947a22-29a2-46da-8b31-48e42bea23da" />

**SSH Connection ss -tn Screenshot:**

<img width="731" height="264" alt="Screenshot 2026-03-11 at 12 52 06 PM" src="https://github.com/user-attachments/assets/08bc1213-d9c4-41e5-bcab-05c25bc3a050" />

**Secure File Transer Screenshot:**

<img width="654" height="98" alt="Screenshot 2026-03-11 at 12 53 25 PM" src="https://github.com/user-attachments/assets/0cf0c5ab-234f-43e8-a368-01f611fa12b9" />

SSH requires TCP because remote administrative access demands absolute reliability and error free transmission. A single dropped or out of order packet could corrupt a command and crash a system. Encryption is not handled at Layer 3 because that layer is responsible only for routing packets between IP addresses, whereas encryption must be tied to specific application data to ensure security. Similarly, HTTP does not provide its own reliability because it is a application protocol designed to request content. If port numbers did not exist, a computer with a single IP address would be unable to distinguish between different incoming traffic types, making it impossible to run a web server and an SSH server simultaneously. It is essential to separate remote access from file transfer protocols  because they serve distinct administrative purposes, one for executing live system commands and the other for structured data management with each requiring different session behaviors.

### HTTP Status Codes

| Status Code Range | Meaning | Example Code | Explanation |
|---|---|---|---|
| 1xx | Informational responses that indicate the request has been received and the server is continuing the process. | 100 Continue | This code means the server has received the initial part of the request and the client can continue sending the rest of it. |
| 2xx | Successful responses that indicate the request was received, understood, and processed correctly. | 200 OK | This code means the request was successful and the server returned the requested resource or response. |
| 3xx | Redirection messages that tell the client that the resource has moved or another action must be taken to complete the request. | 301 Moved Permanently | This code means the requested resource has been permanently moved to a new URL, and the client should update future requests to use that new address. |
| 4xx | Client error responses that indicate something was wrong with the request sent by the client. | 404 Not Found | This code means the server could not find the requested resource, usually because the URL is incorrect or the page no longer exists. |
| 5xx | Server error responses that indicate the server failed to fulfill a valid request. | 500 Internal Server Error | This code means the server encountered an unexpected problem that prevented it from completing the request. |

| Status Code | Name | What It Means | When It Happens |
|---|---|---|---|
| 200 | OK | The request was successful and the server returned the requested content. | Happens when a webpage loads correctly and the server delivers the page or data without errors. |
| 301 | Moved Permanently | The requested resource has been permanently moved to a different URL. | Happens when a website changes its address and automatically redirects users to the new location. |
| 302 | Found | The resource is temporarily located at a different URL. | Happens when a page temporarily redirects users, such as during maintenance or temporary content changes. |
| 404 | Not Found | The server cannot find the requested resource. | Happens when a user tries to access a page that does not exist or the URL was typed incorrectly. |
| 500 | Internal Server Error | The server encountered an unexpected condition that prevented it from completing the request. | Happens when there is a bug, misconfiguration, or failure in the server's software. |

HTTP status codes are handled at the application layer because they describe the result of a web request between a client and a web server. The application layer is responsible for protocols like HTTP that define how web browsers and servers communicate and interpret messages. In contrast, the transport layer is only responsible for reliably delivering data between devices, not interpreting what the data means. Because status codes describe the meaning and outcome of a request, they belong in the application layer where the communication rules of web applications are defined.

### HTTPS Status Codes

**Observe HTTPS Screenshot:**

<img width="1218" height="584" alt="Image 3-23-26 at 1 30 PM" src="https://github.com/user-attachments/assets/084d866d-d014-4500-a651-4a876ae461d3" />

The HTTP code showing is 301, meaning the web domain was moved permanently. It is trying to redirect. All this happens during Layer 7, the application layer.

**Observe HTTPS Redirect Screenshot:**

<img width="1740" height="782" alt="Image 3-23-26 at 1 32 PM" src="https://github.com/user-attachments/assets/40190a4d-0e79-485f-8b68-e8273859ed4a" />

Compared to 301, 302 means that the web application is only temporarily removed. This 302 code might be used in circumstances where the origin web application needs to undergo some fixes or be developed more.

**Observe ss -tn Screenshot:**

<img width="1580" height="864" alt="Image 3-23-26 at 1 47 PM" src="https://github.com/user-attachments/assets/755fe98b-9c52-464e-a540-4337d494d99a" />

The transport protocol is carried out by TCP while the redirect is handled by HTTP as it is at the web layer. For both those, TLS provides security and encryption for all the communication.

## 4. Testing & Evaluation 

| Concept | Test Performed | Verification Result |
|-------|---------------|---------------------|
| TCP Listening Ports | Ran `ss -tln` and `ss -tlpn` | Verified that active services create listening sockets and wait for connection requests |
| UDP Listening Ports | Ran `ss -uln` | Confirmed UDP sockets appear without a traditional LISTEN state because UDP is connectionless |
| TCP Communication | `nc -l 5000` | Verified connection established and messages successfully transmitted |
| TCP Connection State | `ss -tn`  | Confirmed TCP transitions from LISTEN to ESTAB during active communication |
| TLS Encryption | Observed HTTPS transaction | Confirmed encryption occurs before HTTP communication |
| DNS Resolution | `nslookup` | Verified DNS converts domain names into IP addresses |
| SSH Remote Access | Established SSH session and monitored connection with `ss -tn` | Confirmed SSH uses TCP to maintain reliable encrypted remote sessions |

## 5. Reflection  

This project helped me understand how the transport layer enables reliable and unreliable communication between devices. By comparing TCP and UDP, I observed how different protocols prioritize either reliability or speed depending on the application’s needs. Using tools such as `ss -tn` allowed me to directly observe listening ports and connection states, which demonstrated how applications create sockets and wait for incoming connections. 

The experiments using netcat also demonstrated the practical differences between TCP and UDP communication. TCP connections maintained a tracked state and guaranteed delivery, while UDP allowed data to be sent without establishing a persistent connection. Observing these behaviors helped clarify why certain applications choose one protocol over the other. For example, applications requiring precise and reliable data transfer, such as file downloads or secure remote access, rely on TCP, while applications that prioritize speed and low latency, such as video streaming, often use UDP.

Overall, this project strengthened my understanding of how multiple layers of the network stack interact during communication.
