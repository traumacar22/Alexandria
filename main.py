from entry import Entry
from storage import *
import sys
import os


#in memory
file_path = "safe/vault.json"
if os.path.exists(file_path):
    entries = load_entry()
else:
    entries = []



#menu loop
while True:
    response = input("1) Add entry,2) View entries, or 3) Quit?")
    if response == "3":
        sys.exit()
    elif response == "1":
        site = input("What Website or service is this login is for?")
        pword = input("What is your password?")
        email = input("What is the email you are going to use? (optional)")
        uname = input("What is the username you are going to use? (optional)")
        entry = Entry(site, pword, email, uname)
        entries.append(entry)
        save_entry(entries)
    elif response == "2":
        for entry in entries: 
            print(entry)
    else:
        print("input not recognized")