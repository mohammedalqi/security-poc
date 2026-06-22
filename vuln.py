# vuln.py
import os
def run(cmd):
    os.system("ping " + cmd) 
import sqlite3
def get_user(uid):
    db = sqlite3.connect("app.db")
    db.execute("SELECT * FROM users WHERE id = " + uid)
