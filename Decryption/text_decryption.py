from Crypto.Cipher import AES, PKCS1_OAEP
import os
from tkinter import messagebox

from keys import load_private_key
from database import save_history

from hash_utils import calculate_hash
from database import get_hash

def decrypt_text_file(file_path, username):

    if not os.path.exists(file_path):
        messagebox.showerror(
            "File Error",
            "File does not exist."
        )
        return

    if os.path.getsize(file_path) == 0:
        messagebox.showerror(
            "File Error",
            "Selected file is empty."
        )
        return

    with open(file_path, "rb") as f:

        MAGIC = b"ENCRYPTOR_PRO"

        header = f.read(len(MAGIC))

        if header != MAGIC:
            messagebox.showerror(
                "Invalid File"
            )
            return False

        key_len = int.from_bytes(
            f.read(4),
            "big"
        )

        encrypted_session_key = f.read(
            key_len
        )
        nonce = f.read(16)
        tag = f.read(16)

        ciphertext = f.read()

    rsa_key = load_private_key()

    cipher_rsa = PKCS1_OAEP.new(
        rsa_key
    )

    try:

        session_key = cipher_rsa.decrypt(
            encrypted_session_key
        )

        cipher_aes = AES.new(
            session_key,
            AES.MODE_EAX,
            nonce=nonce
        )

        plaintext = cipher_aes.decrypt_and_verify(
            ciphertext,
            tag
        )

    except Exception as e:
        messagebox.showerror(
            "Decryption Error",
            f"Invalid or corrupted encrypted file.\n\n{e}"
        )
        return False

    with open(file_path, "wb") as f:
        f.write(plaintext)

    current_hash = calculate_hash(file_path)

    stored_hash = get_hash(
        username,
        os.path.basename(file_path)
    )

    if current_hash == stored_hash:

        messagebox.showinfo(
        "Integrity Check",
        "✓ File Integrity Verified"
        )

    else:
        messagebox.showerror(
        "Integrity Check",
        "⚠ File Has Been Modified"
        )

    save_history(
        username,
        os.path.basename(file_path),
        "Text",
        "Decrypt"
    )

    return True