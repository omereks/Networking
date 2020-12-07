#!/usr/bin/env python

import socket,sys

TCP_IP = sys.argv[1]

TCP_PORT = int(sys.argv[2])
BUFFER_SIZE = 1024
MESSAGE1 = "Avraham"
MESSAGE2 = "123456"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))

s.send(MESSAGE1.encode())
data = s.recv(BUFFER_SIZE)
print("received data:", data.decode())


s.send(MESSAGE2.encode())
data = s.recv(BUFFER_SIZE)
s.close()

print("received data:", data.decode())