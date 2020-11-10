import socket
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

serverIP = sys.argv[1]
serverPort = sys.argv[2]


while True:
    siteAddress = input()
    b = bytes(siteAddress, 'utf-8')

    s.sendto(b, (serverIP, int(serverPort)))

    data, addr = s.recvfrom(1024)
    data = data.decode('utf-8')
    dataSplit = []
    dataSplit = data.split(",")
    print(dataSplit[1])
