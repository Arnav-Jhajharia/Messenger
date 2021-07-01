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
inp = input("Enter how you want to give your credentials: ").lower()
spl = inp.split(" ")

while True:
    if "retrieve" in spl or "get" in spl or "file" in spl:
        
        print("Retrieved.")
        break
    elif "enter" in spl or "here" in spl or "type" in spl:
        user = input("Enter email: ")
        password = input("Enter password: ")
        key = input("Enter key: ")
        a = input("Do you want to change the recorded credentials? ")
        if "Yes" in a or a == "Y" or a == "Yep" or a == "Mmhmm" or "Ha" in a:
            user, key = vigenere(user, key)
            password, key = vigenere(password, key)
            f = open("credentials.txt", "w")
            f.write(user + "," + password + "," + key)
            f.close()
            print("Changes successfully made!")
        print("Recorded. ")
        break
    else:
        inp = input("Didn't get you, explain in better terms perhaps?: ").lower()
        spl = inp.split(" ")


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
    aaa = input("Enter 1 to send it to multiple participants, anything else for one: ")
    email = ""
    if aaa == "1":
        print("Enter the emails, press enter to exit")
        a = "-"
        email = []
        while a != "":
            a = input()
            email += [a]            
    else:
        email = input("Enter the reciever's email address: ")
    
    b = int(input("Enter 0 if you want to send default message and 1 to read from here: "))
    if b == 1:
        text = input("Enter text: ")
        

        c = int(input("Do you want this to be your default message: Press 1 for yes and anything else for no:"))
        if c == 1:
            hi, o = vigenere(text, cred.columns[2])
            f = open("message.txt", "w")
            f.write(hi)
            f.close()
            
    elif b == 0:
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
     print(body)
     print(body[0])
     decr = idontknow(body[0], body[1])
     print("The decrypted message was: " + decr)


action = int(input("Press 1 to send, 0 to receive: "))
if action == 1:
    send_mail(user, password)
    print("Email Successfully sent in encryped form")
elif action == 0:
    fetch_mail(user, password)

