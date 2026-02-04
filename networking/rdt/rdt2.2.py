def flip_seq(seq):
    return 0 if seq == 1 else 0
# fed


class Sender:
    seq_num = 0
    sndpkt = None


    def rdt_send(self, data):
        self.sndpkt = make_pkt(self.seq_num, data, checksum) # create packet with sequence number

        udt_send(self.sndpkt) # send packet


    # incoming packets are now always going to be ACKs with a sequence number instead of having ACK and NAK
    def rdt_rcv(self, rcvpkt):
        # corrupt receive packet or is ACK for out-of-sequence packet (meaning receiver is asking for retransmission)
        if corrupt(rcvpkt) or not seq_match(rcvpkt):
            udt_send(self.sndpkt) # retransmit packet

        # otherwise if reponse is not corrupt and sequence number is correct
        # wait for call from above with next sequence number
        else:
            self.seq_num = flip_seq(self.seq_num)


class Receiver:
    seq_num = 0 # what we're waiting for


    def rdt_rcv(self, rcvpkt):
        # non-corrupt receive packet and sequence matches (what we're waiting for)
        if not corrupt(rcvpkt) and seq_match(rcvpkt):
            # extract and deliver data
            extract(rcvpkt, data)
            deliver_data(data)

            # send ACK for sequence number
            sndpkt = make_pkt(ACK, self.seq_num, checksum)
            udt_send(sndpkt)

            # flip sequence
            self.seq_num = flip_seq(self.seq_num)


        # send an ACK for corrupt data or non-matching sequence acknowledging a packet of the opposite sequence (sequence of rcvpkt)
        # this is the way asking for retransmission of the packet we are waiting for
        else:
            sndpkt = make_pkt(ACK, flip_seq(self.seq_num), checksum)
            udt_send(sndpkt)

