import customtkinter as ctk

from encryption_menu import encryption_menu
from decryption_menu import decryption_menu
from security_assistant import security_assistant


def manual_menu(
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
        text="🛠 Manual Security Center",
        font=("Segoe UI", 28, "bold")
    ).pack(pady=(20, 10))

    ctk.CTkLabel(
        frame,
        text="Choose an operation",
        font=("Segoe UI", 14)
    ).pack(pady=(0, 20))

    card_frame = ctk.CTkFrame(frame)
    card_frame.pack(pady=20)

    encrypt_btn = ctk.CTkButton(
        card_frame,
        text="🔒\nEncryption",
        width=220,
        height=120,
        font=("Segoe UI", 18, "bold"),
        command=lambda:[
            frame.destroy(),
            encryption_menu(
                root,
                manual_menu,
                username,
                login_page
            )
        ]
    )

    decrypt_btn = ctk.CTkButton(
        card_frame,
        text="🔓\nDecryption",
        width=220,
        height=120,
        font=("Segoe UI", 18, "bold"),
        command=lambda:[
            frame.destroy(),
            decryption_menu(
                root,
                manual_menu,
                username,
                login_page
            )
        ]
    )

    ai_btn = ctk.CTkButton(
        card_frame,
        text="🤖\nAI Assistant",
        width=220,
        height=120,
        font=("Segoe UI", 18, "bold"),
        command=lambda:[
            frame.destroy(),
            security_assistant(
                root,
                username,
                manual_menu,
                login_page
            )
        ]
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

    ai_btn.grid(
        row=0,
        column=2,
        padx=20,
        pady=20
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
                username,
                login_page
            )
        ]
    ).pack(pady=20)