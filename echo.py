import argparse
import sys


def uppercase(string):
    return string.upper()


def lowercase(string):
    return string.lower()


def titlecase(string):
    return string.title()


def msg(name=None):
    return '''usage: echo.py [-h] [-u] [-l] [-t] text\n
Perform transformation on input text.\n\npositional arguments:
  text         text to be manipulated\n\noptional arguments:
  -h, --help   show this help message and exit
  -u, --upper  convert text to uppercase
  -l, --lower  convert text to lowercase
  -t, --title  convert text to titlecase'''


def main():
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("--upper", "-u")
    parser.add_argument("--lower", "-l")
    parser.add_argument("--title", "-t",)
    parser.add_argument("-help", "--h", action="store_true")
    args = parser.parse_args()
    if args.upper:
        print uppercase(sys.argv[2])
    if args.lower:
        print lowercase(sys.argv[2])
    if args.title:
        print titlecase(sys.argv[2])
    if args.h:
        print msg()


if __name__ == "__main__":
    main()
