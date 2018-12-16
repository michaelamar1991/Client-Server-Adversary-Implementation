from scapy.all import *

counter = 0

def sniffAction(pkt):
    global counter
    counter += 1
    if counter%2==0:
    	return
    return'{} ==> {} || Size : {} bytes || Data : {}'.format(pkt[0][1].src, pkt[0][1].dst, pkt[0][1].len, pkt[0][3].load)


sniff(iface="lo0", filter="udp port 12321", prn = sniffAction, store=0)