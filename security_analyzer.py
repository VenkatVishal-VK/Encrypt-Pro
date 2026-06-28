import os
import tkinter as t
from tkinter import filedialog as fd


def analyze_file(file_path):

    size_mb = os.path.getsize(file_path) / (1024 * 1024)

    ext = os.path.splitext(file_path)[1].lower()

    file_info = {

        # Documents
        ".txt": ("Text File", "AES + RSA",
                 ["Protects confidential text",
                  "Prevents unauthorized reading"]),

        ".pdf": ("PDF Document", "AES + RSA",
                 ["Protects business documents",
                  "Prevents document leakage"]),

        ".doc": ("Word Document", "AES + RSA",
                 ["Protects editable documents",
                  "Prevents unauthorized modification"]),

        ".docx": ("Word Document", "AES + RSA",
                  ["Protects editable documents",
                   "Prevents unauthorized modification"]),

        # Images
        ".jpg": ("JPEG Image", "AES + RSA",
                 ["Protects personal images",
                  "Prevents image theft"]),

        ".jpeg": ("JPEG Image", "AES + RSA",
                  ["Protects personal images",
                   "Prevents image theft"]),

        ".png": ("PNG Image", "AES + RSA",
                 ["Protects personal images",
                  "Prevents image theft"]),

        ".gif": ("GIF Image", "AES + RSA",
                 ["Protects media content",
                  "Prevents unauthorized access"]),

        # Videos
        ".mp4": ("MP4 Video", "AES + RSA",
                 ["Protects video content",
                  "Prevents unauthorized viewing"]),

        ".avi": ("AVI Video", "AES + RSA",
                 ["Protects video content",
                  "Prevents unauthorized viewing"]),

        ".mkv": ("MKV Video", "AES + RSA",
                 ["Protects video content",
                  "Prevents unauthorized viewing"]),

        ".mov": ("MOV Video", "AES + RSA",
                 ["Protects video content",
                  "Prevents unauthorized viewing"]),

        # Audio
        ".mp3": ("MP3 Audio", "AES + RSA",
                 ["Protects audio recordings",
                  "Prevents unauthorized copying"]),

        ".wav": ("WAV Audio", "AES + RSA",
                 ["Protects audio recordings",
                  "Prevents unauthorized copying"]),

        # Archives
        ".zip": ("ZIP Archive", "AES + RSA",
                 ["Protects compressed files",
                  "Secures bundled data"]),

        ".rar": ("RAR Archive", "AES + RSA",
                 ["Protects compressed files",
                  "Secures bundled data"]),

        # Code
        ".py": ("Python File", "AES + RSA",
                ["Protects source code",
                 "Prevents intellectual property theft"]),

        ".java": ("Java File", "AES + RSA",
                  ["Protects source code",
                   "Prevents intellectual property theft"]),

        ".cpp": ("C++ File", "AES + RSA",
                 ["Protects source code",
                  "Prevents intellectual property theft"]),

        # Spreadsheet
        ".xls": ("Excel Spreadsheet", "AES + RSA",
                 ["Protects financial data",
                  "Prevents data leakage"]),

        ".xlsx": ("Excel Spreadsheet", "AES + RSA",
                  ["Protects financial data",
                   "Prevents data leakage"]),

        ".csv": ("CSV Data File", "AES + RSA",
                 ["Protects structured data",
                  "Prevents unauthorized access"])
    }

    if ext in file_info:
        file_type, algorithm, effects = file_info[ext]
    else:
        file_type = f"{ext.upper()[1:]} File" if ext else "Unknown File"
        algorithm = "AES + RSA"
        effects = [
            "General file protection",
            "Prevents unauthorized access"
        ]

    # ---------------- SECURITY SCORE ----------------

    score = 50

    # Sensitive business files
    if ext in [".xlsx", ".xls", ".csv", ".pdf", ".doc", ".docx"]:
        score += 40

    # Source code files
    elif ext in [".py", ".java", ".cpp"]:
        score += 25

    # Text files
    elif ext in [".txt"]:
        score += 20

    # Images
    elif ext in [".jpg", ".jpeg", ".png", ".gif"]:
        score += 15

    # Videos
    elif ext in [".mp4", ".avi", ".mkv", ".mov"]:
        score += 10

    # Large files slightly increase score
    if size_mb > 100:
        score += 10

    score = min(score, 100)

    # ---------------- RISK LEVEL ----------------

    if score >= 85:
        risk = "HIGH"
    elif score >= 65:
        risk = "MEDIUM"
    else:
        risk = "LOW"

    return {
        "type": file_type,
        "size": round(size_mb, 2),
        "score": score,
        "risk": risk,
        "algorithm": algorithm,
        "effects": effects
    }


def security_assistant(
    root,
    username,
    dashboard_page,
    login_page
):

    frame = t.Frame(root)
    frame.pack(fill="both", expand=True)

    t.Label(
        frame,
        text="AI Security Assistant",
        font=("Arial", 25)
    ).pack(pady=20)

    response_box = t.Text(
        frame,
        width=70,
        height=20
    )
    response_box.pack(pady=10)

    def analyze_uploaded_file():

        file_path = fd.askopenfilename()

        if not file_path:
            return

        result = analyze_file(file_path)

        response_box.delete("1.0", t.END)

        response_box.insert(
            t.END,
            f"""
File Type:
{result['type']}

File Size:
{result['size']} MB

Risk Level:
{result['risk']}

Security Score:
{result['score']}/100

Recommended Encryption:
{result['algorithm']}

Effects:

- {result['effects'][0]}
- {result['effects'][1]}

Encryption Process:

1. Generate AES Session Key
2. Encrypt File Using AES
3. Encrypt AES Key Using RSA
4. Store Encrypted Data

Decryption Process:

1. Load RSA Private Key
2. Recover AES Session Key
3. Decrypt File Using AES
4. Restore Original File
"""
        )

    t.Button(
        frame,
        text="Upload File",
        width=25,
        command=analyze_uploaded_file
    ).pack(pady=10)

    t.Button(
        frame,
        text="Back",
        width=25,
        command=lambda: [
            frame.destroy(),
            dashboard_page(
                root,
                username,
                login_page
            )
        ]
    ).pack(pady=10)