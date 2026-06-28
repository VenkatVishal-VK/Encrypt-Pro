from Crypto.Cipher import ChaCha20
import os
from tkinter import messagebox

from hash_utils import calculate_hash
from database import get_hash, save_history

def decrypt_chacha_file(file_path, username):

    if not os.path.exists(file_path):
        messagebox.showerror(
            "File Error",
            "File does not exist."
        )
        return False

    if os.path.getsize(file_path) == 0:
        messagebox.showerror(
            "File Error",
            "Selected file is empty."
        )
        return False

    MAGIC = b"CHACHA20_PRO"

    with open(file_path, "rb") as f:

        header = f.read(len(MAGIC))

        if header != MAGIC:
            messagebox.showerror(
                "Invalid File",
                "This file was not encrypted using ChaCha20."
            )
            return False

        key = f.read(32)

        nonce = f.read(8)

        ciphertext = f.read()

    try:

        cipher = ChaCha20.new(
            key=key,
            nonce=nonce
        )

        plaintext = cipher.decrypt(
            ciphertext
        )

    except Exception as e:

        messagebox.showerror(
            "Decryption Error",
            str(e)
        )

        return False

    with open(file_path, "wb") as f:
        f.write(plaintext)

    current_hash = calculate_hash(file_path)

    stored_hash = get_hash(
        username,
        os.path.basename(file_path)
    )

    if stored_hash:

        if current_hash == stored_hash:

            messagebox.showinfo(
                "Integrity Check",
                "✓ File Integrity Verified"
            )

        else:

            messagebox.showwarning(
                "Integrity Check",
                "⚠ File Has Been Modified"
            )

    save_history(
        username,
        os.path.basename(file_path),
        "ChaCha20",
        "Decrypt"
    )

    return True

