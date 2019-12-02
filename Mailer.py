import logging
import pymsteams

connectorCard = "https://outlook.office.com/webhook/64e5918b-4481-4afd-9a3d-9e58a791a2d8@b79b5471-e1ff-402e-9d2f-325e42c29942/IncomingWebhook/b0f0b5bf882446548a52b6374c02a5ab/ba84cd1b-7ec2-4986-bf39-86a6f0a0119f"


def sendMicrosoftTeamsMessage(msg):
    myTeamsMessage = pymsteams.connectorcard(connectorCard)
    # Add text to the message.
    myTeamsMessage.text(msg)
    # send the message.
    myTeamsMessage.send()


def sendMessageToDevs(msg):
    logging.info("Sending Messages")
    # TODO: send Email to Deployer

    sendMicrosoftTeamsMessage(msg)

    # sender_email = "deployer@nicando.de"
    # receiver_email = "your@gmail.com"
    # password = input("Type your password and press enter:")
    #
    # message = MIMEMultipart("alternative")
    # message["Subject"] = "multipart test"
    # message["From"] = sender_email
    # message["To"] = receiver_email
    #
    # # Create the plain-text and HTML version of your message
    # text = """\
    # Hi,
    # How are you?
    # Real Python has many great tutorials:
    # www.realpython.com"""
    # html = """\
    # <html>
    #   <body>
    #     <p>Hi,<br>
    #        How are you?<br>
    #        <a href="http://www.realpython.com">Real Python</a>
    #        has many great tutorials.
    #     </p>
    #   </body>
    # </html>
    # """
    #
    # # Turn these into plain/html MIMEText objects
    # part1 = MIMEText(text, "plain")
    # part2 = MIMEText(html, "html")
    #
    # # Add HTML/plain-text parts to MIMEMultipart message
    # # The email client will try to render the last part first
    # message.attach(part1)
    # message.attach(part2)
    #
    # # Create secure connection with server and send email
    # context = ssl.create_default_context()
    # with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    #     server.login(sender_email, password)
    #     server.sendmail(
    #         sender_email, receiver_email, message.as_string()
    #     )
