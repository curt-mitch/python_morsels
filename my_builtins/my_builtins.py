"""
This week I'd like you to re-implement many of Python's built-in functions. This might sound boring and pointless, but you may be surprised at what you learn in this exercise.

Many of the built-in functions are very simple, some are not so simple, and many of them reveal interesting and important facts about the way Python works.

Initially, I'd like you to re-implement len, all, and sum.

Note that your custom versions of len and sum will need to raise TypeError exceptions (with specific error messages) in certain cases, just as the Python built-in versions do:

>>> len(4)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: object of type 'int' has no len()
>>> sum(['a', 'b'], '')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: sum() can't sum strings [use ''.join(seq) instead]

"""
from collections.abc import Collection, Iterator

def len(obj):
    try:
        return obj.__len__()
    except AttributeError:
        class_name = type(obj).__name__
        raise TypeError(f"object of type '{class_name}' has no len()")
    return obj.__len__()


def all(iter):
    for item in iter:
        if not bool(item):
            return False
    return True


def sum(iter, start=0):
    if isinstance(start, str):
        raise TypeError("sum() can't sum strings [use ''.join(seq) instead]")
    total = start
    for item in iter:
        total += item
    return total