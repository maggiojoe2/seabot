#!/usr/local/bin/python2.7

def getUser(line):
    """ Get user name """

    separate = line.split(":", 2)
    user = separate[1].split("!", 1)[0]
    return user

def getMessage(line):
    """ Get message text """

    separate = line.split(":", 2)
    message = separate[2]
    return message
