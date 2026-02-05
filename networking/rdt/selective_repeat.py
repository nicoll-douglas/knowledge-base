class Sender:
    send_base = 0
    next_seq_num = 0
    win_size = 4
    pkt_buffer = {}
    ack = set()

    def rdt_send(self, data):
        # if window is not full
        if next_seq_num < send_base + win_size:
            pkt_buffer[next_seq_num] = make_pkt(data, checksum, next_seq_num) # store packet in buffer
            udt_send(pkt_buffer[next_seq_num]) # send packet
            next_seq_num += 1 # advance sequence number
            start_timer(next_seq_num) # start logical timer for the packet

    def rdt_rcv(self, rcvpkt):
        if not corrupt(rcvpkt):
            stop_timer(rcvpkt.seq_num) # stop the timer for the packet (if it was running, operation is idempotent)
            ack.add(rcvpkt.seq_num) # mark the packet as acknowledged (may have already been acknowledged so operation idempotent)

            # if the seq num is the smallest unack'ed packet
            if rcvpkt.seq_num == send_base:
                send_base = min(pkt_buffer.keys(), key=lambda seq_num: not ack.contains(seq_num)) # advance window base to the next unack'ed seq num

    """On packet timeout, retransmit it and restart the timer.

    A timeout will also occur if a corrupted ACK was received for the packet.
    """
    def on_timeout(seq_num):
        udt_send(pkt_buffer[seq_num])
        start_timer(seq_num)


class Receiver:
    rcv_base = 0
    pkt_buffer = {}

    def rdt_rcv(self, rcvpkt):
        # if the packet is within the window (acceptable for processing)
        if rcv_base <= rcvpkt.seq_num <= rcv_base + rcvpkt.win_size - 1:
            # if packet was not already received buffer it
            if not pkt_buffer.get(rcvpkt.seq_num):
                pkt_buffer[rcvpkt.seq_num] = rcvpkt

            # if the packet was in order, deliver it and all the subsequent in order packets (if any) to the application
            if rcvpkt.seq_num == rcv_base:
                deliver_count = deliver_in_sequence_packets(rcv_base, pkt_buffer)
                rcv_base += deliver_count # advance the expected seq num by the amount of packets that were delivered (the next undelivered packet expected)

            # ack the packet regardless
            sndpkt = make_pkt(ACK, checksum, rcvpkt.seq_num)
            udt_send(sndpkt)
           
        # if the packet is to the left of the window we already processed that data previously, either way acknowledge it to help the sender move its window forward
        # if the sender is retransmitting the packet that means that a previous ACK was lost and it doesn't know that the receiver already successfully got that data so we have to ack it to help the sender
        # here we have rcv_base - N because its impossible for the sender to be more than N packets behind the receiver
        # in the case that the sender succuessfully sends N packets, all ACKs are lost, and the retransmitted packet 1 arrives first, rcv_base = N + 1 and we will ack (rcv_base - N) = 1 which is the oldest possible packet
        elif rcv_base - rcvpkt.win_size <= rcvpkt.seq_num <= rcv_base - 1:
            sndpkt = make_pkt(ACK, checksum, rcvpkt.seq_num)
            udt_send(sndpkt)


