import os

from security_analyzer import analyze_file


def choose_encryption_method(file_path):

    result = analyze_file(file_path)

    file_size_mb = result["size"]
    risk_level = result["risk"]

    extension = os.path.splitext(
        file_path
    )[1].lower()

    # Large files -> ChaCha20
    if file_size_mb > 100:
        return {
            "algorithm": "CHACHA20",
            "reason":
            "Large files encrypt faster using ChaCha20."
        }

    # Video files -> ChaCha20
    if extension in [
        ".mp4",
        ".avi",
        ".mkv",
        ".mov"
    ]:
        return {
            "algorithm": "CHACHA20",
            "reason":
            "Video files are better suited for stream encryption."
        }

    # High risk files -> AES + RSA
    if risk_level == "High":
        return {
            "algorithm": "AES_RSA",
            "reason":
            "High risk files require stronger hybrid encryption."
        }

    # Text files -> AES + RSA
    if extension in [
        ".txt",
        ".doc",
        ".docx",
        ".pdf"
    ]:
        return {
            "algorithm": "AES_RSA",
            "reason":
            "Documents are protected using AES + RSA."
        }

    # Images -> AES + RSA
    if extension in [
        ".png",
        ".jpg",
        ".jpeg"
    ]:
        return {
            "algorithm": "AES_RSA",
            "reason":
            "Image files are encrypted using AES + RSA."
        }

    # Default
    return {
        "algorithm": "AES_RSA",
        "reason":
        "Default secure encryption selected."
    }


def security_agent(file_path):

    analysis = analyze_file(
        file_path
    )

    decision = choose_encryption_method(
        file_path
    )

    return {
        "file_type":
        analysis["type"],

        "file_size":
        analysis["size"],

        "risk_level":
        analysis["risk"],

        "security_score":
        analysis["score"],

        "algorithm":
        decision["algorithm"],

        "reason":
        decision["reason"]
    }