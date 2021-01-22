"""
This week I'd like you to write a function that returns "windows" of items
from a given list. Your function should take a list and a number n and return a
new list of tuples, each containing "windows" of n consecutive items. That is,
each tuple should contain the current item and the n-1 items after it.

Here are some examples:

>>> numbers = [1, 2, 3, 4, 5, 6]
>>> window(numbers, 2)
[(1, 2), (2, 3), (3, 4), (4, 5), (5, 6)]
>>> window(numbers, 3)
[(1, 2, 3), (2, 3, 4), (3, 4, 5), (4, 5, 6)]
>>> window(numbers, 4)
[(1, 2, 3, 4), (2, 3, 4, 5), (3, 4, 5, 6)]

Your window function should return an empty list if the given n is 0. It should
also be able to accept strings, tuples, and other sequences.

# Bonus 1
As a bonus, make sure your function accepts any iterables, not just sequences. ✔️

For example your function should accept iterators and other lazy iterables:

>>> numbers = [1, 2, 3, 4, 5, 6]
>>> squares = (n**2 for n in numbers)
>>> window(squares, 3)
[(1, 4, 9), (4, 9, 16), (9, 16, 25), (16, 25, 36)]

# Bonus 2
For a second bonus, make sure your function returns an iterator instead of a list. ✔️

>>> numbers = [1, 2, 3, 4, 5, 6]
>>> next(window(numbers, 3))
(1, 2, 3)

"""

def window(numbers, n):
  numbers = list(numbers)
  result = []
  start = 0
  end = len(numbers) - n
  while start <= end:
      result.append(tuple(numbers[start:(start + n)]))
      start += 1
  return result
