# Transport Layer - OSI Model Layer 4

- Transport-layer protocols provide logical communication between processes running on different hosts
- Network-layer protocols provide logical communication between hosts

## UDP

### Services Provided by UDP

- Process-to-process data delivery
- Segment integrity checking by including error-detection fields in the segment's header
- Multiplexing/demultiplexing is as simple as specifying the host and destination ports in the headers of a UDP segment
- When a sender specifies the source port it acts as a "return address"
- UDP does not provide flow control and if receive buffer at the receiver overflows (segments arrive faster than the application reads) then packet loss occurs at layer 4

### Segment Structure

#### 1. Source Port (16 bits)

- 16 bits for the source port (0 to 65535)

#### 2. Destination Port (16 bits)

- 16 bits for the destination port (0 to 65535)

#### 3. Length (16 bits)

- 16 bits for the total length of the segment (header + data) in bytes
- Minimum value is 8 bytes (just the header)
- Theoretical maximum is 65535 bytes but usually limited by the MTU of the network

#### 4. Checksum (16 bits)

- 16 bits for the checksum which is used for error-checking the header and data to ensure integrity
- The sender calculates a checksum over the segment's bits
- The receiver does the same maths, if the numbers don't match, the segment was corrupted in transit and typically discarded

#### 5. Payload

- A payload with a theoretical maximum size of 65527 (65535 - 8 header bytes)

## TCP

### Overview

#### Multiplexing and Demultiplexing

- Refers to extending the host-to-host delivery service to a process-to-process delivery service for applications running on the hosts
- The transport-layer in the receiving host doesn't deliver data directly to the process but to an intermediary socket (the OS's networking API)
- Each transport-layer segment has a set of fields in the segment for this purpose
- Multiplexing and demultiplexing also happen at other layers of the OSI model whenever a protocol in the layer is used by other protocols higher up

##### Demultiplexing

- In a receiving host, the transport layer examines the fields a transport-layer segment in order to identify the receiving socket and then directs the segment to that socket
- Ths job of delivering the data in a transport-layer segment to the correct socket is called demultiplexing

##### Multiplexing

- The job of gathering data chunks passed to the transport-layer at the source host, encapsulating each chunk with header information to create segments, and passing the segments to the network layer is called multiplexing

#### Sockets and Port Numbers

- Sockets on end hosts must be uniquely identified in order for multiplexing and demultiplexing to work at the transport-level
- The unique identifiers used are the source port number field and the destination port number field in a transport-layer segment
- Each port is an unsigned 16-bit number (0 to 65535)
- Port numbers ranging from 0 to 1023 are well-known port numbers and are restricted

### Services Provided by TCP

- Process-to-process data delivery
- Reliable data transfer ensuring data is correct and in order
- Congestion control (a service provided not so much to the application but to the internet as a whole)
- Flow control (regulating the rate at which data is transferred to help the receiver not be overloaded)

#### Reliable Data Transfer

- Pipelining is used to avoid poor performance of stop-and-wait protocols and improve the utilization of the sender
- The sender can start sending any data it has whilst some of it is already in transit instead of waiting
- Pipelining allows the sender to send multiple packets without waiting for acknowledgements
- The introduction of pipelining has the following consequences (in comparison with the protocol developed in [rdt](./rdt)):
  - The range of sequence numbers must be increased since each in-transit packet must have a unique sequence number
  - The sender and receiver sides may have to buffer more than one packet (at minimum the sender has to buffer packets that have not yet been ack'd)
  - The range of seq. numbers and buffering requirements will depend on how the protocol responds to lost, corrupted or overly delayed packets
    - 2 basic approaches to pipelined error recovery can be identified: Go-Back-N and Selective Repeat

##### TCP Implementation

- TCP uses a single retransmission timer
- When data is passed to TCP, a timer is started if there isn't already one running
- The timeout is associated with the oldest unacknowledged packet
- When the timeout occurs, TCP retransmits the oldest unacknowledged segment with the smallest sequence number
- When TCP retransmits it doubles the timeout interval (from what the previous value was)
- The timer expiration is usually caused by congestion in the network and in times of congestion if the sender continues to retransmit packets persistently the congestion may get worse
- TCP uses cumulative acknowlegdements so when a new ack. number is received, the value of the sequence number of the oldest unacknowledged byte is updated and the timer restarted (assuming its bigger than what was known)
- Timeout-triggered retransmissions increase end-to-end delay due to the sender withholding the segment
- TCP functions like Go-Back-N but instead of resending all unacknowledged packets on timeout it only retransmits the oldest unacknoweldged packet
- TCP also relies on duplicate ACKs, if three duplicate ACKs are received then the oldest unacknowledged packet is retransmitted immediately instead of waiting for the timeout (fast retransmit)

###### Round-Trip Time Estimation and Timeout

- A new value for the sample RTT can be obtained once every RTT (since we get a new approximation / data point)
- The sample RTT fluctuate between segments due to congestion in routers
- TCP calculates its timeout using an estimate of the round trip time plus some margin
- The estimate is calculated using an average such that newer samples of the RTT provide more weight in the average
- The margin is calculated based on how much the RTT samples vary; when there is a lot of fluctuation, the margin is large, when there isn't any, the margin is small
- The initial timeout interval is 1 second

#### Flow Control

- TCP senders and receivers each have a send buffer and a receive buffer
- The send buffer contains data that was sent but not yet acknowledged and kept for the case of retransmission as well as data that TCP is waiting to transmit (waiting for the window to slide up)
- The receive buffer contains in-order data that was received and that is ready for the application above to read
- TCP has a flow control service that it provides to its application to prevent the possibility of the sender overflowing the receiver's receive buffer
- Flow control acts like a speed-matching service that matches the rate at which the sender is sending against the rate at which the receiving application is reading
- The sender maintains a "receive window" state variable which gives the sender an idea of much free buffer space is available at the receiver
- The LastByteRead variable is the number of the last byte read from the buffer by the application process
- The LastByteRcvd variable is the number of the last byte received and placed in the buffer
- rwnd = RcvBuffer - (LastByteRcvd - LastByteRead); the receive window is the amount of remaining space available in the buffer
- The rwnd value is placed in the receive window field of the header of every segment that is sent back from the receiver
- The sender on the other side maintains the LastByteSent and LastByteAcked variables (the difference between them is the amount of unacknowledged data sent into the connection)
- By keeping the amount of unacknowledged data less than rwnd, the sender prevents the receive buffer from overflowing on the other side
- However, if rwnd is 0 and the sender has no more data to send then no data segments or ACKs will be transmitted which stops any future data received from above from being transmitted when space eventually opens up in the receive buffer and the sender has data to send
- TCP uses a mechanism call Zero Window Probe (ZWP) which starts a persist timer that runs indefinitely when rwnd is 0 to prevent this
- The sender will send the next byte of data in the sequence after the timer expires (intentionally breaking the rules) to force a response from the receiver with a potential new rwnd value
- If the window is still 0, the persist timer is restarted and doubles the wait time

#### Congestion Control

##### Costs of Congeston

- As packet arrival rate nears link capacity (congestion), large queueing delays are experienced
- As packet loss occurs (due to congestion), the sender has to perform retransmissions to compensate for lost packets
- If a network is congested and experiencing large queueing delays, the sender may timeout and retransmit the packet when it is unneeded (e.g previous packet received or still in transit), wasting link bandwidth that could've been better spent on other packets
- When a packet is dropped at a router, the transmission capacity used for forwarding the packet at each link between that router and the sender was wasted

##### TCP Implementation

### Connection Management

#### Opening a Connection

##### Step 1 - Send SYN

- The client sends a data-less TCP segment with the SYN flag set to 1 in the header
- The client also adds the randomly chosen initial sequence number to the header

##### Step 2 - Receive SYN, Send SYNACK

- The receiver receives the SYN segment and allocates the TCP buffers and variables to the connection
- A connection-granted (SYNACK) segment is then sent to the client
- The SYN bit here is set to 1
- The ACK number here is set to the client's initial sequence number + 1
- The server also adds its randomly chosen initial sequence number to the header

##### Step 3 - Receive SYNACK

- When the client receives the SYNACK segment, it also allocates variables and buffers to the connection
- The client then sends another segment to the server with the ACK number set to the server's initial sequence number + 1 (acknowledging the connection-granted SYNACK segment)
- Here the SYN bit is set to 0 since the connection is established
- This segment may contain application data in the payload

#### Closing a Connection

- Because TCP is full-duplex, each direction of the connection must be closed independently

##### Step 1 - Client FIN

- The client sends a segment with the FIN flag set to 1 (when the client has no more data to send)
- The client then enters the FIN-WAIT-1 state (waiting for the ACK)

##### Step 2 - Server FINACK

- The server then responds with an ACK acknowledging that the client wants to close the connection
- The server then enters the CLOSE-WAIT state and the client enters the FIN-WAIT-2 state

##### Step 3 - Server FIN

- The server sends a segment with the FIN flag set to 1 (when the server has no more data to send)
- The server then enters the LAST-ACK state

##### Step 4 - Client FINACK

- The client then responds with an ACK acknowledging that the server wants to close the connection
- The client then enters a TIME-WAIT state (safety buffer)
- The server receives this ACK and immediately closes the connection (enters the CLOSED state)
- In the TIME-WAIT state the client enters a wait period (usually twice the maximum segment lifetime)
- This is done for reliability i.e if the client's FINACK gets lost there is a window for the server to resend its FIN and the ACK to be resent
- This also allows wandering packets from the old connection to die off in the network, preventing a new connection using the same port numbers from accidentally receiving a delayed packet from the old connection
- If the last ACK has to be retransmitted the TIME-WAIT timer is restarted

#### RST (Reset)

- If a server host receives a TCP SYN segment but the host is not listening for TCP connections on the target port, the host will then send a segment with the RST flag set to 1
- It tells the sender that it is not accepting TCP connections on that port

### Segment Stucture

- MTU (Maximum Transmission Unit) is the largest physical packet size that a network interface (e.g ethernet cable) can handle
- The standard size for ethernet networks is 1500 bytes which is the size of an Ethernet frame's payload (an IP packet)
- MSS (Maximum Segment Size) is the largest amount of application data that TCP can handle in a single segment
- MSS is usually 1460 bytes since the IP header is 20 bytes and the TCP header is 20 bytes

#### 1. Source Port (16 bits)

- 16 bits for the source port (0 to 65535)

#### 2. Destination Port (16 bits)

- 16 bits for the destination port (0 to 65535)

#### 3. Sequence Number (32 bits)

- The sequence number for a segment is calculated from the byte stream given to TCP
- E.g, if the byte stream consists of 500,000 bytes and the MSS is 1,000 bytes, TCP will construct 500 segments
- The bytes will be numbered from 0 to 499,999 and the sequence number will be the byte's number for where the segment starts (0, 1000, 2000, etc.)
- Sequence numbers increase by the payload size sent in that packet (so if current seq. is 0 and you send a packet of 1000 bytes, current seq. becomes 1000)
- Both sides choose a random initial sequence number which is done to minimize the possibility that a segment still present in the network from an earlier already-terminated connection is mistaken for a valid segment in a later connection
- Sequence numbers range from 0 to about 4 billion (4GB); when the max is reached the sequence number wraps around back to 0

#### 4. Acknowledgement Number (32 bits)

- The number of the next byte the receiver expects to receive
- If a receiver sends an ACK with the number 1001, it is saying "I have successfully received everything up to and including byte 1000, please send 1001 next"
- E.g, if a sender sends a segment with sequence number 500 and data length 200 (payload), the receiver will send an ack. number of 700 (we got bytes 500-699 now give us 700+)
- The ack. number is cumulative so it can only advance if all previous bytes have been received
- E.g, seg A = bytes 1-100, seg B = bytes 101-200, seg C = bytes 201-300
  - Seg A arrives at receiver, receiver ACKs seg A by using ack. number 101 (asking for seg B)
  - Seg C arrives at receiver, receiver sees out of order packet, buffers it but ACKs 101 (asking again for 101 because it cannot ACK seg C yet)
  - The sender receives a duplicate ACK and realizes 101 is missing at the receiver and retransmits it
- Acknowledgement numbers increase by the number of bytes received in an in-order payload from the other side
- ACKs often piggyback on data being sent if the client and server are both exchanging data simulataneously

#### 5. Header Length (4 bits)

- Tells the receiver the length of the header in 32-bit words
- A TCP header can have variable length due to the options field however it is usually empty making the header 20 bytes and the length field 0101 (5 32-bit words e.g 5 x 4 bytes = 20)

#### 6. Flags (9 bits)

- Flags that act as control bits to manage the state of the connection
- SYN: synchronize (start a connection).
- ACK: indicates the acknowledgment field is valid (the segment contains an acknowledgement for a segment that has been successfully received).
- FIN: finished (close a connection).
- RST: reset the connection.

#### 7. Receive Window

- Used for flow control, tells the sender "I only have room for X more bytes".

#### 8. Checksum

- Used for error detection
