import socket
import sys
import time

# read a file and initialize 2D list
def creatListFromFile(fileName):
	file1 = open(fileName, 'r')
	Lines = file1.readlines()
	listFile = []
	i = 0
	for line in Lines:
		listFile.append(line.split(","))
		# put 0 if the line is static line
		if len(listFile[i]) == 3:
			listFile[i].append(0)
		# if the site address is not  static
		if (float(listFile[i][3]) > 0.0):
			thisTime = time.time()
			passTime = thisTime - float(listFile[i][3])
			# if TTL passed, remove the line
			if (float(listFile[i][2]) <= passTime):
				listFile.pop(i)
				i = i - 1
		i = i + 1
	updateFile(fileName, listFile)
	return listFile

# getting 2D list and look for the domain
# if found return the inside list
# else returning empty ([]) list
def searchDomainInList (listIPs, domain):
	i = 0
	for oneList in listIPs:
		try:
			domainInList = listIPs[i][0]
			if domainInList == str(domain):
				return listIPs[i]
		except:
			pass
		i = i+1
	return []
# function take an array and convert to string
def makeFromArrayToString(arr):
	ret = ""
	for w in arr:
		ret = ret + str(w) + ","
	# remove the last ","
	ret = ret[:-1]
	return ret
# function updates file according to our 2D array
def updateFile(fileName, arrayList):
	arrStr = []
	for line in arrayList:
		arrStr.append(makeFromArrayToString(line).replace("\n",""))
	with open(fileName, 'w') as f:
		for line in arrStr:
			f.write("%s\n" % line)


# argumnets from command line
myPort = sys.argv[1]
parentIP = sys.argv[2]
parentPort = sys.argv[3]
ipsFileName = sys.argv[4]
# initalize a socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('', int(myPort)))

while True:
	clientDomain, clientAddress = s.recvfrom(1024)
	clientDomain = clientDomain.decode('utf-8')
	listIps = creatListFromFile(ipsFileName)
	specificLine = searchDomainInList(listIps, clientDomain)
	# is server find the domain in the file
	if specificLine != []:
		siteInfo = makeFromArrayToString(specificLine)
		siteInfo = bytes(siteInfo, 'utf-8')
		s.sendto(siteInfo, clientAddress)
	# else, send to parent server
	else:
		clientDomain = bytes(clientDomain, 'utf-8')
		# send to parent server
		s.sendto(clientDomain, (parentIP, int(parentPort)))
		data, parentAddress = s.recvfrom(1024)
		arrayToAdd = data.decode('utf-8')
		arrayToAdd = arrayToAdd.split(",")
		# add the new site to 2D array
		arrayToAdd[3] = time.time()
		listIps.append(arrayToAdd)
        # update the file according to the 2D array
		updateFile(ipsFileName, listIps)
        # send the answer back to client
		s.sendto(data, clientAddress)
