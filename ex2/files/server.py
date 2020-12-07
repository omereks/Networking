import socket,sys,os

def getFileName(firstLine):
	arrFirstLine = firstLine.split(" ")
	return arrFirstLine[1]

def getConnection(arrLines):
	for line in arrLines:
		#print (line)
		if line.startswith('Connection:'):
			arrCurLine = line.split(" ")
			return arrCurLine[1]


TCP_IP = '10.0.2.15'
TCP_PORT = 12371
#TCP_PORT = int(sys.argv[1])
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
		
		#file name#
		fileName = getFileName(arrLines[0])
		if (str(fileName) == str('/')):
			fileName = "index.html"
			fileName = str(fileName)

		#connection#
		connectionStatus = getConnection(arrLines)

		#‫‪Content-Length‬‬#
		contentLength = os.path.getsize(fileName)


		Mes1 = "HTTP/1.1‬‬ ‫‪200‬‬ ‫‪OK‬‬\r\n"
		Mes2 = "Connection:‬‬ " + connectionStatus + "\r\n"
		Mes3 = "Content-Length:‬‬ ‫‪" + str(contentLength) + "\r\n\r\n"
		
		retMess = Mes1 + Mes2 + Mes3
		
		file1 = open(fileName, 'r')
		#file1.read().encode()

		#print ("received:", file1.read().encode('hex'))
		conn.send(retMess.encode() + file1.read().encode()) 
	conn.close()

