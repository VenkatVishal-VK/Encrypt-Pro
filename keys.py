from Crypto.PublicKey import RSA
import os

PRIVATE_KEY_PATH = "private.pem"
PUBLIC_KEY_PATH = "public.pem"


def ensure_rsa_keys():

    if not os.path.exists(PRIVATE_KEY_PATH) or not os.path.exists(PUBLIC_KEY_PATH):

        key = RSA.generate(2048)

        with open(PRIVATE_KEY_PATH, "wb") as f:
            f.write(
                key.export_key("PEM")
            )

        with open(PUBLIC_KEY_PATH, "wb") as f:
            f.write(
                key.publickey().export_key("PEM")
            )


def load_private_key():

    with open(PRIVATE_KEY_PATH, "rb") as f:
        return RSA.import_key(
            f.read()
        )


def load_public_key():

    with open(PUBLIC_KEY_PATH, "rb") as f:
        return RSA.import_key(
            f.read()
        )