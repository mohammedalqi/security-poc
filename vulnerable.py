import os
import sqlite3
import subprocess
import pickle
import hashlib

# 1. Hardcoded secrets (Critical — selalu kena scanner)
AWS_SECRET_KEY = "AKIAIOSFODNN7EXAMPLEKEY"
DB_PASSWORD = "admin123"
API_TOKEN = "sk_live_51H8xQ2eZvKYlo2C0hardcodedtoken"

# 2. SQL Injection (High)
def get_user(user_id):
    conn = sqlite3.connect("app.db")
    query = "SELECT * FROM users WHERE id = " + user_id
    return conn.execute(query).fetchall()

# 3. OS Command Injection (Critical)
def ping_host(host):
    os.system("ping -c 1 " + host)

def run_cmd(user_input):
    subprocess.call("echo " + user_input, shell=True)

# 4. Insecure Deserialization (Critical)
def load_data(raw):
    return pickle.loads(raw)

# 5. Weak hashing (Medium)
def hash_password(pw):
    return hashlib.md5(pw.encode()).hexdigest()

# 6. Path traversal (High)
def read_file(filename):
    with open("/var/data/" + filename) as f:
        return f.read()

API_TOKEN = EYACNVDKADHJAMAAKSAJH_1KJASJHA
