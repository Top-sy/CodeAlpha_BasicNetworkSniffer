from scapy.all import sniff, IP, TCP, UDP, ICMP, Raw, wrpcap
from datetime import datetime


def get_protocol_name(packet):
    if packet.haslayer(TCP):
        return "TCP"
    elif packet.haslayer(UDP):
        return "UDP"
    elif packet.haslayer(ICMP):
        return "ICMP"
    else:
        return "OTHER"


def packet_sniffer(packet):
    print("\n========== PACKET CAPTURED ==========")

    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print("Time:", current_time)

    if packet.haslayer(IP):
        source_ip = packet[IP].src
        destination_ip = packet[IP].dst
        protocol_name = get_protocol_name(packet)
        packet_size = len(packet)

        print("Source IP:", source_ip)
        print("Destination IP:", destination_ip)
        print("Protocol:", protocol_name)
        print("Packet Size:", packet_size, "bytes")

        if packet.haslayer(Raw):
            payload = packet[Raw].load
            print("Payload:", payload)

    print("=====================================")


print("Starting Network Sniffer...")
print("Waiting for packets...\n")

captured_packets = sniff(prn=packet_sniffer, count = 20)
wrpcap("captured_traffic.pcap", captured_packets)