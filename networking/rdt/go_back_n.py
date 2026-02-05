"""
ack_packets = [0, base - 1]
unack_packets = [base, next_seq_num - 1]
sendable_packets = [next_seq_num, base + N - 1]
unsendable_packets = >= base + N

next_seq_num >= base + N means the range of sendable = [base + N, base + N - 1] which is empty so packets can be sent 
"""

class Sender:
    packet_buffer = {}
    timer = None
    base = 0
    next_seq_num = 0
    N = 4

    def rdt_send(data):
        # window is not full so the packet can be sent
        if self.next_seq_num < self.base + self.N:
            self.packet_buffer[self.next_seq_num] = make_pkt(data, checksum, self.next_seq_num) # store the packet in the buffer according to its sequence number
            udt_send(self.packet_buffer[self.next_seq_num]) # send the packet

            # if the packet is the first in the window start the timer
            if self.base == self.next_seq_num:
                self.timer =  start_timer()

            # increment the sequence number for the next packet
            self.next_seq_num += 1

    def rdt_rcv(rcvpkt):
        if not corrupt(rcvpkt):
            # the receiver has packets up to and including rcvpkt.seq_num so update the base to reflect this by moving it forward
            self.base = rcvpkt.seq_num + 1

            # the base has caught up to the next sequence number so there are no longer any unacknowledged packets in transit meaning we can stop the timer
            if self.base == self.next_seq_num:
                stop_timer(self.timer)
            # start a new timer for the oldest unacknowledged packet if the base hasn't caught up
            else:
                self.timer = start_timer()

    def on_timeout(self):
        # start a new timer
        self.timer = start_timer()
        
        # resend all currently unacknowledged packets
        for i in range(self.base, self.next_seq_num):
            udt_send(self.packet_buffer[i])


class Receiver:
    seq_num = 0

    def rdt_rcv(self, rcvpkt):
        if not corrupt(rcvpkt) and rcvpkt.seq_num == self.seq_num:
            data = extract_data(rcvpkt)
            deliver_data(data)
            self.seq_num += 1

        sndpkt = make_pkt(ACK, checksum, self.seq_num - 1) # send to sender that we have all packets up to and including seq number - 1 (waiting for seq number)
        udt_send(sndpkt)
