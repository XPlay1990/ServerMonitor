import logging
import os
import socket
import time
import datetime
import Mailer

#####################
#   Logging
#####################
today = '{:%Y-%m-%d_%H-%M-%S}'.format(datetime.datetime.now())
logFileHandler = logging.FileHandler("ServerMonitor_" + today + ".log")
logFileHandler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logFileHandler.setFormatter(formatter)
consoleLogger = logging.StreamHandler()
consoleLogger.setLevel(logging.INFO)
logging.basicConfig(level=logging.DEBUG, handlers=[logFileHandler, consoleLogger])

# Set the filename and open the file
filename = 'server.log'
filepath = '/usr/local/jboss/server/abbino/log/' + filename
file = open(filepath, 'r')

sleepTime = 10

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
            logging.debug("Line found. Reading...")
            checkLine(line)  # already has newline
            line = file.readline()  # read next line
        if not line:
            logging.debug("No Line found. Sleeping...")
            time.sleep(sleepTime)


def checkLine(line):
    for searchString in searchStrings:
        if searchString in line:
            logging.info("Searchterm found. Notifying Team.")
            notifyTeam(line)


def notifyTeam(line):
    Mailer.sendMicrosoftTeamsMessage(socket.gethostname().upper() + " - Error Detected in Line: " + line)


scanFile()
