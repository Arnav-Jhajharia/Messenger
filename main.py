import pandas as pd
import smtplib



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
    email = []  
    print("These are you default recipients")
    qw = -1
    for key, value in cred2.iteritems():
        qw += 1
        print(str(qw) + ".", key)
    qa = input("To send to any one of them, press 1: ")
    if qa == "1":
        print("Enter the number associated with the participants, press exit when you're done. ")
        while True:
            u = input()
            if u == "exit":
                break
            email += [cred2.columns[int(u)]]
            

    print("Enter other emails, press enter to exit")
    a = "-"
    while a != "":
        a = input()

        if "@" in a:
            email += [a]     
       
    b = (input("Enter 0 if you want to send default message and 1 to read from here: "))
    if b == "1":
        text = input("Enter text: ")
        

        c = (input("Do you want this to be your default message: Press 1 for yes and anything else for no:"))
        if c == "1":
            hi, o = vigenere(text, cred.columns[2])
            f = open("message.txt", "w")
            f.write(hi)
            f.close()
            
    elif b == "0":
        text = open("message.txt", "r").read()
        text = idontknow(text, cred.columns[2])
    key = input("Enter key(enter a if you want to send the code in non-encrytped form): ").upper()
    encr, key = vigenere(text, key)
    if key != "A":
        encr += ',' + key
    
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(user, pas)
    s.sendmail(user, email, encr)
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
  for part in msg.walk():
     b = part.get_payload()
     body = b.rstrip("\r\n").split(",")
     try: 
        decr = idontknow(body[0], body[1])
        print("The decrypted message was: " +decr)
     except IndexError:
        decr = body[0]
        print("The message was" + decr)
    


action = int(input("Press 1 to send, 0 to receive: "))
if action == 1:
    send_mail(user, password)
    print("Email Successfully sent in encrypted form")
elif action == 0:
    fetch_mail(user, password)

