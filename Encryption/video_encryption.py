import os
from tkinter import messagebox

from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.Random import get_random_bytes

from hash_utils import calculate_hash
from database import save_hash

from keys import load_public_key
from database import save_history
from security_analyzer import analyze_file


CHUNK_SIZE = 64 * 1024


def encrypt_video_file(file_path, username):

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
    
    # Prevent double encryption
    with open(file_path, "rb") as f:
        header = f.read(13)

    if header == b"ENCRYPTOR_PRO":
        messagebox.showwarning(
            "Already Encrypted",
            "This video is already encrypted."
        )
        return False

    session_key = get_random_bytes(32)

    cipher_aes = AES.new(
        session_key,
        AES.MODE_CTR
    )

    nonce = cipher_aes.nonce

    rsa_key = load_public_key()

    cipher_rsa = PKCS1_OAEP.new(
        rsa_key
    )

    encrypted_session_key = cipher_rsa.encrypt(
        session_key
    )

    temp_path = file_path + ".tmp"

    original_hash = calculate_hash(file_path)

    save_hash(
        username,
        os.path.basename(file_path),
        original_hash
    )

    with open(file_path, "rb") as fin, open(temp_path, "wb") as fout:

        fout.write(b"ENCRYPTOR_PRO")
        fout.write(
            len(encrypted_session_key).to_bytes(
                4,
                "big"
            )
        )

        fout.write(encrypted_session_key)
        fout.write(nonce)

        while True:

            chunk = fin.read(CHUNK_SIZE)

            if not chunk:
                break

            fout.write(
                cipher_aes.encrypt(chunk)
            )

    os.remove(file_path)
    os.rename(temp_path, file_path)

    try:
        # encryption code here
        save_history(
            username,
            os.path.basename(file_path),
            "Image",
            "Encrypt"
        )

        return True

    except Exception as e:
        messagebox.showerror(
            "Encryption Error",
            str(e)
        )
        return False