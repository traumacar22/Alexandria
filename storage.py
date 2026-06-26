import json
from entry import Entry


def save_entry(new_list: list[Entry]):
    entrys = []
    for i in new_list:
        entrys.append(i.to_dict())

    with open("safe/vault.json", 'w') as vault:
        json.dump(entrys, vault)



def load_entry():
    loaded_list: list[Entry] = []
    with open("safe/vault.json", 'r') as vault:
        data = json.load(vault)
    for entry in data:
        loaded_list.append(Entry.from_dict(entry))
    return loaded_list