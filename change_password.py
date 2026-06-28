import customtkinter as ctk
from tkinter import messagebox

from database import (
    verify_password,
    reset_password
)

def change_password_page(
root,
username,
dashboard_page,
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
        text="🔐 Security Settings",
        font=("Segoe UI", 28, "bold")
    ).pack(pady=(30, 10))

    ctk.CTkLabel(
        frame,
        text="Update your account password securely",
        font=("Segoe UI", 14)
    ).pack(pady=(0, 20))

    card = ctk.CTkFrame(
        frame,
        width=450,
        height=350
    )
    card.pack(pady=20)

    ctk.CTkLabel(
        card,
        text="Current Password"
    ).pack(pady=(25, 5))

    old_password = ctk.CTkEntry(
        card,
        width=300,
        show="*"
    )
    old_password.pack()

    ctk.CTkLabel(
        card,
        text="New Password"
    ).pack(pady=(15, 5))

    new_password = ctk.CTkEntry(
        card,
        width=300,
        show="*"
    )
    new_password.pack()

    ctk.CTkLabel(
        card,
        text="Confirm Password"
    ).pack(pady=(15, 5))

    confirm_password = ctk.CTkEntry(
        card,
        width=300,
        show="*"
    )
    confirm_password.pack()

    show_var = False

    def toggle_password():

        nonlocal show_var

        if show_var:

            old_password.configure(show="*")
            new_password.configure(show="*")
            confirm_password.configure(show="*")
            show_var = False

        else:

            old_password.configure(show="")
            new_password.configure(show="")
            confirm_password.configure(show="")
            show_var = True

    ctk.CTkButton(
        card,
        text="👁 Show / Hide Password",
        width=220,
        command=toggle_password
    ).pack(pady=15)

    def update_password():

        if not verify_password(
                username,
                old_password.get()
        ):

            messagebox.showerror(
                "Error",
                "Current Password Incorrect"
            )
            return

        if new_password.get() != confirm_password.get():

            messagebox.showerror(
                "Error",
                "Passwords Do Not Match"
            )
            return

        if len(new_password.get()) < 6:

            messagebox.showerror(
                "Error",
                "Password must be at least 6 characters"
            )
            return

        reset_password(
            username,
            new_password.get()
        )

        messagebox.showinfo(
            "Success",
            "Password Changed Successfully"
        )

        frame.destroy()

        dashboard_page(
            root,
            username,
            login_page
        )

    ctk.CTkButton(
        card,
        text="🔄 Update Password",
        width=250,
        height=40,
        command=update_password
    ).pack(pady=10)

    ctk.CTkButton(
        frame,
        text="⬅ Back",
        width=220,
        command=lambda:[
            frame.destroy(),
            dashboard_page(
                root,
                username,
                login_page
            )
        ]
    ).pack(pady=20)

