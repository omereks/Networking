import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('', 60237))
s.sendto( b"avraham and omer , 205937949", ('127.0.0.1', 12345))
data, addr = s.recvfrom(1024)
print(str(data), addr)
s.close()
