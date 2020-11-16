import socket
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

serverIP = sys.argv[1]
serverPort = sys.argv[2]


while True:
    # get info from user
    siteAddress = input()
    # convert to byte string
    b = bytes(siteAddress, 'utf-8')

    s.sendto(b, (serverIP, int(serverPort)))

    data, addr = s.recvfrom(1024)
    # convert the byte string back to string
    data = data.decode('utf-8')
    dataSplit = []
    dataSplit = data.split(",")
    # print given IP from server
    print(dataSplit[1])
