import socket
import CacheDNS.config as config

request = b"\x96\xd9\x01\x00\x00\x01\x00\x00\x00\x00\x00\x00\x06\x67\x6f" \
          b"\x6c\x61\x6e\x67\x03\x6f\x72\x67\x00\x00\x01\x00\x01"


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.settimeout(5)
sock.sendto(request, (config.DNS_SERVER_IP, config.DNS_PORT))
print(sock.recv(1024))