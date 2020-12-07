import socket,sys

TCP_IP = '10.0.2.15'
TCP_PORT = int(sys.argv[1])
BUFFER_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

while True:
	conn, addr = s.accept()
	print ('New connection from:', addr)
	while True:
		data = conn.recv(BUFFER_SIZE)
		if not data: break
		arrLines = data.decode().split("\r\n")

		print ("received:", arrLines)
		conn.send(data.upper()) 
	conn.close()
