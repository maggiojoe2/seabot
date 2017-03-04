#!/usr/bin/python3
import socket
from settings import HOST, PORT, PASS, NICK, CHANNEL

def openSocket():
	
	s = socket.socket()
	s.connect((HOST, PORT))
	s.send("PASS " + PASS + "\r\n")
	s.send("NICK " + NICK + "\r\n")
	s.send("CAP REQ :twitch.tv/membership \r\n")
	s.send("JOIN #" + CHANNEL + ",#seab0t95" + "\r\n")
	return s

def sendMessage(s, message):
	messagetemp = "PRIVMSG #" + CHANNEL + " :" + message
	s.send(messagetemp + "\r\n")
	print("Sent: " + messagetemp)