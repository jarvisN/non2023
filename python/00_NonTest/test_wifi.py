from scapy.all import ARP, Ether, srp

def scan(ip):
    arp = ARP(pdst=ip)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether/arp

    result = srp(packet, timeout=3, verbose=0)[0]

    clients = []

    for sent, received in result:
        clients.append({'ip': received.psrc, 'mac': received.hwsrc})

    return clients

def print_result(clients):
    print("IP" + " "*18+"MAC")
    for client in clients:
        print("{:16}    {}".format(client['ip'], client['mac']))

# replace '192.168.1.1/24' with your network IP range
clients = scan("192.168.1.1/24")
print_result(clients)
