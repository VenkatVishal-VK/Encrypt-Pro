import customtkinter as ctk

from ai_encrypt_menu import ai_encrypt
from ai_decrypt_menu import ai_decrypt


def ai_menu(
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
        text="🤖 AI Security Agent",
        font=("Segoe UI", 28, "bold")
    ).pack(pady=(20, 10))

    ctk.CTkLabel(
        frame,
        text="Automatic encryption and decryption using AI decisions",
        font=("Segoe UI", 14)
    ).pack(pady=(0, 20))

    button_frame = ctk.CTkFrame(frame)
    button_frame.pack(pady=20)

    encrypt_btn = ctk.CTkButton(
        button_frame,
        text="🤖\nAI Encrypt",
        width=220,
        height=120,
        font=("Segoe UI", 18, "bold"),
        command=lambda: ai_encrypt(username)
    )

    decrypt_btn = ctk.CTkButton(
        button_frame,
        text="🤖\nAI Decrypt",
        width=220,
        height=120,
        font=("Segoe UI", 18, "bold"),
        command=lambda: ai_decrypt(username)
    )

    encrypt_btn.grid(
        row=0,
        column=0,
        padx=20,
        pady=20
    )

    decrypt_btn.grid(
        row=0,
        column=1,
        padx=20,
        pady=20
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
                username,
                login_page
            )
        ]
    ).pack(pady=20)