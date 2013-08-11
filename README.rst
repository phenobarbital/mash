MaSH: Mandarina Shell
=====================

http://github.com/phenobarbital/mash

**MaSH** (Mandarina Shell) is a python module that provides basic interactive-shell and command-oriented classes using cmd and argparse. 
You can use for developing commandline applications.

What does it do?
----------------

**MaSH** is a generic, shell command-line oriented interface for developing console applications, is provided
with basic functionalities:

- Basic Interactive Shell
- xterm color string (for pretty print)
- inheritable shell class with useful functions (textinput, warn, info, question, etc)

Current Features:
-----------------

- Basic interactive shell-console based on `cmd` module
- Simple to use

Basic Example
-------------

- Shell Class:
Mash is easy to use

```python

from mash import Shell
import os

class command(Shell):

    def do_shell(self, s):
        """ Execute shell commands"""
        os.system(s)

if __name__ == '__main__':
    c = command()
    a.start() # starts a console

```

an interactive console appears:

- executing a shell command ("date")
```
# > shell date\n
dom ago 11 03:01:37 VET 2013
```

- "!" is a shortcut to shell commands:

```
# > ! date\n
dom ago 11 03:01:39 VET 2013
```

- auto-complete commands ("q" = "quit")
```
# > q
Goodbye! ...
```

Documentation
-------------

Coming soon.

License
-------

LGPLv3