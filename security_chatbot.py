def get_response(question):

    question = question.lower()

    if "aes" in question:
        return "AES is a symmetric encryption algorithm used for fast and secure data protection."

    elif "rsa" in question:
        return "RSA is an asymmetric encryption algorithm used to securely exchange encryption keys."

    elif "encryption" in question:
        return "Encryption converts readable data into unreadable ciphertext."

    elif "password" in question:
        return "Use strong passwords with letters, numbers, and symbols."

    return "I am your Security Assistant. Please ask a cybersecurity question."