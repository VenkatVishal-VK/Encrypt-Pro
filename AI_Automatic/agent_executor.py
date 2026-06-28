import os

from security_agent import security_agent

from Encryption.text_encryption import encrypt_text_file
from Encryption.image_encryption import encrypt_image_file
from Encryption.video_encryption import encrypt_video_file
from Encryption.chacha_encryption import encrypt_chacha_file


def execute_encryption(file_path, username):

    decision = security_agent(file_path)

    algorithm = decision["algorithm"]

    extension = os.path.splitext(
        file_path
    )[1].lower()

    # AI selected ChaCha20
    if algorithm == "CHACHA20":

        success = encrypt_chacha_file(
            file_path,
            username
        )

    # AI selected AES + RSA
    else:

        if extension == ".txt":

            success = encrypt_text_file(
                file_path,
                username
            )

        elif extension in [
            ".png",
            ".jpg",
            ".jpeg"
        ]:

            success = encrypt_image_file(
                file_path,
                username
            )

        elif extension in [
            ".mp4",
            ".avi",
            ".mkv",
            ".mov"
        ]:

            success = encrypt_video_file(
                file_path,
                username
            )

        else:
            success = False

    return success, decision
