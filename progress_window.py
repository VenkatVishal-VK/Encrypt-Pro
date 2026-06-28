import customtkinter as ctk


class ProgressWindow:

    def __init__(self, title="Processing"):

        self.window = ctk.CTkToplevel()

        self.window.title(title)
        self.window.geometry("400x150")

        self.label = ctk.CTkLabel(
            self.window,
            text=title,
            font=("Segoe UI", 16, "bold")
        )
        self.label.pack(pady=15)

        self.progress = ctk.CTkProgressBar(
            self.window,
            width=300
        )
        self.progress.pack(pady=10)

        self.progress.set(0)

        self.percent = ctk.CTkLabel(
            self.window,
            text="0%"
        )
        self.percent.pack()

    def update(self, value):

        self.progress.set(value / 100)

        self.percent.configure(
            text=f"{value}%"
        )

        self.window.update()

    def close(self):

        self.window.destroy()