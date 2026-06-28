import customtkinter as ctk

from database import (
register_account,
user_exists
)

def register_page(root, login_page):


    frame = ctk.CTkFrame(root)
    frame.pack(expand=True)

    ctk.CTkLabel(
        frame,
        text="📝 Create Account",
        font=("Segoe UI", 28, "bold")
    ).pack(pady=(30, 10))

    ctk.CTkLabel(
        frame,
        text="Register to use Encryptor Pro",
        font=("Segoe UI", 14)
    ).pack(pady=(0, 20))

    error_label = ctk.CTkLabel(
        frame,
        text="",
        text_color="red"
    )
    error_label.pack()

    ctk.CTkLabel(
        frame,
        text="Username"
    ).pack(pady=(10, 5))

    username = ctk.CTkEntry(
        frame,
        width=280,
        placeholder_text="Enter Username"
    )
    username.pack()

    ctk.CTkLabel(
        frame,
        text="Password"
    ).pack(pady=(15, 5))

    password = ctk.CTkEntry(
        frame,
        width=280,
        show="*",
        placeholder_text="Enter Password"
    )
    password.pack()

    ctk.CTkLabel(
        frame,
        text="Confirm Password"
    ).pack(pady=(15, 5))

    confirm_password = ctk.CTkEntry(
        frame,
        width=280,
        show="*",
        placeholder_text="Confirm Password"
    )
    confirm_password.pack()

    def toggle_password():

        if password.cget("show") == "*":

            password.configure(show="")
            confirm_password.configure(show="")
            show_btn.configure(text="Hide")

        else:

            password.configure(show="*")
            confirm_password.configure(show="*")
            show_btn.configure(text="Show")

    show_btn = ctk.CTkButton(
        frame,
        text="Show",
        width=80,
        command=toggle_password
    )
    show_btn.pack(pady=10)

    def register():

        user = username.get().strip()
        pwd = password.get().strip()
        confirm = confirm_password.get().strip()

        if not user:

            error_label.configure(
                text="Username Required",
                text_color="red"
            )
            return

        if not pwd:

            error_label.configure(
                text="Password Required",
                text_color="red"
            )
            return

        if pwd != confirm:

            error_label.configure(
                text="Passwords Do Not Match",
                text_color="red"
            )
            return

        if user_exists(user):

            error_label.configure(
                text="Username Already Exists",
                text_color="red"
            )
            return

        register_account(
            user,
            pwd
        )

        error_label.configure(
            text="Account Created Successfully",
            text_color="green"
        )

        username.delete(0, "end")
        password.delete(0, "end")
        confirm_password.delete(0, "end")

    username.bind(
        "<Return>",
        lambda event: register()
    )

    password.bind(
        "<Return>",
        lambda event: register()
    )

    confirm_password.bind(
        "<Return>",
        lambda event: register()
    )

    ctk.CTkButton(
        frame,
        text="Create Account",
        width=280,
        height=40,
        command=register
    ).pack(pady=(20, 10))

    ctk.CTkButton(
        frame,
        text="Back To Login",
        width=280,
        height=40,
        fg_color="gray30",
        command=lambda: [
            frame.destroy(),
            login_page()
        ]
    ).pack(pady=(0, 30))

