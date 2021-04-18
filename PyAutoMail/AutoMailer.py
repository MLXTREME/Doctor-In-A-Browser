"""
python PyAutoMail/AutoMailer.py
"""

import os
import sys
from email.message import EmailMessage
import smtplib, ssl,email
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from email import encoders
from email.mime.base import MIMEBase

def addtoPath(directory):
    for root, subdirectories, files in os.walk(directory):
        for subdirectory in subdirectories:
            #print(os.path.join(root, subdirectory))
            sys.path.append(os.path.join(root, subdirectory))

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
addtoPath(ROOT_DIR)

from Passwords.Save_Password import read_user_details


def read_file(TemplatePath):
    with open(TemplatePath) as f:
        message = f.read()
    return message


def send_email(MailDetails):
    EmailAdd = UserDetails["Email"] #senders Gmail id over here
    Pass = UserDetails["Password"] #senders Gmail's Password over here 

    msg = EmailMessage()
    msg['From'] = EmailAdd
    msg['Subject'] = MailDetails['Subject'] # Subject of Email
    msg['To'] = MailDetails['To'] # Reciver of the Mail
    msg.set_content(MailDetails['Body']) # Email body or Content

    #### >> Code from here will send the message << ####
    with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp: #Added Gmails SMTP Server
        smtp.login(EmailAdd,Pass) #This command Login SMTP Library using your GMAIL
        smtp.send_message(msg) #This Sends the message

def send_email_fancy(MailDetails):
    EmailAdd = UserDetails["Email"] #senders Gmail id over here
    Pass = UserDetails["Password"] #senders Gmail's Password over here 

    msg = MIMEMultipart("alternative")
    msg['From'] = EmailAdd
    msg['Subject'] = MailDetails['Subject'] # Subject of Email
    msg['To'] =  ', '.join(MailDetails['To'])
    
    # Reciver of the Mail
    # Turn these into plain/html MIMEText objects
    TemplateNameTXT = "Plain_Mail.txt"
    TemplateFolderTXT = "Templates"
    TemplatePathTXT = os.path.join(ROOT_DIR,TemplateFolderTXT, TemplateNameTXT)
    
    part1 = MIMEText(read_file(TemplatePathTXT), "plain")
    part2 = MIMEText(MailDetails['Body'],"html")
    
    msg.attach(part1)
    msg.attach(part2)
    
    
    # msg.attach(MIMEText(MailDetails['Body'],"html")) # Email body or Content
    
    # Create secure connection with server and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(EmailAdd,Pass)
        server.sendmail(EmailAdd, MailDetails["To"], msg.as_string()) 

def send_email_attach(MailDetails):
    EmailAdd = UserDetails["Email"] #senders Gmail id over here
    Pass = UserDetails["Password"] #senders Gmail's Password over here 

    msg = MIMEMultipart()
    msg['From'] = EmailAdd
    msg['Subject'] = MailDetails['Subject'] # Subject of Email
    msg['To'] =  ', '.join(MailDetails['To'])
    """
    message["Bcc"] = receiver_email  # Recommended for mass emails
    """
    # Reciver of the Mail
    # Turn these into plain/html MIMEText objects
    TemplateNameTXT = "Plain_Mail.txt"
    TemplateFolderTXT = "Templates"
    TemplatePathTXT = os.path.join(ROOT_DIR,TemplateFolderTXT, TemplateNameTXT)
    
    part1 = MIMEText(read_file(TemplatePathTXT), "plain")
    part2 = MIMEText(MailDetails['Body'],"html")
    
    # msg.attach(part1)
    msg.attach(part2)
    
    
    filename = MailDetails['AttachmentPath']  # In same directory as script

    # Open PDF file in binary mode
    with open(filename, "rb") as attachment:
        # Add file as application/octet-stream
        # Email client can usually download this automatically as attachment
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

    # Encode file in ASCII characters to send by email    
    encoders.encode_base64(part)
    FileBaseName = os.path.basename(filename)
    # Add header as key/value pair to attachment part
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {FileBaseName}",
    )

    # Add attachment to message and convert message to string
    msg.attach(part)
    # msg.attach(MIMEText(MailDetails['Body'],"html")) # Email body or Content
    
    # Create secure connection with server and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(EmailAdd,Pass)
        server.sendmail(EmailAdd, MailDetails["To"], msg.as_string()) 



if __name__ == "__main__":
    """
    Simple Mails
    """
    """
    TemplateName = "Plain_Mail.txt"
    TemplateFolder = "Templates"
    UserDetails = read_user_details()

    TemplatePath = os.path.join(ROOT_DIR,TemplateFolder, TemplateName)
    MailDetails = {
                    "Subject": "Wow! I can text using Python.",
                    "To":      ['damikdhar@gmail.com','njrfarhandasilva10@gmail.com'],
                    "Body" :   read_file(TemplatePath)
                    }
    send_email(MailDetails)
    """
    
    """
    Fancy Email
    """
    
    """
    TemplateName = "MLXTREME_Template_Stripo.html"
    TemplateFolder = "Templates"
    UserDetails = read_user_details()

    TemplatePath = os.path.join(ROOT_DIR,TemplateFolder, TemplateName)
    MailDetails = {
                    "Subject": "Wow! I can text using Python.",
                    "To":      ['damikdhar@gmail.com','njrfarhandasilva10@gmail.com','nirmalya14misra@gmail.com','swaymsdennings@gmail.com'],
                    "Body" :   read_file(TemplatePath)
                    }
    send_email_fancy(MailDetails)
    """
    
    """
    Attached Fancy Email
    """
    
    """
    TemplateName = "MLXTREME_Template_Stripo.html"
    TemplateFolder = "Templates"
    UserDetails = read_user_details()

    TemplatePath = os.path.join(ROOT_DIR,TemplateFolder, TemplateName)
    MailDetails = {
                    "Subject": "Wow! I can text using Python.",
                    "To":      ['damikdhar@gmail.com','njrfarhandasilva10@gmail.com','nirmalya14misra@gmail.com','swaymsdennings@gmail.com'],
                    "Body" :   read_file(TemplatePath),
                    "AttachmentPath" : "PyAutoMail/Sample_PDF.pdf"
                    }
    send_email_attach(MailDetails)
    """
    """
    Attached Fancy Email - Python File Attached
    """
    
    TemplateName = "MLXTREME_Template_Stripo.html"
    TemplateFolder = "Templates"
    UserDetails = read_user_details()

    TemplatePath = os.path.join(ROOT_DIR,TemplateFolder, TemplateName)
    MailDetails = {
                    "Subject": "New Mail Sent using Python",
                    "To":      ['damikdhar@gmail.com','njrfarhandasilva10@gmail.com','nirmalya14misra@gmail.com','swaymsdennings@gmail.com'],
                    "Body" :   read_file(TemplatePath),
                    "AttachmentPath" : "PyAutoMail/AutoMailer.py"
                    }
    send_email_attach(MailDetails)
    
    