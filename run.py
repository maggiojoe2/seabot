#!/usr/local/bin/python2.7

import time
import string
import re
import logging
from logging.config import fileConfig

from mysocket import openSocket
from send import sendMessage, sendWhisper
from init import joinRoom
from read import getUser, getMessage
from settings import OWNER

fileConfig('logging_conf.ini')                      # set up logger using ini file
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

alertLog = logging.getLogger('alertLog')
chatLog = logging.getLogger('chatLog')

chatlog = False                                     # chatlog setting
run = True                                          # Run setting. Set to false to close program.
s = openSocket()                                    # set up socket for IRC
joinRoom(s, logger)                                         # join channel
readbuffer = ""
# timer = time.time()
# logger.info(timer)

while run:                                          # Run until run = False
    readbuffer = readbuffer + s.recv(1024)          # Read messages from IRC line by line
    temp = string.split(readbuffer, "\n")
    readbuffer = temp.pop()

    for line in temp:                               # Output messages to console and check for other instructions
        # logger.info('here')
        # curtimer = time.time() - timer            # Timer for checking connection
        # logger.info(curtimer)
        # if curtimer >= 10:
        #     logger.info('Ten Seconds.')
        #     timer = time.time()

        logger.info(line)                           # Put line into logger
        if "PING :tmi.twitch.tv" in line:           # Make sure to PONG when twitch PINGS
            pong = line.replace("PING", "PONG")
            pong += "\n\r"
            logger.info('Received ping. Sent: ' + pong)
            s.send(pong)
        elif "PRIVMSG" in line:                     # When the line contains a message from a channel
            user = getUser(line)                    # Parse user name of message sender
            message = getMessage(line)              # Parse message
            #print user + " typed: " + message      # Print message to console

            if '@' + OWNER in message:              # Check if owner is tagged in message and add to alerts
                print '\a\a\a'
                alertLog.info(user + ': ' + message)

            if chatlog:
                chatLog.info(user + ': ' + message)

            # if '!ping' in message:
            #     s.send('PING :tmi.twitch.tv')
            #     logger.info('Sent Ping.')
            #     sendMessage(s, 'Sent Ping.')


        elif "WHISPER" in line:                      # When the line contains a whisper from a user
            user = getUser(line)
            message = getMessage(line)
            # print user + " WHISPERED: " + message

            regex = re.compile('!logchat.*')
            if regex.match(message):
                if chatlog:
                    chatlog = False
                    sendWhisper(s, user, 'Toggled chatlog off\r\n')
                else:
                    chatlog = True
                    sendWhisper(s, user, 'Toggled chatlog on\r\n')

            if message == "!quit\r" and user == OWNER:
                logger.info('closing down')
                s.close()
                run = False
                break

logger.info('Successfully shut down.')
