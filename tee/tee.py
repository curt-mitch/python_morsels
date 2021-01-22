"""
I'd like you to write a tee.py program which works like the Linux/Unix tee utility.

This program pipes standard input into standard output and also writes this output an optional file.

Given a Python program, hello.py, like this:

print("Hello world!")

Your tee.py program should work like this:

$ python hello.py | python tee.py output.txt
Hello world!

After running tee.py, the output.txt file should contain the captured output:

Hello world!

The tee.py program should also work when no filename is given.

$ python hello.py | python tee.py
Hello world!

"""

import sys

if len(sys.argv) > 1:
  f = open(sys.argv[1], mode='wt')
else:
  f = None

for line in sys.stdin:
  sys.stdout.write(line)
  if f:
    f.write(line)
