import customtkinter as ctk

from dashboard import dashboard
from register import register_page
from keys import ensure_rsa_keys

from database import (
create_database,
verify_password
)

# ---------------- THEME ----------------

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# ---------------- ROOT ----------------

root = ctk.CTk()
root.geometry("900x650")
root.title("Encrypt Pro")

create_database()
ensure_rsa_keys()

# ---------------- LOGIN PAGE ----------------

def login_page():

    frame = ctk.CTkFrame(
    root,
    width=400,
    height=500,
    corner_radius=25
    )

    frame.place(
        relx=0.5,
        rely=0.5,
        anchor="center"
    )

    frame.pack_propagate(False)

    ctk.CTkLabel(
        frame,
        text="🔐 Encrypt Pro",
        font=("Segoe UI", 30, "bold")
    ).pack(pady=(30, 10))

    ctk.CTkLabel(
        frame,
        text="Encrypt • Protect • Secure",
        font=("Segoe UI", 14, "bold")
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
        width=250,
        placeholder_text="Enter Username"
    )
    username.pack()

    ctk.CTkLabel(
        frame,
        text="Password"
    ).pack(pady=(15, 5))

    password = ctk.CTkEntry(
        frame,
        width=250,
        placeholder_text="Enter Password",
        show="*"
    )
    password.pack()

    def toggle_password():

        if password.cget("show") == "*":
            password.configure(show="")
            show_btn.configure(text="Hide")
        else:
            password.configure(show="*")
            show_btn.configure(text="Show")

    show_btn = ctk.CTkButton(
        frame,
        text="Show",
        width=70,
        command=toggle_password
    )
    show_btn.pack(pady=10)

    def login():

        if verify_password(
            username.get(),
            password.get()
        ):

            user = username.get()

            frame.destroy()

            dashboard(
                root,
                user,
                login_page
            )

        else:

            error_label.configure(
                text="Invalid Username or Password"
            )

    username.bind(
        "<Return>",
        lambda event: login()
    )

    password.bind(
        "<Return>",
        lambda event: login()
    )

    ctk.CTkButton(
        frame,
        text="Login",
        width=250,
        height=40,
        command=login
    ).pack(pady=(20, 10))

    ctk.CTkButton(
        frame,
        text="Register",
        width=250,
        height=40,
        fg_color="gray30",
        command=lambda: [
            frame.destroy(),
            register_page(
                root,
                login_page
            )
        ]
    ).pack(pady=(0, 30))


login_page()

root.mainloop()
