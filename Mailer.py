import logging
import pymsteams

connectorCard = "Teams-Connectorcard"


def sendMicrosoftTeamsMessage(msg):
    myTeamsMessage = pymsteams.connectorcard(connectorCard)
    # Add text to the message.
    myTeamsMessage.text(msg)
    # send the message.
    myTeamsMessage.send()


def sendMessageToDevs(msg):
    logging.info("Sending Messages")
    sendMicrosoftTeamsMessage(msg)
