#!/usr/local/bin/python2.7

import string
#import logging
#from logging.config import fileConfig

def joinRoom(s, logger):
    """ Protocol for joining chat room """

    readbuffer = ""
    loading = True
    while loading:
        readbuffer = readbuffer + s.recv(1024)
        temp = string.split(readbuffer, "\n")
        readbuffer = temp.pop()

        for line in temp:
            logger.debug(line)
            loading = loadingComplete(line)
            if loading != True:
                break

    logger.info('Successfully joined chat!')
    # sendMessage(s, "Successfully joined chat!")

def loadingComplete(line):
    """ Check if bot has finished loading into chat """

    if "End of /NAMES list" in line:
        #print('false')
        return False
    else:
        #print('true')
        return True
