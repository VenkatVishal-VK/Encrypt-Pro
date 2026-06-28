import os
from tkinter import messagebox

from Crypto.Cipher import AES, PKCS1_OAEP

from hash_utils import calculate_hash
from database import get_hash

from keys import load_private_key
from database import save_history

CHUNK_SIZE = 64 * 1024

def decrypt_video_file(file_path, username):

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

    temp_path = file_path + ".tmp"

    with open(file_path, "rb") as fin:

        header = fin.read(13)

        if header != b"ENCRYPTOR_PRO":
            messagebox.showerror(
                "Invalid File"
            )
            return

        key_len = int.from_bytes(
            fin.read(4),
            "big"
        )

        encrypted_session_key = fin.read(
            key_len
        )

        nonce = fin.read(8)

        rsa_key = load_private_key()

        cipher_rsa = PKCS1_OAEP.new(
            rsa_key
        )

        session_key = cipher_rsa.decrypt(
            encrypted_session_key
        )

        cipher_aes = AES.new(
            session_key,
            AES.MODE_CTR,
            nonce=nonce
        )

        with open(temp_path, "wb") as fout:

            while True:

                chunk = fin.read(CHUNK_SIZE)

                if not chunk:
                    break

                fout.write(
                    cipher_aes.decrypt(chunk)
                )

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

    os.remove(file_path)
    os.rename(temp_path, file_path)

    save_history(
        username,
        os.path.basename(file_path),
        "Video",
        "Decrypt"
    )

    return os.path.basename(file_path)