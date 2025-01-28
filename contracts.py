import tkinter as tk
from tkinter import ttk
import os
import psycopg2

def query():
	# Configure and connect to Postgres
	conn = psycopg2.connect(host="blue-ric-olie.eks1.us-west-2.aws.cratedb.net", 
						 database='doc',
						 port=5432, 
						 user="admin", 
						 password="y-Z*BqBw!*!(Vs,Q-J4_jbHQ", 
						 sslmode="require"
		)
	c = conn.cursor()
	conn.commit()
	conn.close()
	
def submit():
	# Configure and connect to Postgres
	conn = psycopg2.connect(host="blue-ric-olie.eks1.us-west-2.aws.cratedb.net",
						 database='doc', 
						 port=5432, 
						 user="admin", 
						 password="y-Z*BqBw!*!(Vs,Q-J4_jbHQ", 
						 sslmode="require"
		)
	# Create a cursor
	c = conn.cursor()
	# Insert data into table
	thing1 = contractid_entry.get()
	thing2 = companyname_entry.get()
	thing3 = contractname_entry.get()
	thing4 = contracttotal_entry.get()
	c.execute('''INSERT INTO Contracts (contractid, companyname, contractname, contracttotal)
		VALUES (%s,%s,%s,%s)''', (thing1, thing2, thing3, thing4)
		)
	conn.commit()	
	conn.close()
		
	update()

def update():
	# Configure and connect to Postgres
	conn = psycopg2.connect(host="blue-ric-olie.eks1.us-west-2.aws.cratedb.net", 
						 database='doc',
						 port=5432, 
						 user="admin", 
						 password="y-Z*BqBw!*!(Vs,Q-J4_jbHQ", 
						 sslmode="require")

	# Create a cursor
	c = conn.cursor()

	# Grab stuff from online database
	c.execute("SELECT * FROM Contracts")
	records = c.fetchall()

	output = ''

	# Loop thru the results
	for record in records:
		output_label.config(text=f'{output}\n{record[0]} {record[1]}')
		output = output_label['text']

	conn.close()
	

root = tk.Tk()
root.title("Contracts")

style = ttk.Style(root)
root.tk.call("source", "forest-light.tcl")
root.tk.call("source", "forest-dark.tcl")
style.theme_use("forest-dark")

frame = ttk.Frame(root)
frame.pack()


# Create The GUI For The App

contractid_label = ttk.Label(frame, text="Contract ID:")
contractid_label.grid(row=0, column=0, pady=10, padx=10)

contractid_entry = ttk.Entry(frame, font=("Helvetica, 18"))
contractid_entry.grid(row=1, column=0, pady=10, padx=10)

companyname_label = ttk.Label(frame, text="Company Name:")
companyname_label.grid(row=0, column=1, pady=10, padx=10)

companyname_entry = ttk.Entry(frame, font=("Helvetica, 18"))
companyname_entry.grid(row=1, column=1, pady=10, padx=10)

contractname_label = ttk.Label(frame, text="Contract Name:")
contractname_label.grid(row=0, column=2, pady=10, padx=10)

contractname_entry = ttk.Entry(frame, font=("Helvetica, 18"))
contractname_entry.grid(row=1, column=2, pady=10, padx=10)

contracttotal_label = ttk.Label(frame, text="Contract Total:")
contracttotal_label.grid(row=0, column=3, pady=10, padx=10)

contracttotal_entry = ttk.Entry(frame, font=("Helvetica, 18"))
contracttotal_entry.grid(row=1, column=3, pady=10, padx=10)


submit_button = ttk.Button(frame, text="Submit", command=submit)
submit_button.grid(row=2, column=0, pady=10, padx=10)

update_button = ttk.Button(frame, text="Update", command=update)
update_button.grid(row=2, column=1, pady=10, padx=10)

output_label = ttk.Label(root, text="")
output_label.pack(pady=50)



query()

root.mainloop()