import os
from tkinter import filedialog as fd
from tkinter import messagebox

from Decryption.text_decryption import decrypt_text_file
from Decryption.image_decryption import decrypt_image_file
from Decryption.video_decryption import decrypt_video_file
from Decryption.chacha_decryption import decrypt_chacha_file

def ai_decrypt(username):

    file_path = fd.askopenfilename()

    if not file_path:
        return

    try:

        with open(file_path, "rb") as f:
            header = f.read(20)

        algorithm = None
        reason = ""

        if header.startswith(b"ENCRYPTOR_PRO"):

            algorithm = "AES + RSA"

            extension = os.path.splitext(
                file_path
            )[1].lower()

            if extension == ".txt":
                file_type = "Text"

            elif extension in [
                ".png",
                ".jpg",
                ".jpeg"
            ]:
                file_type = "Image"

            else:
                file_type = "Video"

            reason = (
                "Detected Encryptor Pro header. "
                "Using AES + RSA decryption."
            )

        elif header.startswith(b"CHACHA20_PRO"):

            algorithm = "ChaCha20"
            file_type = "Generic File"

            reason = (
                "Detected ChaCha20 header. "
                "Using ChaCha20 decryption."
            )

        else:

            messagebox.showerror(
                "AI Agent",
                "Unknown encryption format."
            )
            return

        proceed = messagebox.askyesno(
            "AI Security Agent",
            f"""

    Detected Encryption:
    {algorithm}

    Detected File Type:
    {file_type}

    Reason:
    {reason}

    Proceed with decryption?
    """
    )

        if not proceed:
            return

        if algorithm == "ChaCha20":

            success = decrypt_chacha_file(
                file_path,
                username
            )

        else:

            if file_type == "Text":

                success = decrypt_text_file(
                    file_path,
                    username
                )

            elif file_type == "Image":

                success = decrypt_image_file(
                    file_path,
                    username
                )

            else:

                success = decrypt_video_file(
                    file_path,
                    username
                )

        if success:

            messagebox.showinfo(
                "AI Agent",
                f"""


    Decryption Successful

    Algorithm Used:
    {algorithm}

    File:
    {os.path.basename(file_path)}
    """
    )


    except Exception as e:

        messagebox.showerror(
            "AI Decryption Error",
            str(e)
        )