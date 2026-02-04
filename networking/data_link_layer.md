# Data Link Layer - OSI Model Layer 2

## Frames

A frame is the data unit at layer 2. A frame packages bits transmitted at layer 1.

### Structure

#### 1. Preamble

- Size: 7 bytes
- Shape: 10101010
- Purpose: Allows receivers to synchronize their clock at the bit-level by detecting the signal of an incoming frame. The receiver will lock onto the signal timing to know where each bit will start and end.

#### 2. Start Frame Delimiter (SFD)

- Size: 1 byte
- Shape: 10101011
- Purpose: Signals to the receiver the start of a frame. The bit at the end breaks the pattern of the preamble signalling the start of the frame data.

#### 3. Destination MAC Address

- Size: 6 bytes
- Purpose: A link-layer switch reads this field to determine where to send the frame (the target device).
- Special cases:
    - Broadcast: FF:FF:FF:FF:FF:FF - Frame goes to all devices on the network
    - Specific range of MAC addresses - Frame goes to multiple subscribed devices

#### 4. Source MAC Address

- Size: 6 bytes
- Purpose: Identifies the MAC address of the sender of the frame and lets switches learn MAC addresses to build their forwarding tables.

#### 5. EtherType / Length

- Size: 2 bytes
- Shape: EtherType >= 0x0600 (decimal 1536), Length <= 1500
- EtherType: Specifies which layer 3 protocol is encapsulated (e.g IPv4 = 0x0800, IPv6 = 0x86DD, ARP = 0x0806)
- Length: Indicates how many bytes are in the payload
- Purpose: Lets the receiver know how to interpret the payload

#### 6. Payload / Data

- Size: 46-1500 bytes
- Purpose: Carries actual data, usually a layer 3 packet
- Minimum size is 46 bvtes, if size is smaller padding bytes (0x00) are added to the end of the payload to meet the minimum ethernet frame size of 64 bytes.
- Maximum size is 1500 bytes which is the standard MTU (Maximum Transmission Unit) for ethernet.

#### 7. Frame Check Sequence (FCS)

- Size: 4 bytes
- Purpose: Error detection using CRC (Cyclic Redundancy Check)
- The sender calculates a checksum over all previous bits in the frame and stores it in the FCS.
- The receiver recalculates the checksum and compares it to the FCS. If they match the frame is likely ok, otherwise it is discarded.

### Data Loss

- Error checking occurs at the NIC (network interface card) where the FCS and MAC address are checked that they are ok.
- If error detection fails, the frame is discarded/dropped which causes data loss at layer 2.
- Data loss is handled differently depending on the upper layer (e.g TCP, lost frame = lost segment = TCP detects missing sequence numbers = TCP retransimits the segment).

## Outgoing Frames

- When an application wants to send data, the device creates an IP packet with the source IP and destination IP.
- The IP layer asks "is the destination on my local network or somewhere else?".
- Every device has a routing table. If a destination matches a local route, send the packet directly otherwise send to the default gateway (a router's IP address on the local network).
- The routing table contains information about IP addresses, their gateways, subnet masks, and what outgoing network interface to use for them.
- Once the device decides where the IP packet must go using the routing table it needs a destination MAC address to build an ethernet frame.

### Building Ethernet Frames

- Once the device knows the local IP to send to and which network interface (found in the routing table), it has to find the corresponding MAC address.
- The device checks the network interface's ARP table for the MAC address.
- If missing, an ARP request is sent/broadcast asking "who has IP x?" to obtain the MAC address.
- An ethernet frame is constructed with a destination MAC address of FF:FF:FF:FF:FF:FF (broadcast) and exits the device using the network interface.
- The corresponding device then responds to the request with the MAC address which is then cached in the ARP table.
- An ethernet frame can now be constructed.

## Link-layer Switches

- A layer 2 switch operates on ethernet frames.
- The switch maintains a MAC address table where each entry contains a MAC address, the port and a timestamp of when it was recorded.
- MAC table entries expire after a period of inactivity (typically ~300 seconds) which prevents stale entries when devices move or disconnect.
- A switch is only responsible for accepting incoming frames and forwarding them to their destination.
- MAC Learning: When a frame arrives on a port the switch updates the table with the source MAC address, port number, and timestamp or inserts into the table.

### Forwarding

- Destination MAC is known: The switch looks up the MAC address in the table and forwards the frame only to the correct port.
- Destination MAC is unknown: The switch floods the frame out of all ports except the incoming one (unknown unicast flooding). When the destination device replies, the switch learns its MAC and future frames are sent directly.
- Desination MAC = FF:FF:FF:FF:FF:FF: The switch floods the frame out of all ports except the incoming one (used for things like ARP requests and DHCP discovery).
