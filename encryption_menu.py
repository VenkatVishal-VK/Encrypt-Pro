import customtkinter as ctk
from tkinter import filedialog as fd
from tkinter import messagebox
import os

from Encryption.text_encryption import encrypt_text_file
from Encryption.image_encryption import encrypt_image_file
from Encryption.video_encryption import encrypt_video_file
from Encryption.chacha_encryption import encrypt_chacha_file

from security_analyzer import analyze_file
from progress_window import ProgressWindow
import time

def show_analysis(result):


    return messagebox.askyesno(
        "AI Security Analysis",
        f"""

    File Type      : {result['type']}
    File Size      : {result['size']} MB

    Risk Level     : {result['risk']}
    Security Score : {result['score']}/100

    Recommendation:
    AES + RSA Encryption Recommended

    Do you want to continue?
    """
    )

def chacha_encrypt(username):

    file_path = fd.askopenfilename()

    if not file_path:
        return

    progress = ProgressWindow(
        "Encrypting with ChaCha20..."
    )

    try:

        for i in range(101):
            progress.update(i)
            time.sleep(0.01)

        success = encrypt_chacha_file(
            file_path,
            username
        )

        progress.close()

        if success:
            messagebox.showinfo(
                "Success",
                "File Encrypted Successfully using ChaCha20"
            )

    except Exception as e:

        progress.close()

        messagebox.showerror(
            "Encryption Error",
            str(e)
        ) 

def text_encrypt(username):

    file_path = fd.askopenfilename(
        filetypes=[("Text Files", "*.txt")]
    )

    if not file_path:
        return

    result = analyze_file(file_path)

    if not show_analysis(result):
        return
    
    if not os.path.exists(file_path):
        return

    if os.path.getsize(file_path) == 0:
        messagebox.showerror(
            "File Error",
            "Cannot encrypt an empty file."
        )
        return

    progress = ProgressWindow(
        "Encrypting Text File..."
    )

    try:

        for i in range(101):

            progress.update(i)

            time.sleep(0.01)

        success = encrypt_text_file(
            file_path,
            username
        )

        progress.close()

        if success:
            messagebox.showinfo(
                "Success",
                "Text File Encrypted Successfully"
            )

    except Exception as e:

        progress.close()

        messagebox.showerror(
            "Encryption Error",
            str(e)
        )

def image_encrypt(username):

    file_path = fd.askopenfilename(
        filetypes=[
            ("Images", "*.png *.jpg *.jpeg")
        ]
    )

    if not file_path:
        return

    result = analyze_file(file_path)

    if not show_analysis(result):
        return

    progress = ProgressWindow(
        "Encrypting Image..."
    )

    try:

        for i in range(101):
            progress.update(i)
            time.sleep(0.01)

        success = encrypt_image_file(
            file_path,
            username
        )

        progress.close()

        if success:
            messagebox.showinfo(
                "Success",
                "Image Encrypted Successfully"
            )

    except Exception as e:

        progress.close()

        messagebox.showerror(
            "Encryption Error",
            str(e)
        )


def video_encrypt(username):

    file_path = fd.askopenfilename(
        filetypes=[
            ("Videos", "*.mp4 *.avi *.mkv *.mov")
        ]
    )

    if not file_path:
        return

    result = analyze_file(file_path)

    if not show_analysis(result):
        return

    progress = ProgressWindow(
        "Encrypting Video..."
    )

    try:

        for i in range(101):

            progress.update(i)

            time.sleep(0.02)

        success = encrypt_video_file(
            file_path,
            username
        )

        progress.close()

        if success:
            messagebox.showinfo(
                "Success",
                "Video Encrypted Successfully"
            )

    except Exception as e:

        progress.close()

        messagebox.showerror(
            "Encryption Error",
            str(e)
        )


def encryption_menu(
    root,
    dashboard_page,
    username,
    login_page
):

    frame = ctk.CTkFrame(root)

    frame.pack(
        fill="both",
        expand=True,
        padx=20,
        pady=20
    )

    ctk.CTkLabel(
        frame,
        text="🔒 Encryption Center",
        font=("Segoe UI", 28, "bold")
    ).pack(pady=(20, 5))

    ctk.CTkLabel(
        frame,
        text="Select a file type to encrypt",
        font=("Segoe UI", 14)
    ).pack(pady=(0, 20))

    card_frame = ctk.CTkFrame(frame)

    card_frame.pack(
        pady=20
    )

    text_btn = ctk.CTkButton(
        card_frame,
        text="📝\nText Encryption",
        width=220,
        height=120,
        font=("Segoe UI", 18, "bold"),
        command=lambda: text_encrypt(username)
    )

    image_btn = ctk.CTkButton(
        card_frame,
        text="🖼️\nImage Encryption",
        width=220,
        height=120,
        font=("Segoe UI", 18, "bold"),
        command=lambda: image_encrypt(username)
    )

    video_btn = ctk.CTkButton(
        card_frame,
        text="🎥\nVideo Encryption",
        width=220,
        height=120,
        font=("Segoe UI", 18, "bold"),
        command=lambda: video_encrypt(username)
    )

    chacha_btn = ctk.CTkButton(
        card_frame,
        text="⚡\nChaCha20 Encryption",
        width=220,
        height=120,
        font=("Segoe UI", 18, "bold"),
        command=lambda: chacha_encrypt(username)
    )

    chacha_btn = ctk.CTkButton(
card_frame,
text="⚡\nChaCha20 Encryption",
width=220,
height=120,
font=("Segoe UI", 18, "bold"),
command=lambda:
chacha_encrypt(username)
)
    
    text_btn.grid(
        row=0,
        column=0,
        padx=15,
        pady=15
    )

    image_btn.grid(
        row=0,
        column=1,
        padx=15,
        pady=15
    )

    video_btn.grid(
        row=0,
        column=2,
        padx=15,
        pady=15
    )

    chacha_btn.grid(
        row=1,
        column=1,
        padx=15,
        pady=15
    )

    ctk.CTkButton(
        frame,
        text="⬅ Back",
        width=220,
        height=40,
        command=lambda: [
            frame.destroy(),
            dashboard_page(
                root,
                dashboard_page,
                username,
                login_page
            )
        ]
    ).pack(
        pady=20
    )