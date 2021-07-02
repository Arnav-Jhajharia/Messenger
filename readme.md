# CLI Messenger for transfer of messages in encrypted format
- End-to-end text transfer and viewing. 
- Gmail used as agent. 


## Steps needed  for setup
1. Go [here](https://myaccount.google.com/lesssecureapps?pli=1&rapt=AEjHL4OB0tZ7ZJARqV-_kI_ePvVpf-MQGOxWf7Sol2BjdsfWBNzIMPoavfdbUY_zGwV17bhPyJTLKJKYE5VrU2egh9F4zBxP-A) and turn on Less Secure Apps.
2. Go [here](https://mail.google.com/mail/u/0/?tab=rm&ogbl#settings/fwdandpop) and "Enable IMAP"
3. Download the repository, and make sure you have python installed.
4. Enter this in terminal for setup
```
pip3 install pandas
python setup.py

```
5. To edit any of the details:
```
python edit.py
```
# Use 

- Enter this 
```
python main.py
```
- Note - Enter gmail credentials *only*
- Tips and tricks
    - All your details are stored in your local computer in credentials.txt, message.txt and recipients.txt
    - Enter 
    ```
        notepad credentials.txt
        notepad message.txt
        notepad recipients.txt

    ``` 
    - That will let you manually add/remove details!!

    - You can send emails in encrypted form and decrypt sent emails(with the same messenger). 
    - To send non-encrypted emails, enter "a" when prompted for key
    



## Version 1.1
### Features 
- New edit panel
- Save your recipients
- Slight redeisgn






