from mysocket import openSocket, sendMessage
from init import joinRoom
from read import getUser, getMessage
import string
import os
import json

chatlog = False
s = openSocket()
joinRoom(s)
readbuffer = ""

while True:
	# persist = True

	readbuffer = readbuffer + s.recv(1024)
	temp = string.split(readbuffer, "\n")
	readbuffer = temp.pop()

	for line in temp:
		if "PING :tmi.twitch.tv" in line:
			pong = line.replace("PING", "PONG")
			print(pong)
			s.send(pong)
		if "PRIVMSG" in line:
			# print(line)
			user = getUser(line)
			message = getMessage(line)
			print(user + " typed: " + message)

			if "@thesealion" in message:
			#and (user != 'thesealion95'):
				#print('HELLO HELLO HELLO')
				#os.system('say "Beer time."');
				print('\a\a\a')
				f = open('alerts.txt', 'a')
				f.write(message + '\n')
				f.close()
			#if chatlog is True:

		#sendMessage(s, "Hello @" + user)
		# if "JOIN" in line:
		# 	# print(line)
		# 	sendMessage(s, "Welcome!")