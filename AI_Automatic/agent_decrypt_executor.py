from Decryption.text_decryption import decrypt_text_file
from Decryption.image_decryption import decrypt_image_file
from Decryption.video_decryption import decrypt_video_file
from Decryption.chacha_decryption import decrypt_chacha_file

import os


def execute_ai_decryption(
    file_path,
    username
):

    with open(file_path, "rb") as f:

        header = f.read(20)

    # Detect ChaCha20 encrypted file
    if b"CHACHA20_PRO" in header:

        success = decrypt_chacha_file(
            file_path,
            username
        )

        return success, {
            "algorithm": "ChaCha20"
        }

    # Detect AES+RSA encrypted files
    elif b"ENCRYPTOR_PRO" in header:

        extension = os.path.splitext(
            file_path
        )[1].lower()

        if extension == ".txt":

            success = decrypt_text_file(
                file_path,
                username
            )

        elif extension in [
            ".png",
            ".jpg",
            ".jpeg"
        ]:

            success = decrypt_image_file(
                file_path,
                username
            )

        elif extension in [
            ".mp4",
            ".avi",
            ".mkv",
            ".mov"
        ]:

            success = decrypt_video_file(
                file_path,
                username
            )

        else:
            success = False

        return success, {
            "algorithm": "AES + RSA"
        }

    return False, {
        "algorithm": "Unknown"
    }