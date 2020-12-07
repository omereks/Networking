import socket,sys

TCP_IP = '10.0.2.15'
TCP_PORT = int(sys.argv[1])
BUFFER_SIZE = 1024




s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

while True:
	conn, addr = s.accept()
	print ("New connection from:", addr)
	while True:
	    data = conn.recv(BUFFER_SIZE)
	    if not data: break
	    print("received data:", data.decode())
	    conn.send(data.decode().upper().encode()) 
	conn.close()

