class Sender:
    seq_num = 0
    sndpkt = None


    def rdt_send(self, data):
        self.sndpkt = make_pkt(self.seq_num, data, checksum) # create packet with sequence number

        udt_send(self.sndpkt) # send packet


    def rdt_rcv(self, rcvpkt):
        # corrupt receive packet or NAK
        if corrupt(rcvpkt) or not isACK(rcvpkt):
            udt_send(self.sndpkt) # retransmit packet with same sequence number

        # otherwise response packet was in tact and was an ACK for the sent packet
        # wait for call from above with next sequence number
        else:
            self.seq_num = 0 if self.seq_num == 1 else 0


class Receiver:
    seq_num = 0 # what we're waiting for


    def rdt_rcv(self, rcvpkt):
        # non-corrupt receive packet
        if not corrupt(rcvpkt):
            # sequence matches (what we're waiting for and isn't a duplicate from a retransmission)
            if seq_match(rcvpkt):
                # extract and deliver data, wait for next packet
                extract(rcvpkt, data)
                deliver_data(data)
                self.seq_num = 0 if self.seq_num == 1 else 0 # update to next sequence number

            # send an ACK for non-corrupt data regardless is sequence matches
            sndpkt = make_pkt(ACK, checksum)
            udt_send(sndpkt)

        # otherwise, packet was corrupt so send NAK
        else:
            sndpkt = make_pkt(NAK, checksum)
            udt_send(sndpkt)

