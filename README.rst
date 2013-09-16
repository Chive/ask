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

    >>> from ask import ask, askChar, askInt, askString, askPassword, askEmail, askBool, explain
    >>> ask()
    # Creates an empty input query here

    >>> askInt('Your age')
    Your age
    # Input here (Only accepts integers)

    >>> askString("What's your name?")
    What's your name?
    # Input here

    >>> askChar('Do you want to proceed?', ['y','n'])
    Do you want to proceed? (y/n)
    # Input here (Only accepts 'y' and 'n')

    >>> askChar('Do you want to install this?', ['y','n'], 'y')
    Do you want to install this? (y/n) [y]
    # Input here (Only accepts 'y' and 'n', you can hit enter to use the default 'y')
    
    >>> askBool('Do you want to continue?')
    Do you want to continue (y/n)
    # Input here (automatically generates the possibilites 'y' and 'n')
    
    >>> askEmail()
    # Input here (only accepts email-adresses)
    
    >> askPassword()
    # Masked input here
    
    >> explain()
    # Prints explanation:
    Attention: Input prompts follow this template:
    "Question (answer1, answer2, answer3) [default_answer]"
    (You can just hit enter to chose the default answer)
