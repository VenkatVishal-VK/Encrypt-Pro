import customtkinter as ctk
from tkinter import filedialog as fd
from tkinter import messagebox
import time

from Decryption.text_decryption import decrypt_text_file
from Decryption.image_decryption import decrypt_image_file
from Decryption.video_decryption import decrypt_video_file
from Decryption.chacha_decryption import decrypt_chacha_file

from progress_window import ProgressWindow

def chacha_decrypt(username):

    file_path = fd.askopenfilename()

    if not file_path:
        return

    progress = ProgressWindow(
        "Decrypting ChaCha20 File..."
    )

    try:

        for i in range(101):
            progress.update(i)
            time.sleep(0.01)

        success = decrypt_chacha_file(
            file_path,
            username
        )

        progress.close()

        if success:
            messagebox.showinfo(
                "Success",
                "File Decrypted Successfully"
            )

    except Exception as e:

        progress.close()

        messagebox.showerror(
            "Decryption Error",
            str(e)
        )

def text_decrypt(username):

    file_path = fd.askopenfilename(
        filetypes=[("Text Files", "*.txt")]
    )

    if not file_path:
        return

    progress = ProgressWindow(
        "Decrypting Text File..."
    )

    try:

        for i in range(101):
            progress.update(i)
            time.sleep(0.01)

        success = decrypt_text_file(
            file_path,
            username
        )

        progress.close()

        if success:
            messagebox.showinfo(
                "Success",
                "Text File Decrypted Successfully"
            )

    except Exception as e:

        progress.close()

        messagebox.showerror(
            "Decryption Error",
            str(e)
        )

def image_decrypt(username):

    file_path = fd.askopenfilename(
        filetypes=[
            ("Images", "*.png *.jpg *.jpeg")
        ]
    )

    if not file_path:
        return

    progress = ProgressWindow(
        "Decrypting Image..."
    )

    try:

        for i in range(101):
            progress.update(i)
            time.sleep(0.01)

        success = decrypt_image_file(
            file_path,
            username
        )

        progress.close()

        if success:
            messagebox.showinfo(
                "Success",
                "Image Decrypted Successfully"
            )

    except Exception as e:

        progress.close()

        messagebox.showerror(
            "Decryption Error",
            str(e)
        )

def video_decrypt(username):

    file_path = fd.askopenfilename(
        filetypes=[
            ("Videos",
             "*.mp4 *.avi *.mkv *.mov")
        ]
    )

    if not file_path:
        return

    progress = ProgressWindow(
        "Decrypting Video..."
    )

    try:

        for i in range(101):
            progress.update(i)
            time.sleep(0.02)

        success = decrypt_video_file(
            file_path,
            username
        )

        progress.close()

        if success:
            messagebox.showinfo(
                "Success",
                "Video Decrypted Successfully"
            )

    except Exception as e:

        progress.close()

        messagebox.showerror(
            "Decryption Error",
            str(e)
        )


def decryption_menu(
    root,
    dashboard_page,
    username,
    login_page):

    frame = ctk.CTkFrame(root)
    frame.pack(
        fill="both",
        expand=True,
        padx=20,
        pady=20
    )

    ctk.CTkLabel(
        frame,
        text="🔓 Decryption Center",
        font=("Segoe UI", 28, "bold")
    ).pack(pady=(20, 5))

    ctk.CTkLabel(
        frame,
        text="Restore encrypted files securely",
        font=("Segoe UI", 14)
    ).pack(pady=(0, 20))

    card_frame = ctk.CTkFrame(frame)
    card_frame.pack(pady=20)

    text_btn = ctk.CTkButton(
        card_frame,
        text="📝\nText Decryption",
        width=220,
        height=120,
        font=("Segoe UI", 18, "bold"),
        command=lambda: text_decrypt(username)
    )

    image_btn = ctk.CTkButton(
        card_frame,
        text="🖼️\nImage Decryption",
        width=220,
        height=120,
        font=("Segoe UI", 18, "bold"),
        command=lambda: image_decrypt(username)
    )

    video_btn = ctk.CTkButton(
        card_frame,
        text="🎥\nVideo Decryption",
        width=220,
        height=120,
        font=("Segoe UI", 18, "bold"),
        command=lambda: video_decrypt(username)
    )

    chacha_btn = ctk.CTkButton(
        card_frame,
        text="⚡\nChaCha20 Decryption",
        width=220,
        height=120,
        font=("Segoe UI", 18, "bold"),
        command=lambda: chacha_decrypt(username)
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
        command=lambda:[
            frame.destroy(),
            dashboard_page(
                root,
                dashboard_page,
                username,
                login_page
            )
        ]
    ).pack(pady=20)

