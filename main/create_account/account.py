import sqlite3
import os
import hashlib

# check if the database exists or not -> creates if not found in dir
def check_valid_db():
    if os.path.exists("LocalAccount.db"):
        print("Database found")

    else:
        # Local storage for user account + data
        conn = sqlite3.connect("instance/LocalAccount.db")
        cursor = conn.cursor()

        # User_Account table
        cursor.execute("""CREATE TABLE IF NOT EXISTS User_Account
        (user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        password BLOB NOT NULL,
        salt BLOB NOT NULL)
        """)

        # Sorted_Data table
        cursor.execute("""CREATE TABLE IF NOT EXISTS Sorted_Data
        (title_id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        title TEXT UNIQUE NOT NULL,
        file_path TEXT NOT NULL,
        description TEXT,
        FOREIGN KEY (user_id)
            REFFERENCES User_Account(user_id))
        """)
    
        conn.commit()
        conn.close()

# check for an account, if found dont continue
def check_for_user():
    conn = sqlite3.connect("instance/LocalAccount.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM User_Account")

    exists = cursor.fetchone()

    if exists:
        print("welcome back")
    else:
        #create an account
        username = input("set username: ")
        password = input("set password: ").encode()
        create_account(username, password)

    conn.commit()
    conn.close()

# passes in username and password to generate a hash for password
def create_account(username, password):
    generate_pass_hash(username, password)

# generate hash via sha256
def generate_pass_hash(username, password):
    salt = os.urandom(32)
    secure_pass = hashlib.pbkdf2_hmac('sha256', password, salt, 100000)

    #call the adding account function
    add_local_account(username, secure_pass, salt)

# add the user account into the database
def add_local_account(username, secure_pass, salt):
    conn = sqlite3.connect("instance/LocalAccount.db")
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO User_Account (username, password, salt)
        VALUES (?, ?, ?)""", (username, secure_pass, salt))

    conn.commit()
    conn.close()