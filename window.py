import tkinter as tk
from tkinter import ttk
import os

def run(runfile):
  with open(runfile,"r") as rnf:
    exec(rnf.read())


def login_attempt():
     if username_entry.get() == "mustafa" and password_entry.get() == "12345":
        print("Succesful login")
        run("contracts.py")
     else:
         print("Unsuccesful login")

    
root = tk.Tk()
root.title("User Entry")

style = ttk.Style(root)
root.tk.call("source", "forest-light.tcl")
root.tk.call("source", "forest-dark.tcl")
style.theme_use("forest-dark")

frame = ttk.Frame(root)
frame.pack()

 # Saving User Info
user_info_frame = ttk.LabelFrame(frame, text="User Login" )
user_info_frame.grid(row = 0, column = 0)

username_text = ttk.Label(user_info_frame, text="Username")
username_text.grid(row=0,column=0)
username_entry = ttk.Entry(user_info_frame)
username_entry.insert(0, "Username")
username_entry.grid(row=0, column=1)

password_text = ttk.Label(user_info_frame, text="Password")
password_text.grid(row=1,column=0)
password_entry = ttk.Entry(user_info_frame)
password_entry.insert(0, "Password")
password_entry.grid(row=1, column=1)

button = ttk.Button(frame, text = "Log In", command = login_attempt)
button.grid(row=1, column = 0)

root.mainloop()