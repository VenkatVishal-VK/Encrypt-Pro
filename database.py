import sqlite3
from bcrypt import hashpw, gensalt, checkpw
import bcrypt


def create_database():

    con = sqlite3.connect("account_data.db")
    cursor = con.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
        username TEXT PRIMARY KEY,
        password BLOB,
        phone TEXT
    )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS history(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            filename TEXT,
            filetype TEXT,
            operation TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS file_hashes(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            filename TEXT,
            filehash TEXT
        )
    """)

    con.commit()
    con.close()


def register_account(username, password):

    conn = sqlite3.connect("account_data.db")
    cursor = conn.cursor()

    hashed = bcrypt.hashpw(
        password.encode(),
        bcrypt.gensalt()
    )

    cursor.execute(
        """
        INSERT INTO users
        (username,password)
        VALUES (?,?)
        """,
        (
            username,
            hashed
        )
    )

    conn.commit()
    conn.close()

def verify_password(username, password):

    con = sqlite3.connect("account_data.db")
    cursor = con.cursor()

    cursor.execute(
        "SELECT password FROM users WHERE username=?",
        (username,)
    )

    row = cursor.fetchone()

    con.close()

    if row is None:
        return False

    stored_password = row[0]

    if isinstance(stored_password, str):
        stored_password = stored_password.encode()

    return bcrypt.checkpw(
        password.encode(),
        stored_password
    )

def user_exists(username):

    con = sqlite3.connect("account_data.db")
    cursor = con.cursor()

    cursor.execute(
        "SELECT username FROM users WHERE username=?",
        (username,)
    )

    row = cursor.fetchone()

    con.close()

    return row is not None

def reset_password(username, new_password):

    conn = sqlite3.connect("encryptor.db")
    cursor = conn.cursor()

    hashed = bcrypt.hashpw(
        new_password.encode(),
        bcrypt.gensalt()
    )

    cursor.execute(
        """
        UPDATE users
        SET password=?
        WHERE username=?
        """,
        (
            hashed,
            username
        )
    )

    conn.commit()
    conn.close()

def save_hash(username, filename, filehash):

    con = sqlite3.connect("account_data.db")
    cursor = con.cursor()

    cursor.execute(
        """
        INSERT INTO file_hashes
        (username, filename, filehash)
        VALUES (?, ?, ?)
        """,
        (username, filename, filehash)
    )

    con.commit()
    con.close()

def get_hash(username, filename):

    con = sqlite3.connect("account_data.db")
    cursor = con.cursor()

    cursor.execute(
        """
        SELECT filehash
        FROM file_hashes
        WHERE username=?
        AND filename=?
        ORDER BY id DESC
        LIMIT 1
        """,
        (username, filename)
    )

    row = cursor.fetchone()

    con.close()

    if row:
        return row[0]

    return None

def get_dashboard_stats(username):

    con = sqlite3.connect("account_data.db")
    cursor = con.cursor()

    # Total Encryptions
    cursor.execute(
        """
        SELECT COUNT(*)
        FROM history
        WHERE username=?
        AND operation='Encrypt'
        """,
        (username,)
    )
    encrypt_count = cursor.fetchone()[0]

    # Total Decryptions
    cursor.execute(
        """
        SELECT COUNT(*)
        FROM history
        WHERE username=?
        AND operation='Decrypt'
        """,
        (username,)
    )
    decrypt_count = cursor.fetchone()[0]

    # Text Files
    cursor.execute(
        """
        SELECT COUNT(*)
        FROM history
        WHERE username=?
        AND filetype='Text'
        """,
        (username,)
    )
    text_count = cursor.fetchone()[0]

    # Images
    cursor.execute(
        """
        SELECT COUNT(*)
        FROM history
        WHERE username=?
        AND filetype='Image'
        """,
        (username,)
    )
    image_count = cursor.fetchone()[0]

    # Videos
    cursor.execute(
        """
        SELECT COUNT(*)
        FROM history
        WHERE username=?
        AND filetype='Video'
        """,
        (username,)
    )
    video_count = cursor.fetchone()[0]

    con.close()

    return {
        "encrypt": encrypt_count,
        "decrypt": decrypt_count,
        "text": text_count,
        "image": image_count,
        "video": video_count
    }

def save_history(username, filename, filetype, operation):

    con = sqlite3.connect("account_data.db")
    cursor = con.cursor()

    cursor.execute("""
        INSERT INTO history
        (username,filename,filetype,operation)
        VALUES(?,?,?,?)
    """, (
        username,
        filename,
        filetype,
        operation
    ))

    con.commit()
    con.close()


def delete_account(username):

    con = sqlite3.connect("account_data.db")
    cursor = con.cursor()

    cursor.execute(
        "DELETE FROM users WHERE username=?",
        (username,)
    )

    cursor.execute(
        "DELETE FROM history WHERE username=?",
        (username,)
    )

    con.commit()
    con.close()

def get_history(username):

    con = sqlite3.connect("account_data.db")
    cursor = con.cursor()

    cursor.execute(
        """
        SELECT filename,
               filetype,
               operation,
               timestamp
        FROM history
        WHERE username=?
        ORDER BY id DESC
        """,
        (username,)
    )

    records = cursor.fetchall()

    con.close()

    return records