"""
This week I'd like you to write a callable object called float_range that acts
sort of like the built-in range callable but allows for floating point numbers
to be specified.

I say "callable" instead of "function" or "class" because I don't actually care
how you implement this thing. What I care about is that you can call it and
loop over the resulting items.

It should work like this:

>>> for n in float_range(0.5, 2.5, 0.5):
...     print(n)
...
0.5
1.0
1.5
2.0
>>> list(float_range(3.5, 0, -1))
[3.5, 2.5, 1.5, 0.5]

Your float_range callable should also allow the step and start arguments to be
optional, the same way they are for Python's built-in range callable:

>>> for n in float_range(0.0, 3.0):
...     print(n)
...
0.0
1.0
2.0
>>> for n in float_range(3.0):
...     print(n)
...
0.0
1.0
2.0

I also want you to make sure that calling float_range doesn't create a large
list of numbers. By this I mean that calling float_range should be
memory-efficient. Return an iterator or generator or some kind of lazy object;
not a list.
"""

def float_range(start, stop=None, step=1):
    if stop is None:
        start, stop = 0, start
    i = start
    if step > 0:
        while i < stop:
            yield i
            i += step
    else:
        while i > stop:
            yield i
            i += step