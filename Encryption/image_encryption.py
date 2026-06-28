import os
import numpy as np
from tkinter import messagebox

from PIL import Image

from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.Random import get_random_bytes

from hash_utils import calculate_hash
from database import save_hash

from keys import load_public_key
from database import save_history
from security_analyzer import analyze_file

def encrypt_image_file(file_path, username):

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
            "This image is already encrypted."
        )
        return False

    img = Image.open(file_path)

    img = img.convert("RGB")

    img_array = np.array(img)

    plaintext = img_array.tobytes()

    session_key = get_random_bytes(16)

    cipher_aes = AES.new(
        session_key,
        AES.MODE_EAX
    )

    ciphertext, tag = cipher_aes.encrypt_and_digest(
        plaintext
    )

    rsa_key = load_public_key()

    cipher_rsa = PKCS1_OAEP.new(
        rsa_key
    )

    encrypted_session_key = cipher_rsa.encrypt(
        session_key
    )

    original_hash = calculate_hash(file_path)

    save_hash(
        username,
        os.path.basename(file_path),
        original_hash
    )

    with open(file_path, "wb") as f:

        f.write(b"ENCRYPTOR_PRO")
        f.write(
            len(encrypted_session_key).to_bytes(
                4,
                "big"
            )
        )

        f.write(encrypted_session_key)

        f.write(cipher_aes.nonce)

        f.write(tag)

        f.write(
            img.size[0].to_bytes(4, "big")
        )

        f.write(
            img.size[1].to_bytes(4, "big")
        )

        f.write(ciphertext)


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