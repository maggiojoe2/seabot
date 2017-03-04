import string
from mysocket import sendMessage

def joinRoom(s):
	readbuffer = ""
	loading = True
	while loading == True:
		readbuffer = readbuffer + s.recv(1024)
		temp = string.split(readbuffer, "\n")
		readbuffer = temp.pop()

		for line in temp:
			loading = loadingComplete(line)
			if loading != True:
				break

	print('Successfully joined chat!')
	# sendMessage(s, "Successfully joined chat!")

def loadingComplete(line):
	if("End of /NAMES list" in line):
		#print('false')
		return False
	else:
		#print('true')
		return True