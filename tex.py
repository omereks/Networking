
def makeFromArrayToString(arr):
	ret = ""
	for w in arr:
		ret = ret + w + ","
	return ret


def updateFile(arrayList):
    arrStr = []
    for line in arrayList:
        arrStr.append(makeFromArrayToString(line))
    with open('test.txt', 'w') as f:
        for line in arrStr:
            f.write("%s\n" % line)


arr = [["a","b"],["c","d"]]
updateFile(arr)