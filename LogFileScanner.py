import os
import time
import Mailer

# Set the filename and open the file
filename = 'server.log'
filepath = '/usr/local/jboss/server/abbino/log/' + filename
file = open(filepath, 'r')

searchStrings = ["FATAL", "OutOfMemory"]

# Find the size of the file and move to the end
st_results = os.stat(filepath)
st_size = st_results[6]
file.seek(st_size)


def scanFile():
    while 1:
        # where = file.tell()  # current position of the reader
        line = file.readline()  # read next line
        while line:
            checkLine(line)  # already has newline
            line = file.readline()  # read next line
        if not line:
            time.sleep(1)


def checkLine(line):
    for searchString in searchStrings:
        if searchString in line:
            notifyTeam(line)


def notifyTeam(line):
    Mailer.sendMicrosoftTeamsMessage("Error Detected in Line: " + line)


scanFile()
