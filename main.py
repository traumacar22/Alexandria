from entry import Entry
from storage import *
from crypto import *
from getpass import getpass
from cryptography.fernet import Fernet, InvalidToken
import sys
import os

#check salt
salt_path = "safe/salt.bin"
if os.path.exists(salt_path):
    salt = load_salt(salt_path)

    #check master password
    print("Welcome to the Alexandria.")
    Master = getpass(prompt="Use the key: ")
else:
    salt = generate_salt(salt_path)

    #set master password
    Master1 = getpass(prompt="Create your key: ")
    Master2 = getpass(prompt="confirm your key: ")
    if Master2 == Master1:
        Master = Master1
    else:
        print("Keys do not match.")
        input("Press Enter to exit...")
        sys.exit()
        

#create fernet(key)
fernet = get_fernet(Master, salt)

#check to make sure the vault exists if not make it
file_path = "safe/vault.json"
if os.path.exists(file_path):
    try:
        entries = load_entry(fernet)
    except (InvalidToken):
        print("Wrong password")
        try_again = getpass(prompt="Try again:")
        fernet = get_fernet(try_again, salt)
        try:
            entries = load_entry(fernet)
        except (InvalidToken):
            print("failed again. You have been kicked out.")
            input("Press Enter to exit...")
            sys.exit()

else:
    entries = []



#menu loop
while True:
    response = input("1) Add entry, 2) View entries, or 3) Quit?")
    if response == "3":
        sys.exit()
    elif response == "1":
        site = input("What Website or service is this login is for?") 
        pword = input("What is your password?")
        email = input("What is the email you are going to use? (optional)") or None
        uname = input("What is the username you are going to use? (optional)") or None
        entry = Entry(site, pword, email, uname)
        entries.append(entry)
        save_entry(entries, fernet)
    elif response == "2":
        for entry in entries: 
            print(entry)
    else:
        print("input not recognized")