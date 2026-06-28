from Crypto.Cipher import ChaCha20
from Crypto.Random import get_random_bytes

import os
from tkinter import messagebox

from hash_utils import calculate_hash
from database import save_hash, save_history

def encrypt_chacha_file(file_path, username):

    if not os.path.exists(file_path):
        messagebox.showerror(
            "File Error",
            "File does not exist."
        )
        return False

    if os.path.getsize(file_path) == 0:
        messagebox.showerror(
            "File Error",
            "Cannot encrypt an empty file."
        )
        return False

    with open(file_path, "rb") as f:
        header = f.read(12)

    if header == b"CHACHA20_PRO":
        messagebox.showwarning(
            "Already Encrypted",
            "This file is already encrypted."
        )
        return False

    with open(file_path, "rb") as f:
        plaintext = f.read()

    key = get_random_bytes(32)

    cipher = ChaCha20.new(key=key)

    ciphertext = cipher.encrypt(plaintext)

    save_hash(
        username,
        os.path.basename(file_path),
        calculate_hash(file_path)
    )

    with open(file_path, "wb") as f:

        f.write(b"CHACHA20_PRO")
        f.write(key)
        f.write(cipher.nonce)
        f.write(ciphertext)

    save_history(
        username,
        os.path.basename(file_path),
        "Text",
        "ChaCha20 Encrypt"
    )
    return True
