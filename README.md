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

import sys

class Console:
    """
    Console class for the AirBnB clone command-line interface.
    """
    prompt = "(hbnb) "

    def do_help(self, arg):
        """
        Display help messages for available commands.
        """
        commands = ["EOF", "help", "quit"]
        print("\nDocumented commands (type help <topic>):")
        print("=" * 40)
        for cmd in commands:
            print(cmd.ljust(10), end=" ")
        print("\n")

    def do_EOF(self, arg):
        """
        Handle the EOF command.
        """
        print()
        sys.exit()

    def do_quit(self, arg):
        """
        Exit the console.
        """
        sys.exit()

if __name__ == "__main__":
    my_console = Console()
    my_console.cmdloop()
