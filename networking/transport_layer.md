# Transport Layer - OSI Model Layer 4

- Transport-layer protocols provide logical communication between processes running on different hosts
- Network-layer protocols provide logical communication between hosts

## UDP

### Services Provided by UDP

- Process-to-process data delivery
- Segment integrity checking by including error-detection fields in the segment's header
- Multiplexing/demultiplexing is as simple as specifying the host and destination ports in the headers of a UDP segment
- When a sender specifies the source port it acts as a "return address"

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

### Services Provided by TCP

- Process-to-process data delivery
- Reliable data transfer ensuring data is correct and in order
- Congestion control (a service provided not so much to the application but to the internet as a whole)

### Multiplexing and Demultiplexing

- Refers to extending the host-to-host delivery service to a process-to-process delivery service for applications running on the hosts
- The transport-layer in the receiving host doesn't deliver data directly to the process but to an intermediary socket (the OS's networking API)
- Each transport-layer segment has a set of fields in the segment for this purpose
- Multiplexing and demultiplexing also happen at other layers of the OSI model whenever a protocol in the layer is used by other protocols higher up

#### Demultiplexing

- In a receiving host, the transport layer examines the fields a transport-layer segment in order to identify the receiving socket and then directs the segment to that socket
- Ths job of delivering the data in a transport-layer segment to the correct socket is called demultiplexing

#### Multiplexing

- The job of gathering data chunks passed to the transport-layer at the source host, encapsulating each chunk with header information to create segments, and passing the segments to the network layer is called multiplexing

#### Sockets and Port Numbers

- Sockets on end hosts must be uniquely identified in order for multiplexing and demultiplexing to work at the transport-level
- The unique identifiers used are the source port number field and the destination port number field in a transport-layer segment
- Each port is an unsigned 16-bit number (0 to 65535)
- Port numbers ranging from 0 to 1023 are well-known port numbers and are restricted

### Segment Stucture

- MTU (Maximum Transmission Unit) is the largest physical packet size that a network interface can handle
- The standard size for ethernet networks is 1500 bytes which is the size of an Ethernet frame's payload (an IP packet)
- MSS (Maximum Segment Size) is the largest amount of application data that TCP can handle in a single segment
- MSS is usually 1460 bytes since the IP header is 20 bytes and the TCP header is 20 bytes

#### 1. Source Port

- 16 bits for the source port (0 to 65535)

#### 2. Destination Port

- 16 bits for the destination port (0 to 65535)

#### 3. Sequence Number (32 bits)

- The sequence number for a segment is calculated from the byte stream given to TCP
- E.g, if the byte stream consists of 500,000 bytes and the MSS is 1,000 bytes, TCP will construct 500 segments
- The bytes will be numbered from 0 to 499,999 and the sequence number will be the byte's number for where the segment starts (0, 1000, 2000, etc.)
- Sequence numbers increase by the payload size sent in that packet (so if current seq. is 0 and you send a packet of 1000 bytes, current seq. becomes 1000)
- Both sides choose a random initial sequence number which is done to minimize the possibility that a segment still present in the network from an earlier already-terminated connection is mistaken for a valid segment in a later connection

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
- Each time a sender or receiver receives a segment, the header acts as a status report saying "here is the next chunk of my data (seq), and by the way, I have successfully received everything of yours up to this point (ack)"
- ACKs often piggyback on data being sent if the client and server are both exchaning data simulataneously

#### 5. Header Length (4 bits)

- Tells the receiver the length of the header in 32-bit words

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

### Reliable Data Transfer
