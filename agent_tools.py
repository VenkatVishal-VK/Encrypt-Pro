from Encryption.text_encryption import encrypt_text_file
from Encryption.image_encryption import encrypt_image_file
from Encryption.video_encryption import encrypt_video_file
from Encryption.chacha_encryption import encrypt_chacha_file

from Decryption.text_decryption import decrypt_text_file
from Decryption.image_decryption import decrypt_image_file
from Decryption.video_decryption import decrypt_video_file
from Decryption.chacha_decryption import decrypt_chacha_file

from security_analyzer import analyze_file

def encrypt_file(file_path, username, method):
    if method == "AES_TEXT":
        return encrypt_text_file(file_path, username)

    elif method == "AES_IMAGE":
        return encrypt_image_file(file_path, username)

    elif method == "AES_VIDEO":
        return encrypt_video_file(file_path, username)

    elif method == "CHACHA20":
        return encrypt_chacha_file(file_path, username)


def decrypt_file(file_path, username, method):
    if method == "AES_TEXT":
        return decrypt_text_file(file_path, username)

    elif method == "AES_IMAGE":
        return decrypt_image_file(file_path, username)

    elif method == "AES_VIDEO":
        return decrypt_video_file(file_path, username)

    elif method == "CHACHA20":
        return decrypt_chacha_file(file_path, username)


def analyze_security(file_path):
    return analyze_file(file_path)