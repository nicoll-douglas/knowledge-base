"""
This file illustrates sender and receiver models for rdt2.1, a stop-and-wait, reliable data transfer protocol, that uses ACKs and NAKs, that accounts for corrupted ACKs and NAKs and that runs over a channel with the potential for bit errors.
"""

"""Flip a sequence number so return 0 if 1 given or 1 if 0 given."""
def flip_seq(seq_num):
    return int(!bool(seq_num))

class Sender:
    sndpkt = None # buffer for packet in case we get a corrupt response or incorrect ACK for it and have to retransmit
    seq_num = 0 # sequence number of the current packet being delivered
    timer = None

    """Receive data from above, send it as a packet with a sequence number and start the timer.

    The created packet will be stored in the buffer. Note this function is only called once the correct ACK for the previously sent packet has been received.
    """
    def rdt_send(self, data):
        self.sndpkt = make_pkt(data, checksum, self.seq_num) # create a packet with the given data from above and the sequence number
        udt_send(self.sndpkt) # send packet
        self.timer = start_timer() # start the timer so we can detect packet loss

    """Resets the sender state for the transmission of the next packet if we got a non-corrupt ACK for the matching sequence number (most recent packet)."""
    def rdt_rcv(self, rcvpkt):
        if not timer_running(): return # if there is no timer running, we are not expecting any packets so don't do anything

        # we got a non-corrupt packet with an ACK for the correct sequence
        if not corrupt(rcvpkt) and seq_match(rcvpkt):
            self.seq_num = flip_seq(self.seq_num) # flip the sequence number 
            stop_timer(self.timer) # stop the timer, it doesn't need to keep running anymore

    """Retransmit the packet when the timer runs out (packet loss probably occurred) and restart the timer. 
    
    This method also handles the case where we received a response but it was corrupt or it was out of sequence. Either way we will need to retransmit so we wait for the timer to run out.
    """
    def on_timeout():
        udt_send(self.sndpkt)
        self.timer = start_timer()


class Receiver:
    seq_num = 0 # maintain the sequence number of what we're waiting for

    """Receive a packet from below and deliver its data up if not corrupted and the sequence number of the packet matches what we're waiting for."""
    def rdt_rcv(self, rcvpkt):
        if not corrupt(rcvpkt) and seq_match(rcvpkt.seq_num):
            data = extract_data(rcvpkt) # extract data from the packet
            deliver_data(data) # deliver data to the application layer above
            self.seq_num = flip_seq(self.seq_num) # flip the sequence number to wait for the next packet

        sndpkt = make_pkt(ACK, checksum, rcvpkt.seq_num) # create an ACK packet with a checksum and the sequence number of the received packet
        udt_send(sndpkt) # send ACK packet
