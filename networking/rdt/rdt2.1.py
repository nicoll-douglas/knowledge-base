"""
This file illustrates sender and receiver models for rdt2.1, a stop-and-wait, reliable data transfer protocol, that uses ACKs and NAKs with sequence numbers, that accounts for corrupted ACKs and NAKs and that runs over a channel with the potential for bit errors.
"""

"""Flip a sequence number so return 0 if 1 given or 1 if 0 given."""
def flip_seq(seq_num):
    return int(!bool(seq_num))

class Sender:
    sndpkt = None # buffer for packet in case we get a NAK for it and have to retransmit
    seq_num = 0 # sequence number of the current packet being delivered

    """Receive data from above and send it as a packet with a sequence number.

    The created packet will be stored in the buffer. Note this function is only called once an ACK for the previously sent packet has been received.
    """
    def rdt_send(self, data):
        self.sndpkt = make_pkt(data, checksum, self.seq_num) # create a packet with the given data from above and the sequence number
        udt_send(self.sndpkt) # send packet

    """Retransmit a packet if the response packet was corrupted or it was a NAK."""
    def rdt_rcv(self, rcvpkt):
        if corrupt(rcvpkt) or not isACK(rcvpkt):
            udt_send(self.sndpkt) # retransmit
        else:
            self.seq_num = flip_seq(self.seq_num) # flip the sequence number


class Receiver:
    seq_num = 0 # maintain the sequence number of what we're waiting for

    """Receive a packet from below and deliver its data up.

    If the packet is not corrupted an ACK is sent. If the sequence matches what we're waiting for the data is delivered up otherwise the packet transmitted was a retransmission as a result of a corrupted ACK. If the packet was corrupted a NAK is sent."""
    def rdt_rcv(self, rcvpkt):
        if corrupt(rcvpkt):
            sndpkt = make_pkt(NAK, checksum) # create a NAK packet with a checksum
            udt_send(sndpkt) # respond with a NAK back to the sender
        else:
            # the sequence matches
            if seq_match(rcvpkt):
                data = extract_data(rcvpkt) # extract data from the packet
                deliver_data(data) # deliver data to the application layer above
                self.seq_num = flip_seq(self.seq_num) # flip the sequence number to wait for the next packet

            sndpkt = make_pkt(ACK, checksum) # create an ACK packet with a checksum
            udt_send(sndpkt) # respond with an ACK back to the sender
