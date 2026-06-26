this is my first personal project. This is a local pasword manager / creator. The scope for V1 is at a button prompt a window wil popup (terminal?) 
entries will have the following format:
    website: [email] [username] [password]
if an email or username is not needed it will show "None" 

The user will be able to create their own series of inputs to make the app execute and popup onto their screen
all data will be encrypted using python Fernet


Current road map:
Finish Entry — add the email/uname defaults we just talked about, plus a __str__/__repr__ so you can print one cleanly.
Plain storage functions (storage.py) — save_entries(list_of_entries) and load_entries(), working against plain JSON in safe/vault.json. No encryption yet.
Basic CLI loop in main.py — menu-driven: add / view / quit to start (skip search/quit-edge-cases for now). This calls into Entry + storage, giving you an actual program to run and poke at.
Encryption layer — once you can see the loop working end-to-end on plain JSON, swap the storage functions to encrypt/decrypt under the hood.
Search — add as a CLI menu option once the rest is stable.