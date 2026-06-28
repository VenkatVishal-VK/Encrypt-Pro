import customtkinter as ctk
from tkinter import messagebox

from database import get_history
from pdf_export import export_history_pdf

def export_pdf(username):


    pdf_file = export_history_pdf(username)

    messagebox.showinfo(
        "Success",
        f"PDF Saved:\n{pdf_file}"
    )


def history_page(
root,
username,
dashboard_page,
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
        text="📜 Activity History",
        font=("Segoe UI", 28, "bold")
    ).pack(pady=(20, 10))

    ctk.CTkLabel(
        frame,
        text="Track all encryption and decryption operations",
        font=("Segoe UI", 14)
    ).pack(pady=(0, 20))

    records = get_history(username)

    history_frame = ctk.CTkScrollableFrame(
        frame,
        width=1000,
        height=400
    )
    history_frame.pack(
        padx=20,
        pady=10,
        fill="both",
        expand=True
    )

    header = ctk.CTkFrame(history_frame)
    header.pack(fill="x", pady=(0, 5))

    ctk.CTkLabel(
        header,
        text="File Name",
        width=250
    ).grid(row=0, column=0, padx=10)

    ctk.CTkLabel(
        header,
        text="Type",
        width=100
    ).grid(row=0, column=1, padx=10)

    ctk.CTkLabel(
        header,
        text="Operation",
        width=120
    ).grid(row=0, column=2, padx=10)

    ctk.CTkLabel(
        header,
        text="Timestamp",
        width=250
    ).grid(row=0, column=3, padx=10)

    if not records:

        ctk.CTkLabel(
            history_frame,
            text="No History Found"
        ).pack(pady=20)

    else:

        for file_name, file_type, operation, timestamp in records:

            row = ctk.CTkFrame(history_frame)
            row.pack(
                fill="x",
                pady=3
            )

            ctk.CTkLabel(
                row,
                text=file_name,
                width=250,
                anchor="w"
            ).grid(row=0, column=0, padx=10)

            ctk.CTkLabel(
                row,
                text=file_type,
                width=100
            ).grid(row=0, column=1, padx=10)

            ctk.CTkLabel(
                row,
                text=operation,
                width=120
            ).grid(row=0, column=2, padx=10)

            ctk.CTkLabel(
                row,
                text=timestamp,
                width=250
            ).grid(row=0, column=3, padx=10)

    button_frame = ctk.CTkFrame(frame)
    button_frame.pack(pady=20)

    ctk.CTkButton(
        button_frame,
        text="📄 Export PDF",
        width=180,
        command=lambda:
        export_pdf(username)
    ).pack(
        side="left",
        padx=10
    )

    ctk.CTkButton(
        button_frame,
        text="⬅ Back",
        width=180,
        command=lambda:[
            frame.destroy(),
            dashboard_page(
                root,
                username,
                login_page
            )
        ]
    ).pack(
        side="left",
        padx=10
    )

