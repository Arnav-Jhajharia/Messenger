import pandas as pd
import smtplib


# email = input("Enter your email address: ")
# text = input("Enter text: ")
# sender = "jhajhariaarnav@gmail.com"

cred = pd.read_csv("credentials.txt")
user = cred.columns[0]
password = cred.columns[1]


def vigenere(text, key):
    key_ord = []
    for a in key:
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


def send_mail(user, pas):
    email = input("Enter your email address: ")
    text = input("Enter text: ")
    key = input("Enter key: ").upper()
    encr, key = vigenere(text, key)
    encr += ',' + key
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(user, pas)
    s.sendmail(user, email, encr)
    s.quit()





send_mail(user, password)