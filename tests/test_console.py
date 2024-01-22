#!/usr/bin/python3

import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models import storage

class TestConsole(unittest.TestCase):

    def setUp(self):
        self.console = HBNBCommand()

    def tearDown(self):
        self.console = None
        storage.reset()

    def test_create(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create User")
            output = f.getvalue().strip()
            self.assertTrue(len(output) == 36)  # Assuming UUID format

    def test_show(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create User")
            user_id = f.getvalue().strip()
            self.console.onecmd(f"show User {user_id}")
            output = f.getvalue().strip()
            self.assertTrue("User" in output and user_id in output)

    def test_all(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create User")
            self.console.onecmd("create Place")
            self.console.onecmd("create State")
            self.console.onecmd("all")
            output = f.getvalue().strip()
            self.assertTrue("User" in output and "Place" in output and "State" in output)

    def test_count(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create User")
            self.console.onecmd("create User")
            self.console.onecmd("count User")
            output = f.getvalue().strip()
            self.assertTrue(output == "2")

    def test_update(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create User")
            user_id = f.getvalue().strip()
            self.console.onecmd(f"update User {user_id} first_name John")
            self.console.onecmd(f"show User {user_id}")
            output = f.getvalue().strip()
            self.assertTrue("John" in output)

if __name__ == '__main__':
    unittest.main()
