import json
from entry import Entry
from cryptography.fernet import Fernet, InvalidToken


def save_entry(new_list: list[Entry], fernet):
    entries = []
    for i in new_list:
        entries.append(i.to_dict())
    stage1 = json.dumps(entries)
    encrypted = fernet.encrypt(stage1.encode())

    with open("safe/vault.json", 'wb') as vault:
        vault.write(encrypted)



def load_entry(fernet):
    loaded_list: list[Entry] = []
    try:
        with open("safe/vault.json", 'rb') as vault:
            Fer = fernet.decrypt(vault.read())
            data = json.loads(Fer)
            
    except (json.JSONDecodeError, FileNotFoundError):
        return []
    for entry in data:
        loaded_list.append(Entry.from_dict(entry))
    return loaded_list