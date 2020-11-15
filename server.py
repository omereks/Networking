import socket
import sys

# getting a file and returning 2D list
def creatListFromFile(fileName):	
	file1 = open(fileName, 'r') 
	Lines = file1.readlines()
	listFile = []
	for line in Lines: 
		listFile.append(line.split(","))
	file1.close
	return listFile

# getting 2D list and look for the domain
# if found return the inside list
# else returning empty ([]) list
def searchDomainInList (listIPs, domain):
	i = 0
	for oneList in listIPs:
		try:
			domiainInList = listIPs[i][0]
			if domiainInList == str(domain):
				return listIPs[i]
		except:
			pass
		i = i+1
	return []

#making a one line sring from array and split by ','
def makeFromArrayToString(arr):
	ret = ""
	for w in arr:
		ret = ret + w + ","
	return ret



myPort = sys.argv[1]
parentIP = sys.argv[2]
parentPort = sys.argv[3]
ipsFileName = sys.argv[4]

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
s.bind(('', int(myPort)))	


while True:
	clientDomian, addr = s.recvfrom(1024)
	clientDomian = clientDomian.decode('utf-8')
	
	#noraml server
	if parentIP != "-1" and parentPort != -1:
		listIps = creatListFromFile(ipsFileName)
		specificLine = searchDomainInList(listIps, clientDomian) 
					#TODO ttl chcek
		
		if specificLine != []:
			b = makeFromArrayToString(specificLine)
			b = bytes(b, 'utf-8')
			s.sendto(b, addr)
		else:
			pass	#TODO sending to parent server

	#parent server
	if parentIP == -1 and parentPort == -1:
		pass		# TODO parent sever