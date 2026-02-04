"""
This file illustrates sender and receiver models for rdt2.0, a stop-and-wait, reliable data transfer protocol, that uses ACKs and NAKs, and that runs over a channel with the potential for bit errors.

The main flaw with this protocol is that it doesn't account for the possibility that an ACK or NAK packet could be corrupted. We add a checksum to the sent packet which allows it to be verified for corruption however we do not do the same for the response packet (ACK or NAK).
"""

class Sender:
    sndpkt = None # buffer for packet in case we get a NAK for it and have to retransmit

    """Receive data from above and send it as a packet.

    The created packet will be stored in the buffer. Note this function is only called once an ACK for previously sent packet has been received.
    """
    def rdt_send(self, data):
        self.sndpkt = make_pkt(data, checksum) # create a packet with the given data from above
        udt_send(self.sndpkt) # send packet

    """Retransmit a packet if a NAK for it was received."""
    def rdt_rcv(self, rcvpkt):
        if not isACK(rcvpkt):
            udt_send(self.sndpkt) # retransmit


class Receiver:
    """Receive a packet from below and deliver its data up + send an ACK if the packet is not corrupted otherwise send a NAK."""
    def rdt_rcv(self, rcvpkt):
        if corrupt(rcvpkt):
            sndpkt = make_pkt(NAK) # create a NAK packet
            udt_send(sndpkt) # respond with a NAK back to the sender
        else:
            data = extract_data(rcvpkt) # extract data from the packet
            deliver_data(data) # deliver data to the application layer above
            sndpkt = make_pkt(ACK) # create an ACK packet
            udt_send(sndpkt) # respond with an ACK back to the sender
