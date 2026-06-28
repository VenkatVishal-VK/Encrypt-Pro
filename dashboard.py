import customtkinter as ctk
from tkinter import messagebox

from manual_menu import manual_menu
from ai_menu import ai_menu

from history import history_page
from database import delete_account
from change_password import change_password_page

def dashboard(root, username, login_page):


    frame = ctk.CTkFrame(root)
    frame.pack(fill="both", expand=True, padx=20, pady=20)

    ctk.CTkLabel(
        frame,
        text="🔐 Encrypt Pro",
        font=("Segoe UI", 28, "bold")
    ).pack(pady=(20, 5))

    ctk.CTkLabel(
        frame,
        text=f"Welcome, {username}",
        font=("Segoe UI", 16)
    ).pack(pady=(0, 20))

    # ---------------- STATS ---------------- #

    stats_frame = ctk.CTkFrame(frame)
    stats_frame.pack(pady=10)

    ctk.CTkLabel(
        stats_frame,
        text="AES for Data • RSA for Keys • ChaCha20 for Speed",
        font=("Segoe UI", 14, "bold")
    ).pack(padx=20, pady=10)

# ---------------- BUTTON GRID ---------------- #

    button_frame = ctk.CTkFrame(frame)
    button_frame.pack(pady=20)

    buttons = [
    ("🛠 Manual Encrypt", lambda:[
        frame.destroy(),
        manual_menu(
            root,
            dashboard,
            username,
            login_page
        )
    ]),

    ("🤖 AI Automatic Encrypt", lambda:[
        frame.destroy(),
        ai_menu(
            root,
            dashboard,
            username,
            login_page
        )
    ]),

    ("📜 History", lambda:[
        frame.destroy(),
        history_page(
            root,
            username,
            dashboard,
            login_page
        )
    ]),

    ("🔑 Change Password", lambda:[
        frame.destroy(),
        change_password_page(
            root,
            username,
            dashboard,
            login_page
        )
    ])
    ]

    row = 0
    col = 0

    for text, cmd in buttons:

        btn = ctk.CTkButton(
            button_frame,
            text=text,
            width=220,
            height=80,
            font=("Segoe UI", 14, "bold"),
            command=cmd
        )

        btn.grid(
            row=row,
            column=col,
            padx=15,
            pady=15
        )

        col += 1

        if col == 2:
            col = 0
            row += 1

    # ---------------- DELETE ACCOUNT ---------------- #

    def delete_user():

        answer = messagebox.askyesno(
            "Delete Account",
            "Are you sure you want to delete your account?"
        )

        if answer:

            delete_account(username)

            frame.destroy()

            login_page()

    ctk.CTkButton(
        frame,
        text="🗑 Delete Account",
        fg_color="red",
        hover_color="#990000",
        width=220,
        height=40,
        command=delete_user
    ).pack(pady=(20, 10))

    ctk.CTkButton(
        frame,
        text="🚪 Logout",
        width=220,
        height=40,
        command=lambda:[
            frame.destroy(),
            login_page()
        ]
    ).pack(pady=(0, 20))

