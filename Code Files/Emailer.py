from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText
import smtplib
import os

#create a SMTP connection using googles servers with a premade gmail account
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
GMAIL_USERNAME = 'trupro42@gmail.com'
GMAIL_PASSWORD = 'wfadxammsiwlyfed'

#Function takes 3 parameters, recipient, subject and the content
#builds the message and then opens and attaches the data of our file to our email body
#finally establishes a connection to the SMTP server, logs in to gmail and then sends our email and deletes the file allowing for fresh data collection
def sendmail(recipient, subject, content):
    msg = MIMEMultipart()
    body_part = MIMEText(content, 'plain')
    
    msg['Subject'] = subject
    msg['From'] = GMAIL_USERNAME
    msg['To'] = recipient
    
    msg.attach(body_part)
    
    
    with open('tempData.csv', 'rb') as file:
        msg.attach(MIMEApplication(file.read(), Name='tempData.csv'))
        
    #Connect to gmail server
    session = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    session.ehlo()
    session.starttls()
    session.ehlo()
    
    #login to gmail
    session.login(GMAIL_USERNAME, GMAIL_PASSWORD)
    
    #send the email and quit
    session.sendmail(msg['From'], msg['To'], msg.as_string())
    session.quit
    
    #delete the file after sending it
    if os.path.exists('tempData.csv'):
        os.remove('tempData.csv')
    else:
        print("The file does not exist")