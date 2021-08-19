########################################################
##                                                    ##
##               OstrichGuardian v1.0.0               ##
##     Copyright (c) 2021 Frederico F. Martins        ##
##                    -------------                   ##
##                    @FredFMartins                   ##
##                    -------------                   ##
##                                                    ##
########################################################

import sys
import scapy
import logging
from scapy.all import *
from datetime import *

whitelist=[]

#Stuff to improve readibility of the log file:

intro=str(" |  ")
log=str("   |  " + str(datetime.now()))

with open('snifflog.txt', 'w') as f:
    f.write(str(' \ Network ARP log since ') +str(date.today()) + str(' :\n'))

# Monitor the network and print/save ARP requests:

def arp_monitor_callback(pkt):
    if ARP in pkt and pkt[ARP].op in (1,2):
        sniffed=pkt.sprintf(intro + "%ARP.hwsrc% %ARP.psrc%" + log)
        print(sniffed)
        sniffedmac = sniffed.split()[1]
        sniffedip = sniffed.split()[2]
        if sniffedmac in whitelist:
            with open('snifflog.txt', 'a') as f:
                f.write("\n" + sniffed + "   --> whitelisted")
        else:
            with open('snifflog.txt', 'a') as f:
                f.write("\n" + sniffed + "   --> WARNING - CHECK LATER")
#                send(fragment(IP(dst=sniffedip)/ICMP()/("X"*60000))):

           

sniff(prn=arp_monitor_callback, filter="arp", store=0)
