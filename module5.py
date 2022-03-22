import sqlite3
from clients import Clients

conn = sqlite3.connect('clients.db')
c = conn.cursor()

def main():
    c.execute("""CREATE TABLE clients (
        fname text PRIMARY KEY,
        fname text PRIMARY KEY, 
        length integer, 
        lash_type text, 
        last_appt text, 
        last_payment real)""")
    conn.commit()

def create_client(f, l):
    client = Clients(f, l)
    c.execute("INSERT INTO clients VALUES (:fname, :lname)", {'fname':client.fname, 'lname':client.lname})

def delete_client():
    pass

def view_client_info(f, l):
        c.execute("SELECT * WHERE (fname=:fname AND lname = lname)", {'fname': f, 'lname': l})

conn.close()


def view_menu():
    value = 0
    while value != 4:
        print("\n\nMENU-\n1- Create a new client\n2- View client information\n3- Update client information\n 4- Quit")
        value = int(input("Choose a menu item (1-4): "))