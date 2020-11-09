import socket
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverIP = sys.argv[1]
serverPort = sys.argv[2]
while True:
    siteAddress = input('Enter site address')
    b = bytes(siteAddress, 'utf-8')
    s.sendto(b, (serverIP, serverPort))
    s.bind(('', 60237))                    # TODO maybe should remove it
    data, addr = s.recvfrom(1024)
    print(str(data), addr)
