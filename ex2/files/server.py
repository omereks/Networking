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
#TCP_PORT = 12364

TCP_PORT = int(sys.argv[1])
BUFFER_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)
#s.settimeout(1.0)

while True:
	conn, addr = s.accept()
	print ('New connection from:', addr)
	while True:
		conn.settimeout(1.0)
		try:
			data = conn.recv(BUFFER_SIZE)
		except socket.timeout:
			break
		if not data: break
		print (data.decode())
		arrLines = data.decode().split("\r\n")
		#file name#
		fileName = getFileName(arrLines[0])
		if (str(fileName) == str('/')):
			fileName = "index.html"
			fileName = str(fileName)
		if (str(fileName[0]) == str('/')):
			fileName = str(fileName[1:])
		
		#connection#
		connectionStatus = getConnection(arrLines)

		if(str(fileName) == str('‫/redirect‬‬')):
			MesRed = 'HTTP/1.1 301 Moved Permanently' + '\r\n' + 'Connection: close' + '\r\n' + 'Location: /result.html' + '\r\n\r\n'
			#MesRed = "‫‪HTTP/1.1‬‬ ‫‪301‬‬ ‫‪Moved‬‬ ‫‪Permanently‬‬"+"\r\n‫‪"+"Connection:‬‬ ‫‪close‬‬\r\n" + "‫‪Location:‬‬ ‫‪/result.html‬‬" + "\r\n\r\n"
			MesRed = str(MesRed)
			conn.send(MesRed.encode())
			break
		if(not os.path.exists(fileName)):
			MesErr = 'HTTP/1.1 404 Not Found' + '\r\n' + 'Connection: close' + '\r\n\r\n'
			conn.send(MesErr.encode())
			break
		
		
		
		#‫‪Content-Length‬‬#
		contentLength = os.path.getsize(fileName)
		

		



		Mes1 = "HTTP/1.1‬‬ ‫‪200‬‬ ‫‪OK‬‬\r\n"
		Mes2 = "Connection:‬‬ " + connectionStatus + "\r\n"
		Mes3 = "Content-Length:‬‬ ‫‪" + str(contentLength) + "\r\n\r\n"
		
		retMess = Mes1 + Mes2 + Mes3
		
		

		if (fileName.endswith('.ico') or fileName.endswith('.jpg')):
			file1 = open(fileName, 'rb')
			conn.send(retMess.encode() + file1.read())
		else:
			file1 = open(fileName, 'r')
			conn.send(retMess.encode() + file1.read().encode())


		
		
		
		
		if (connectionStatus == "close"):
			break
	conn.close()

