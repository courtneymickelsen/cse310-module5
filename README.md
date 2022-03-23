# Overview

Two of my favorite topics to learn within the programming world have been SQL and Python, so I wanted to learn about how they can be integrated. I wrote a program to process and store the information for each of my lash extension clients.

This python program uses SQLite to inegrate with a relational database in oder to store, update, delete and view the data for each client through the command line.

[Software Demo Video](https://youtu.be/F9sDq59zerc)

# Relational Database

I'm using an SQLite relational database, created through Python. It store information for lash extension clients for my small business.

There is only one table in the database currently and it's called 'clients'. This stores names, lash types, lash lengths, most recent appointment dates, and most recent payment amounts for each client.

# Development Environment

I created this program using Visual Studio Code, and it runs in the command-line/terminal.

I used Python to create this program, and the sqlite3 library to integrate SQLite.

# Useful Websites

{Make a list of websites that you found helpful in this project}
* [SQLite Tutorial](https://www.sqlitetutorial.net/what-is-sqlite/)
* [Tutorials Point](https://www.tutorialspoint.com/sqlite/sqlite_python.htm)
* [Stack Overflow](https://stackoverflow.com/questions/1601151/how-do-i-check-in-sqlite-whether-a-table-exists)
* [Learn SQL](https://learnsql.com/cookbook/how-to-get-the-current-date-in-sqlite/)
* [Like Geeks](https://likegeeks.com/python-sqlite3-tutorial/)

# Future Work

* I would like to make it more dynamic, allowing the user to focus on just one client for an extended period of time instead of having to enter in a name every time it calls a new function from the menu
* I would also like to add more tables- things like inventory for my business, bills, etc.