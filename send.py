#!/usr/local/bin/python2.7

from settings import CHANNEL

def sendMessage(s, message):
    """ Send chat message """

    messagetemp = "PRIVMSG #" + CHANNEL + " :" + message
    s.send(messagetemp + "\r\n")
    print "Sent: " + messagetemp

def sendWhisper(s, user, message):
    """ Send Whisper """

    messagetemp = "PRIVMSG #" + CHANNEL + " :" + "/w " + user + " " + message
    s.send(messagetemp + "\r\n")
    print "Sent: " + messagetemp
