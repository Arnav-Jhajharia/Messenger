import os

aaaa = input("Few modules needed for execution..  want to install them? answer in y, n: ").lower()
if(aaaa.lower() == "y"):
    os.system("pip install pandas")
    os.system("pip install matplotlib")
    os.system("pip install pillow")
else:
    print("There might be some execution issues, if the modules are not imported")
import pandas as pd
import getpass 

print("Enter your credentials: ")


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
    return final


while True:
    user = input("Enter email: ")
    if "@" in user and not " " in user:
        password = input("Enter password: ") 
        key = input("Enter key:").upper()
        f = open("credentials.txt", "w")
        user = vigenere(user, key)
        password = vigenere(password, key)
        f.write(user + "," + password + "," + key)
        f.close()
        print("Changes successfully made!")
        print("Recorded. ")
        break
    else: 
        print("Enter details correctly lol")
    

o = vigenere(input("Enter your default message: Press enter for blank: "), key)
f = open("message.txt", "w")
f.write(o)
f.close()

print("Enter reciever's email address for later access(if needed), enter exit when you're done: ")
a = input()
email = a
while True:
    a = input()
    if a.lower() == "exit": 
        break
    email +=  "," + a
    f = open("recipients.txt", "w").write(email)
print("List of what you can do")
print("                 Type python image.py to send / receive images")
print("                 Type python main.py to send / receive text messages")
print("                 Type python edit.py to edit details.")
print("                 Type notepad credentials.txt to see your credentials.")
print("                 Type notepad message.txt to see your default message")
print("                 Type notepad recipients.txt to see your default recipients")
print('                 All your details are only stored in encrypted form in your local computer.')
