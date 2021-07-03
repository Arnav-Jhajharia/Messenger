import os

import pandas as pd
import smtplib
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import random
import subprocess

from email.message import EmailMessage
idd = str(random.randint(1, 1000000))
idd += ".csv"

def vigenere(text, key):
    key_ord = []
    for a in key.upper():
        key_ord.append(ord(a))
    # print(key_ord)
    b = 0
    j = 0
    final = ""
    for i in text:
        b = ord(i)
        # print(i)
        if (b < 65 or b > 90) and (b < 97 or b > 122):
            final += i
        if (b >= 65 and b <= 90):
            final += chr((ord(i) - 65 + key_ord[(j % len(key))] - 65) % 26 + 65)
            j = j + 1
        if (b >= 97 and b <= 122):
            final += chr((ord(i) - 97 + key_ord[(j % len(key))] - 65) % 26 + 97)
            j = j + 1
    return final, key
# email = input("Enter your email address: ")
# text = input("Enter text: ")
# sender = "jhajhariaarnav@gmail.com"
cred = pd.read_csv("credentials.txt")
user = cred.columns[0]
password = cred.columns[1]
key = cred.columns[2]
# inp = input("Enter how you want to give your credentials: ").lower()
# spl = inp.split(" ")
cred2 = pd.read_csv("recipients.txt")
def idontknow(text, key):
    key_ord = []
    for a in key.upper():
        key_ord.append(ord(a))
    # print(key_ord)
    b = 0
    j = 0
    final = ""
    for i in text:
        b = ord(i)
        # print(i)
        if (b < 65 or b > 90) and (b < 97 or b > 122):
            final += i
        if (b >= 65 and b <= 90):
            final += chr((ord(i) - 65 - key_ord[(j % len(key))] - 65) % 26 + 65)
            j = j + 1
        if (b >= 97 and b <= 122):
            final += chr((ord(i) - 97 - key_ord[(j % len(key))] - 65) % 26 + 97)
            j = j + 1
    return final




def send_mail(user, pas):
    message = EmailMessage()
    message["Subject"] = input("Enter subject: ")
    message["From"] = user
    message["To"] = input("Enter recipient's email address: ")
    path = input("Enter image path: ")
    seed = int(input("Enter seed "))
    w = input("Enter a message to send with image: ")
    message.set_content(str(seed) + "," + w)
    img = np.array(Image.open(path).convert('L'))

    np.random.seed(seed)
    ai = np.random.randint(0, 256,size=img.shape) * 10
    encr = img + ai

    df = pd.DataFrame(encr)
    csv = df.to_csv(index=False)
    message.add_attachment(csv.encode('utf-8'), maintype='text', subtype='csv', filename=idd)


    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(user, pas)
    s.send_message(message)
    s.quit()
   



user = idontknow(user, key)
password = idontknow(password, key)

def fetch_mail(u, p): 
  import imaplib
  import email
  imap = imaplib.IMAP4_SSL("imap.gmail.com")
  imap.login(u, p)
  imap.select('"[Gmail]/All Mail"', readonly = True)
  response, messages = imap.search(None, 'UnSeen')
  messages = messages[0].split()
  latest = int(messages[-1])
  res, msg = imap.fetch(str(latest), "(RFC822)")
  for mail in msg:
     if isinstance(mail, tuple):
        msg = email.message_from_bytes(mail[1])

        yo = 2   
        w = 0
  for part in msg.walk():
        
        try:
                        # get the email body
            body = part.get_payload(decode=True).decode()
        except:
            pass
        content_type = part.get_content_type()
        content_disposition = str(part.get("Content-Disposition"))
        if content_type == "text/plain" and "attachment" not in content_disposition:
                        # print text/plain emails and skip attachments
                        body = body.rstrip("\r\n").split(",")
                        yo = int(body[0])
                        print(body[1])
        # this part comes from the snipped I don't understand yet... 
        if part.get_content_maintype() == 'multipart':
            continue
        if part.get('Content-Disposition') is None:
            continue
        fileName = part.get_filename()
        
        if bool(fileName):
                
            filePath = os.path.join('/Users/jhajh/crypto/8Final/YTSProject/Image/CSV', fileName)
            if not os.path.isfile(filePath) :
                fp = open(filePath, 'wb')
                fp.write(part.get_payload(decode=True))
                fp.close()
            subject = str(msg).split("Subject: ", 1)[1].split("\nTo:", 1)[0]
            df = pd.read_csv(filePath)
            arr = df.values #Convert csv to numpy array
            np.random.seed(yo)
            r = 10*np.random.randint(0,256,size=arr.shape)
            final = arr-r
            plt.imshow(final, 'gray')
            plt.show()
  


action = int(input("Press 1 to send, 0 to receive: "))
if action == 1:
    send_mail(user, password)
    print("Email Successfully sent in encrypted form")
elif action == 0:
    fetch_mail(user, password)

