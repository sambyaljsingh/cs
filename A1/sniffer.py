import argparse
from scapy.all import sniff

class Sniffer:
    def __init__(self, args):
        self.args = args
     
    def __call__(self, packet):
        if self.args.verbose:
            packet.show()
        else:
            print(packet.summary())
         
    def run_forever(self):
        # You can just pass 'self' directly as it references __call__
        sniff(iface=self.args.interface, prn=self, store=0)
     
parser = argparse.ArgumentParser()
parser.add_argument("-v", "--verbose", default=False, action="store_true", help="be more talkative")
parser.add_argument("-i", "--interface", type=str, required=True, help="network interface name")
args = parser.parse_args()

sniffer = Sniffer(args)
sniffer.run_forever()

