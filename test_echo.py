import unittest
import subprocess
import sys
from echo import *


class my_tests(unittest.TestCase):



    def test_help(self):
        """ Running the program without arguments should show usage. """

        process = subprocess.Popen(
            ["python", "./echo.py", "-h"],
            stdout=subprocess.PIPE)
        stdout, _ = process.communicate()
        usage = open("./USAGE", "r").read()

        self.assertEquals(stdout, usage)

    def test_upper(self):
        self.assertEquals(uppercase("hello world"), "HELLO WORLD")

    def test_lower(self):
        self.assertEquals(lowercase("HELLO WORLD"), "hello world")

    def test_title(self):
        self.assertEqual(titlecase("hello world"), "Hello World")

    if __name__ == "__main__":
        unittest.main()