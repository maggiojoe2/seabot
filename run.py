#!/usr/bin/python3

import string
import re
from mysocket import openSocket
from send import sendMessage, sendWhisper
from init import joinRoom
from read import getUser, getMessage
from settings import OWNER

chatlog = False                                     # chatlog setting
run = True                                          # Run setting. Set to false to close program.
s = openSocket()                                    # set up socket for IRC
joinRoom(s)                                         # join channel
readbuffer = ""

while run:                                          # Run until run = False
    readbuffer = readbuffer + s.recv(1024)          # Read messages from IRC line by line
    temp = string.split(readbuffer, "\n")
    readbuffer = temp.pop()

    for line in temp:                               # Output messages to console and check for other instructions
        # print line
        if "PING :tmi.twitch.tv" in line:           # Make sure to PONG when twitch PINGS
            pong = line.replace("PING", "PONG")
            print pong
            s.send(pong)
        elif "PRIVMSG" in line:                       # When the line contains a message from a channel
            user = getUser(line)                    # Parse user name of message sender
            message = getMessage(line)              # Parse message
            print user + " typed: " + message       # Print message to console

            if '@' + OWNER in message:              # Check if owner is tagged in message and add to alerts
                print '\a\a\a'
                f = open('alerts.txt', 'a')
                f.write(user + ': ' + message + '\n')
                f.close()

            if chatlog:
                f = open('chatlog.txt', 'a')
                f.write(user + ': ' + message + '\n')
                f.close()

        elif "WHISPER" in line:                       # When the line contains a whisper from a user
            user = getUser(line)
            message = getMessage(line)
            print user + " WHISPERED: " + message

            regex = re.compile('!logchat.*')
            if regex.match(message):
                if chatlog:
                    chatlog = False
                    sendWhisper(s, user, 'Toggled chatlog off')
                else chatlog:
                    chatlog = True
                    sendWhisper(s, user, 'Toggled chatlog on')
