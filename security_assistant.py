import customtkinter as ctk
from tkinter import filedialog as fd

from security_analyzer import analyze_file


def get_response(question):

    question = question.lower()

    if "aes" in question:
        return (
            "AES-256 is used in Encryptor Pro for fast and secure "
            "file encryption. AES encrypts the actual file data."
        )

    elif "rsa" in question:
        return (
            "RSA is used to encrypt the AES session key. "
            "This creates our hybrid AES + RSA architecture."
        )

    elif "chacha" in question:
        return (
            "ChaCha20 is recommended for large files and videos "
            "because it provides high performance while maintaining "
            "strong security."
        )

    elif "manual encryption" in question:
        return (
            "Manual Encryption allows you to choose:\n\n"
            "• Text Encryption\n"
            "• Image Encryption\n"
            "• Video Encryption\n"
            "• ChaCha20 Encryption"
        )

    elif "manual decryption" in question:
        return (
            "Manual Decryption allows you to restore:\n\n"
            "• Text Files\n"
            "• Images\n"
            "• Videos\n"
            "• ChaCha20 Files"
        )

    elif "ai encrypt" in question:
        return (
            "AI Encrypt automatically analyzes:\n\n"
            "• File type\n"
            "• File size\n"
            "• Sensitivity\n"
            "• Risk level\n\n"
            "Then selects AES+RSA or ChaCha20 automatically."
        )

    elif "ai decrypt" in question:
        return (
            "AI Decrypt automatically detects the encryption "
            "algorithm and restores the original file securely."
        )

    elif "history" in question:
        return (
            "The History module stores:\n\n"
            "• Filename\n"
            "• Operation\n"
            "• Timestamp\n"
            "• Algorithm Used"
        )

    elif "supported files" in question:
        return (
            "Encryptor Pro currently supports:\n\n"
            "📝 Text Files\n"
            "🖼 Images\n"
            "🎥 Videos"
        )

    elif "high risk" in question:
        return (
            "High-risk files contain sensitive information such as:\n\n"
            "• Financial data\n"
            "• Personal information\n"
            "• Password databases\n"
            "• Medical records\n\n"
            "Encryptor Pro recommends AES+RSA for these files."
        )

    elif "algorithm" in question:
        return (
            "Encryptor Pro supports:\n\n"
            "🔐 AES + RSA Hybrid Encryption\n"
            "⚡ ChaCha20 Encryption"
        )

    elif "security score" in question:
        return (
            "Security Score is calculated using:\n\n"
            "• File sensitivity\n"
            "• File type\n"
            "• File size\n"
            "• Risk level"
        )

    elif "encryption process" in question:
        return (
            "Encryption Process:\n\n"
            "1. Generate AES key\n"
            "2. Encrypt file using AES\n"
            "3. Encrypt AES key using RSA\n"
            "4. Save encrypted package"
        )

    elif "decryption process" in question:
        return (
            "Decryption Process:\n\n"
            "1. Load RSA private key\n"
            "2. Recover AES key\n"
            "3. Decrypt file using AES\n"
            "4. Restore original file"
        )

    return (
        "You can ask me about:\n\n"
        "• AES Encryption\n"
        "• RSA Encryption\n"
        "• ChaCha20\n"
        "• AI Encryption\n"
        "• AI Decryption\n"
        "• Manual Encryption\n"
        "• History\n"
        "• Supported Files\n"
        "• Security Scores\n"
        "• Encryption Process"
    )

def security_assistant(
        root,
        username,
        dashboard_page,
        login_page
):

    frame = ctk.CTkFrame(root)
    frame.pack(fill="both", expand=True, padx=20, pady=20)

    ctk.CTkLabel(
        frame,
        text="🤖 AI Security Assistant",
        font=("Segoe UI", 28, "bold")
    ).pack(pady=(20, 10))

    chat_box = ctk.CTkTextbox(
        frame,
        width=850,
        height=420
    )
    chat_box.pack(
        padx=20,
        pady=10,
        fill="both",
        expand=True
    )

    chat_box.insert(
        "end",
        "🤖 Assistant:\nHello! Upload a file or ask a security question.\n\n"
    )

    bottom_frame = ctk.CTkFrame(frame)
    bottom_frame.pack(fill="x", padx=20, pady=10)

    question_entry = ctk.CTkEntry(
        bottom_frame,
        placeholder_text="Ask about AES, RSA, Encryption..."
    )

    question_entry.pack(
        side="left",
        fill="x",
        expand=True,
        padx=10
    )

    def ask():

        question = question_entry.get().strip()

        if not question:
            return

        answer = get_response(question)

        chat_box.insert(
            "end",
            f"👤 You:\n{question}\n\n"
        )

        chat_box.insert(
            "end",
            f"🤖 Assistant:\n{answer}\n\n"
        )

        chat_box.see("end")
        question_entry.delete(0, "end")

    def upload_file():

       
        file_path = fd.askopenfilename()

        if not file_path:
            return

        result = analyze_file(file_path)

        recommended_algorithm = "AES + RSA Hybrid Encryption"
        recommendation_reason = ""

        # Large videos -> ChaCha20
        if "video" in result["type"].lower() and result["size"] > 100:
            recommended_algorithm = "ChaCha20 Encryption"
            recommendation_reason = (
                "This is a large video file, so Encryptor Pro selected "
                "ChaCha20 for faster encryption and decryption."
            )

        # Very large files -> ChaCha20
        elif result["size"] > 500:
            recommended_algorithm = "ChaCha20 Encryption"
            recommendation_reason = (
                "This file is very large, so Encryptor Pro selected "
                "ChaCha20 to improve speed without reducing security."
            )

        # High-risk files -> AES + RSA
        elif result["risk"] == "HIGH":
            recommended_algorithm = "AES + RSA Hybrid Encryption"
            recommendation_reason = (
                "This file may contain sensitive or confidential data, "
                "so Encryptor Pro selected AES + RSA for maximum protection."
            )

        # Default recommendation
        else:
            recommended_algorithm = "AES + RSA Hybrid Encryption"
            recommendation_reason = (
                "AES + RSA provides the best balance of security and "
                "compatibility for this type of file."
            )

        # Show only the chosen algorithm explanation
        if "ChaCha20" in recommended_algorithm:

            protection_message = """

        ⚡ Why ChaCha20 was selected

        This file is large or media-heavy.

        ChaCha20 is much faster for large videos and files while still
        providing strong security.

        This means less waiting time during encryption and decryption.
        """
        else:

            protection_message = """

        🔒 Why AES + RSA was selected

        This file may contain important or sensitive information.

        AES + RSA provides stronger protection for confidential files,
        documents, and personal data.

        Only authorized users with the correct keys can access the file.
        """
        chat_box.insert(
            "end",
            f"""
        📂 Uploaded File Analysis

        File Type:
        {result['type']}

        File Size:
        {result['size']} MB

        Risk Level:
        {result['risk']}

        Security Score:
        {result['score']}/100

        ━━━━━━━━━━━━━━━━━━━━━━

        🔐 Recommended Protection
        {recommended_algorithm}
        Why was this selected?
        {recommendation_reason}

        ━━━━━━━━━━━━━━━━━━━━━━
        {protection_message}

        ━━━━━━━━━━━━━━━━━━━━━━
        """
        )
        chat_box.see("end")
    ctk.CTkButton(
        bottom_frame,
        text="📂 Upload",
        width=120,
        command=upload_file
    ).pack(side="left", padx=5)

    ctk.CTkButton(
        bottom_frame,
        text="➤ Send",
        width=120,
        command=ask
    ).pack(side="left", padx=5)

    question_entry.bind(
        "<Return>",
        lambda event: ask()
    )

    ctk.CTkButton(
        frame,
        text="⬅ Back",
        width=220,
        command=lambda: [
            frame.destroy(),
            dashboard_page(
                root,
                dashboard_page,
                username,
                login_page
            )
        ]
    ).pack(pady=15)