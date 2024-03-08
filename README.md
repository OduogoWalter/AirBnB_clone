AirBnB_clone

Description:
This is the first step towards building the AirBnB clone web application. The project involves creating a command interpreter to manage AirBnB objects, such as User, State, City, Place, etc.

Command Interpreter:
The command interpreter allows users to perform various operations on objects, including creating new objects, retrieving objects from files or databases, performing operations on objects, updating object attributes, and destroying objects.

How to Start:
To start the console, run the following command in your terminal:
$ ./console.py

Interactive Mode:
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 

Non-Interactive Mode:
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 

How to Use:
- Use the documented commands to interact with the console.
- Follow the examples provided in the documentation.

Examples:
$ ./console.py
(hbnb) help
(hbnb) create User
(hbnb) show User 1234-5678
(hbnb) update User 1234-5678 first_name "John"
(hbnb) all User
(hbnb) quit

Resources:
1. https://docs.python.org/3.8/library/cmd.html
2. https://pymotw.com/2/cmd/
3. https://docs.python.org/3.8/library/uuid.html
4. https://docs.python.org/3.8/library/datetime.html
5. https://docs.python.org/3.8/library/unittest.html#module-unittest
6. https://yasoob.me/2013/08/04/args-and-kwargs-in-python-explained/
7. https://www.pythonsheets.com/notes/python-tests.html
8. https://wiki.python.org/moin/CmdModule
9. https://realpython.com/python-testing/

i. https://intranet.alxswe.com/concepts/66
ii. https://intranet.alxswe.com/concepts/74
