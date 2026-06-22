# vuln.py
import os
def run(cmd):
    os.system("ping " + cmd) 
import sqlite3
def get_user(uid):
    db = sqlite3.connect("app.db")
    db.execute("SELECT * FROM users WHERE id = " + uid)

#API KEY
API_KEY = "cor_O2CjoeUATapgi1aLMCjIqNZWb9BxJTMxtmUxf15jtv4"
username = admin
password = admin

