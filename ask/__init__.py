__version__ = '0.0.4'

import sys
from getpass import getpass
import re

# Fix python 2.x
try:
    input = raw_input
except NameError:
    pass


# https://www.siafoo.net/snippet/88
# or http://stackoverflow.com/questions/287871/print-in-terminal-with-colors-using-python
def highlight(string, status):
    if sys.stdout.isatty():
        mods = {
            'green': '32',
            'red': '31',
            'bold': '1',
        }
        attr = []
        if status == 'error':
            attr.append(mods['red'])
            attr.append(mods['bold'])
        return '\x1b[%sm%s\x1b[0m' % (';'.join(attr), string)
    else:
        return string


def print_error():
    error = 'Invalid input, please try again'
    print(highlight(error, 'error'))


def buildText(question, possibilities, default):
    text = ""
    if question:
        text += question + " "

    if possibilities:
        text += "("
        for p in possibilities:
            text += str(p) + ", "
        text = text[:-2]
        text += ") "

    if default or default == '':
        if default == '':
            text += "['']"

        else:
            text += "[" + default + "]"

    if text == "":
        return text

    else:
        return text.rstrip(" ") + "\n"


def checkInt(i):
    try:
        int(i)
    except ValueError:
        return False

    return True


def checkChar(ch):
    if len(ch) == 1 and ch.lower() in 'abcdefghijklmnopqrstuvwxyz':
        return True


def checkString(string):
    for c in string:
        if c.lower() not in 'abcdefghijklmnopqrstuvwxyz':
            return False

    return True


def checkEmail(email):
    if re.match(r".+\@.+\..+", email):
        return True


def checkNone(i):
    return True


def _ask(text, possibilities, default, check_method, masked=False):
    while True:
        if masked:
            i = getpass(buildText(text, possibilities, default))
        else:
            i = input(buildText(text, possibilities, default))

        if i == '':
            if default or default == '':
                return default
            else:
                print_error()
                continue

        elif possibilities:
            if i in possibilities:
                return i
            else:
                print_error()
                continue

        else:
            if check_method(i):
                return i
            else:
                print_error()
                continue


def askInt(text=None, possibilities=None, default=None):
    return _ask(text, possibilities, default, checkInt)


def askChar(text=None, possibilities=None, default=None):
    return _ask(text, possibilities, default, checkChar)


def askString(text=None, possibilities=None, default=None):
    return _ask(text, possibilities, default, checkString)


def askEmail(text=None, possibilities=None, default=None):
    return _ask(text, possibilities, default, checkEmail)


def askPassword(text=None, possibilities=None, default=None):
    return _ask(text, possibilities, default, checkNone, masked=True)


def ask(text=None, possibilities=None, default=None):
    return _ask(text, possibilities, default, checkNone)