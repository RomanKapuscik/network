"""
1. Create arp request directed to broadcast MAC asking fo IP
2. Send packet and receive response.
3. Parse the response.
4. Return result.

"""
import scapy.all as scapy

def scan(ip: str):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst='ff:ff:ff:ff:ff:ff')
    arp_request_broadcast = broadcast/arp_request
    answered_list, unanswered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)
    print('PI\t\t\t\t\tMAC\n----------------------------------------------')
    idx = 1
    devices =[]
    for element in answered_list:
        print(f'{idx}. {element[1].psrc}\t\t{element[1].hwsrc}')
        print('----------------------------------------------')
        idx += 1
        device = (element[1].psrc, element[1].hwsrc)
        devices.append(device)
    return devices

# devices = scan('192.168.0.1/24')
# print(devices)