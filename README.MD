# Alexandria

A local, terminal-based password manager. No cloud, no accounts — your vault is a single encrypted file on your own machine, unlocked with one master password.

This is a personal/learning project, currently at V1.

## Features

- Add entries (website/service, password, optional email, optional username)
- View all saved entries
- Search entries by website/service name (case-insensitive, partial match)
- Vault is encrypted at rest using Fernet (AES-based authenticated encryption from the `cryptography` library)
- Master password is never stored — a key is derived from it on the fly each run via PBKDF2-HMAC-SHA256, and verified by attempting to decrypt the vault

## How it works

- On first run, you'll be asked to create and confirm a master password. This generates a random salt (`safe/salt.bin`) and an empty vault.
- On later runs, you'll be prompted for your master password once. If it doesn't decrypt the vault, you get one retry before the program exits.
- Your master password + the salt are run through PBKDF2 (480,000 iterations) to derive a key, which becomes your Fernet encryption key for the session. The password itself is never written to disk.
- Entries are stored as JSON, encrypted as a whole, and written to `safe/vault.json`.

## Requirements

- Python 3
- See `requirements.txt` (mainly the `cryptography` package)

## Setup

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Usage

```bash
python main.py
```

You'll be prompted for your master password (created on first run), then dropped into a menu:

```
1) Add entry
2) View entries
3) Search for an entry
4) Quit
```

## Project structure

- `main.py` — entry point; handles password/salt setup and the menu loop
- `entry.py` — `Entry` class representing a single saved login
- `storage.py` — encrypted read/write of `safe/vault.json`
- `crypto.py` — salt generation/loading, key derivation, and building the `Fernet` instance
- `safe/` — holds `vault.json` (encrypted entries) and `salt.bin`; gitignored except for a `.gitkeep`

## Security notes

- The master password is never persisted anywhere; it only exists in memory for the run, just long enough to derive the key.
- Losing your master password means losing access to the vault — there's no recovery path by design.
- The salt is not secret, but it must persist across runs; deleting `safe/salt.bin` while keeping `safe/vault.json` will make the vault undecryptable even with the correct password.

## Roadmap / possible future features

- Loop the wrong-password retry instead of capping at one retry
- Edit and delete existing entries
- Convert `email`/`username` defaults consistently to `None` everywhere they're unset (in progress)
- Clipboard copy for passwords instead of printing them to the terminal
- Global hotkey to launch the app in a terminal window (similar to the Windows Snipping Tool shortcut) — likely a V2 stretch goal, since it requires a separate background listener process outside Python's normal run/exit model and is OS-specific
- Password generator for creating new entries
- Master password change/rotation (re-encrypt vault under a new key)
