from scapy.all import *

counter = 0

def sniffAction(pkt):
    global counter
    counter += 1
    return'{} ==> {} || Size : {} bytes || Data : {}'.format(pkt[0][1].src, pkt[0][1].dst, pkt[0][1].len, pkt[0][3].load)


sniff(filter="dst host 172.20.10.4 and port 12321 and udp", prn = sniffAction, store=0)
