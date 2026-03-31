# Computer Networks and the Internet

## Packet Switching

- Packet switching is a method of transmitting data through a network by breaking it up into small units called packets
- Each packet is sent independently through the network and may take different paths to reach the destination, where the packets are reassembled into the original message
- Network application exchange messages with each other which are broken down into packets at the source
- Between source and destination, packets travel through communication links and packet switches (routers and link-layer switches mainly)
- Packets are transmitted over each link at a rate equal to the full transmission rate of the link

### Store-and-Forward Transmission

- Store-and-forward transmission means that packet switches must receive an entire packet before it can transmite the first bit of the packet onto the outbound link
- Packet switches do this because they need to process data in the packet in order to forward it to the correct place

### Packet Queueing

- Each outbound link of a packet switch has an output buffer (queue) which stores packets the switch will send out of that link
- If a packet arrives at the queue but there are other packets in front, it will suffer a queueing delay
- If an output buffer is full, packet loss will occur as any incoming packets will be dropped

## Circuit Swtiching

- Circuit switching is a method of transmitting data through a network by creating a dedicated path or circuit from one endpoint to another for the entire duration of a session, ensuring a constant and reserved channel for data transmission
- When a network establishes a circuit, it also reserves a constant transmission rate in the network's links (representing a fraction of each link's transmission capacity)
- Since a fixed transmission rate has been reserved, the sender can transfer data to the receiver at the guaranteed constant rate

### Frequency Division Multiplexing (FDM)

- With FDM, the frequency spectrum of a link is divided up among the connections established across the link
- The frequency band for telephone networks is 4kHz
- The width of the band is called the bandwidth
- FM radio stations also use FDM to share the frequency spectrum between 88MHz and 108MHz

### Time Division Multiplexing (TDM)

- With FDM the frequency domain is split up however with TDM, the time domain is split up
- Time is split into frames, each lasting for T bits
- If a link has N connections then each connection gets N/T bits of transmission ever T bits (rotates peridodically across connections)

## Packet Switching vs. Circuit Switching

- An argument against packet switching is that it is not suitable for real-time services (telephone calls, video conferencing) because of unpredictable end-to-end delays (due primarily to queueing delays).
- An argument against circuit switching is that it offers better sharing of transmission capacity
- Packet switching is less costly to implement than circuit switching
- During silent periods where no data is transmitted, bandwidth is wasted with circuit switching
- Packet switching allocates link use on demand whereas circuit-switching pre-allocates bandwidth

## Network Performance

### Delay

- When a packet has fully arrived at a packet switch, it may experience several delays before arriving at the next packet switch
- Other than the ones mentioned below, end systems can also produce delays for example in packetization and depacketization of messages

#### Processing Delay

- The time required to examine the packet's header and determine where send it forms part of the processing delay
- The processing delay may also include the time it takes for encapsulation and decapsulation of packet layer information
- Devices processing the packet may also verify packet checksums to detect bit errors

#### Queueing Delay

- A packet experiences a queueing delay if it is ready to be transmitted onto a link but it has to wait (either there is a packet already in transmission or the queue is non-empty)
- Queueing delays can be measured using the traffic intensity
- The traffic intensity is the ratio of the average rate at which bits arrive at a link to transmission rate that they are pushed out of the link
- A traffic intensity > 1 means that the packet queue will grow, whereas <= 1 means the queue is stable or will shrink

#### Transmission Delay

- The transmission delay is the amount of time required to push all bits of a packet into a link

#### Propagation Delay

- The propagation delay is the amount of time required for a bit to travel across a link
- The speed at which the bit travels depends on the physical medium and thus so does the delay

### Throughput

- Instantaneous throughput at any instant of time is the rate (bits/sec) at which a receiver is receiving bits from a sender that form part of a piece of data
- Average throughput measures the average rate at which a receiver is receiving bits from a sender that form part of a piece of data (the quotient of the total bits and total data transfer time)

#### Factors Affecting Throughput

- From end-to-end, there are several links connecting packet switches
- One of these links may be a global bottleneck link i.e the link with the lowest transmission rate
- The throughput thus depends on the transmission rate of the bottleneck link as data cannot flow faster end-to-end than the bottleneck allows
- Throughput also depends on queueing delays
- Example: 10 unrelated pieces of data / messages are being transmitted across a link
- This means packets will get queued and the link has to share its capacity
- Assuming fair sharing of packets, the effective transmission rate of the link is now divided by 10 and so is the throughput across each message
