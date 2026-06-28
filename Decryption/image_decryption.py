import os
import numpy as np
from PIL import Image
from tkinter import messagebox

from Crypto.Cipher import AES, PKCS1_OAEP

from hash_utils import calculate_hash
from database import get_hash

from keys import load_private_key
from database import save_history


def decrypt_image_file(file_path, username):

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

        header = f.read(13)

        if header != b"ENCRYPTOR_PRO":
            messagebox.showerror(
                "Invalid File"
            )
            return

        key_len = int.from_bytes(
            f.read(4),
            "big"
        )

        encrypted_session_key = f.read(key_len)

        nonce = f.read(16)
        tag = f.read(16)

        width = int.from_bytes(
            f.read(4),
            "big"
        )

        height = int.from_bytes(
            f.read(4),
            "big"
        )

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

    except Exception:
        messagebox.showerror(
            "Decryption Error",
            "Invalid or corrupted encrypted image."
        )
        return

    image_array = np.frombuffer(
        plaintext,
        dtype=np.uint8
    ).reshape(
        (height, width, 3)
    )

    image = Image.fromarray(image_array,"RGB")

    ext = os.path.splitext(file_path)[1].lower()

    if ext in [".jpg", ".jpeg"]:
        temp_path = file_path + ".tmp.jpg"
        image.save(temp_path, format="JPEG")
    elif ext == ".png":
        temp_path = file_path + ".tmp.png"
        image.save(temp_path, format="PNG")
    else:
        raise ValueError("Unsupported image format")
    
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

    print("Image restored successfully")

    save_history(
        username,
        os.path.basename(file_path),
        "Image",
        "Decrypt"
    )

    return os.path.basename(file_path)