import os
from tkinter import filedialog as fd
from tkinter import messagebox

from security_analyzer import analyze_file

from Encryption.text_encryption import encrypt_text_file
from Encryption.image_encryption import encrypt_image_file
from Encryption.video_encryption import encrypt_video_file
from Encryption.chacha_encryption import encrypt_chacha_file

def ai_encrypt(username):

    file_path = fd.askopenfilename()

    if not file_path:
        return

    result = analyze_file(file_path)

    extension = os.path.splitext(
        file_path
    )[1].lower()

    algorithm = "AES + RSA"

    reason = ""

    if extension in [
        ".mp4",
        ".avi",
        ".mkv",
        ".mov"
    ]:

        algorithm = "ChaCha20"
        reason = (
            "Large multimedia files encrypt faster "
            "with ChaCha20."
        )

    elif extension in [
        ".png",
        ".jpg",
        ".jpeg"
    ]:

        algorithm = "AES + RSA"
        reason = (
            "Images benefit from integrity "
            "verification using AES-EAX."
        )

    elif extension == ".txt":

        algorithm = "AES + RSA"
        reason = (
            "Text files require strong "
            "confidentiality and integrity."
        )

    else:

        algorithm = "ChaCha20"
        reason = (
            "Unknown file type detected. "
            "Using universal ChaCha20 encryption."
        )

    proceed = messagebox.askyesno(
        "AI Security Agent",
        f"""


    File Type:
    {result['type']}

    File Size:
    {result['size']} MB

    Risk Level:
    {result['risk']}

    AI Selected:
    {algorithm}

    Reason:
    {reason}

    Continue with encryption?
    """
    )


    if not proceed:
        return

    try:

        if algorithm == "ChaCha20":

            success = encrypt_chacha_file(
                file_path,
                username
            )

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

                success = encrypt_chacha_file(
                    file_path,
                    username
                )

        if success:

            messagebox.showinfo(
                "AI Encryption Complete",
                f"""

    Encryption Successful

    Algorithm Used:
    {algorithm}

    File:
    {os.path.basename(file_path)}
    """
    )


    except Exception as e:

        messagebox.showerror(
            "AI Encryption Error",
            str(e)
        )
