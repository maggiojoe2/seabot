#!/usr/local/bin/python2.7
import socket
from settings import HOST, PORT, PASS, NICK, CHANNEL

def openSocket():

    s = socket.socket()
    s.connect((HOST, PORT))
    s.send("PASS " + PASS + "\r\n")
    s.send("NICK " + NICK + "\r\n")
    s.send("CAP REQ :twitch.tv/membership \r\n")
    s.send("CAP REQ :twitch.tv/commands \r\n")
    s.send("JOIN #" + CHANNEL + "\r\n")
    return s
