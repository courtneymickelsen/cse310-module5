import sqlite3
from clients import Clients

conn = sqlite3.connect('clients.db')
c = conn.cursor()

def create_table():
    c.execute("""CREATE TABLE clients (
        fname text,
        lname text, 
        length integer, 
        lash_type text, 
        last_appt text, 
        last_payment real)""")
    conn.commit()

def create_client(f, l):
    client = Clients(f, l)
    insert_more = input("Would you like to enter lash information for this client right now? ")
    if insert_more.lower() == 'yes' or insert_more.lower() == 'y':
        client.length = int(input("What length of lashes does this client use? "))
        client.type = input("Does this client have classic or volume lashes? ").capitalize()

    c.execute("""INSERT INTO clients VALUES (
        :fname, 
        :lname,
        :length,
        :type,
        :last_appt,
        :last_payment
        )""", 
        {'fname': client.fname,
        'lname': client.lname,
        'length':client.length,
        'type': client.type,
        'last_appt':client.last_appt,
        'last_payment': client.last_payment
        })
    conn.commit()

def update_client_information(f, l):
    col_name = input("What value do you want to change? (length, type, last_appt, last_payment)").lower()
    value = input("What would you like the new value to be? ")
    if col_name in ['length', 'type', 'last_appt', 'last_payment']:
        c.execute("UPDATE clients SET {col_name} = '{value}' WHERE (fname = {f} AND lname = {l})")
    else:
        print("Invalid input, please try again.")
        update_client_information(f, l)
    conn.commit()

def view_client_info(f, l):
        c.execute("SELECT * FROM clients WHERE (fname =:fname AND lname =:lname)", {'fname': f, 'lname': l})
        rows = c.fetchall()
        for row in rows:
            print(f"Name: {row[0]} {row[1]}\nLash Length: {row[2]}\nLash Type: {row[3]}\nDate of Last Appointment: {row[4]}\nLast Payment Amount: {row[5]}")

def add_appointment(f, l):
    pass

def view_all_clients():
    c.execute("SELECT fname, lname FROM clients")
    rows = c.fetchall()
    print("\nClients:")
    for row in rows:
        print(f"{row[0]} {row[1]}")

def view_menu():
    value = 0
    while value != 6:
        print("\n\nMENU-\n1- Create a new client\n2- View client information\n3- Update client information\n4- Add a new appointment\n5- Quit")
        value = int(input("Choose a menu item (1-6): "))
        if value in [1, 2, 3, 4]:
            f = input("What is the client's first name? ").capitalize()
            l = input("What is the client's last name? ").capitalize()
        if value == 1:
            create_client(f, l)
        elif value == 2:
            view_client_info(f, l)
        elif value == 3:
            update_client_information(f, l)
        elif value == 4:
            add_appointment(f, l)
        elif value == 5:
            view_all_clients()
        elif value == 6:
            print("\nThank you! Your data has been saved.\n\n")
            pass
        else:
            print("Invalid input, please try again.")
            view_menu()

def main():
    
    # create_table() # please comment out this line of code after running the first time
    view_menu()
    conn.close()

if __name__ == "__main__":
    main()