import pandas as pd
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
cred = pd.read_csv("credentials.txt")

while True:
    
    print("cred - alter credentials")
    print("mess - edit default message")
    print("recep - edit default reciepients")
    print("exit - to exit")
    a = input("Enter what you wanna do:").lower()
    if a == "cred":
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
    elif a == "mess":
        o = vigenere(input("Enter your default message: Press enter for blank: "), cred.columns[2])
        f = open("message.txt", "w")
        f.write(o)
        f.close()
        print("Altered. ")
    elif a == "recep":
        email = ""
        while True:
            a = input("Enter: ")
            if a.lower() == "exit": 
                break
            email += a + ","
            f = open("reciepients.txt", "w").write(email)



    

    
    

