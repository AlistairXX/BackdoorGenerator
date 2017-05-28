from scapy.all import *
import time
udp = []
tcp = []
found = []
def filter(pkt):
    if pkt.haslayer('IP'):
        if pkt.haslayer('TCP'):
            if pkt['TCP'].dport in tcp:
                if pkt['IP'].src not in found:
                    found.append(pkt['IP'].src)
        elif pkt.haslayer('UDP'):
            if pkt['UDP'].dport in udp:
                if pkt['IP'].src not in found:
                    found.append(pkt['IP'].src)
def main():
    tmp = raw_input('Enter list of udp ports in this form(p1,p2,p3) for no port hit enter: ')
    if tmp != '':
        for port in tmp.split(','):
            dp.append(int(port))
    tmp = raw_input('Enter list of tcp ports in this form(p1,p2,p3) for no port hit enter: ')
    if tmp != '':
        for port in tmp.split(','):
            tcp.append(int(port))
    filename = raw_input('Enter output filename: ')
    while True:
        output = open(filename,'a+')
        sniff(prn=filter,timeout=60)
        content = output.readlines()
        final_content = []
        for line in content:
            line = line[:len(line)-1]
            final_content.append(line)
        for ip in found:
            if ip not in final_content:
                output.write(ip+'\n')
        output.close()
        print 'Output was written to file'
main()
    
