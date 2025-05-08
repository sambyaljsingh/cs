from scapy.all import *
def handler(packet):
    print(packet.summary())
sniff(iface="enp3s0",prn=handler,store=0)

