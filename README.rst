ask
===

Easy input validation for python

Installation
------------
::

    pip install ask

Usage
-----
::

    >>> from ask import ask, askChar, askInt, askString
    >>> ask()
    # Creates an empty input query here

    >>> askInt('Your age')
    Your age
    # Input here (Only accepts integers)

    >>> askString("What's your name?")
    What's your name?
    # Input here

    >>> askChar('Do you want to proceed?', ['y','n'])
    Do you want to proceed? (y, n)
    # Input here (Only accepts 'y' and 'n')

    >>> askChar('Do you want to install this?', ['y','n'], 'y')
    Do you want to install this? (y, n) [y]
    # Input here (Only accepts 'y' and 'n', you can hit enter to use the default 'y')