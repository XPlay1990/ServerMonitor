#!/bin/sh

pkill -f LogFileScanner
cd /home/jboss/servermonitor
/usr/local/bin/python3.6 /home/jboss/servermonitor/LogFileScanner.py &