import unittest
import subprocess
import echo


class my_tests(unittest.TestCase):


    def setUp(self):
        """let us create one parset to rule them all"""
        self.parser = echo.create_parser()

    def test_help(self):
        """ Running the program without arguments should show usage. """

        process = subprocess.Popen(
            ["python", "./echo.py", "-h"],
            stdout=subprocess.PIPE)
        stdout, _ = process.communicate()
        usage = open("./USAGE", "r").read()

        self.assertEquals(stdout, usage)

    def test_text(self):
        """testing text parsing of the parser"""
        args = ["hello world"]
        namespace = self.parser.parse_args(args)
        self.assertEqual(namespace.text, "hello world")


    """ testing if shorthand optional flags do the right thing"""

    def test_upper_short(self):
        args = ["-u", "hello world"]
        namespace = self.parser.parse_args(args)
        self.assertEqual(namespace.upper, True)
        self.assertEqual(echo.main(args), "HELLO WORLD")

    
    def test_lower_short(self):
        args = ["-l", "HELLO WORLD"]
        namespace = self.parser.parse_args(args)
        self.assertEqual(namespace.lower, True)
        self.assertEqual(echo.main(args), "hello world")


    def test_title_short(self):
        args = ["-t", "hello world"]
        namespace = self.parser.parse_args(args)
        self.assertEqual(namespace.title, True)
        self.assertEqual(echo.main(args), "Hello World")


    """ testing if long (--flag) optional flags do the right thing"""

    def test_upper_long(self):
        args = ["--upper", "hello world"]
        namespace = self.parser.parse_args(args)
        self.assertEqual(namespace.upper, True)
        self.assertEqual(echo.main(args), "HELLO WORLD")


    def test_lower_long(self):
        args = ["--lower", "HELLO WORLD"]
        namespace = self.parser.parse_args(args)
        self.assertEqual(namespace.lower, True)
        self.assertEqual(echo.main(args), "hello world")


    def test_title_long(self):
        args = ["--title", "hello world"]
        namespace = self.parser.parse_args(args)
        self.assertEqual(namespace.title, True)
        self.assertEqual(echo.main(args), "Hello World")



if __name__ == "__main__":
    unittest.main()