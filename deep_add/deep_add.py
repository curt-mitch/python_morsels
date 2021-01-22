"""
This week I'd like you to write a function that takes a nested list of numbers
and adds up all the numbers.

The phrase "nested list of numbers" might not be obvious. Here are examples of
what I mean:

>>> deep_add([1, 2, 3, 4])
10
>>> deep_add([[1, 2, 3], [4, 5, 6]])
21
>>> deep_add([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
36

So your deep_add function should accept lists of numbers, lists of lists of
numbers, lists of lists of lists of numbers, and so on. It should even work
when there are multiple hierarchies involved or when there are empty lists:

>>> deep_add([1, [2, [3, 4], [], [[5, 6], [7, 8]]]])
36
>>> deep_add([[], []])
0

Bonus 1

For the first bonus this week, I'd like you to make sure your function works with any iterable, not just lists. It should work with tuples, sets, and even generators ✔️:

>>> deep_add([(1, 2), [3, {4, 5}]])
15

Bonus 2

For the second bonus I'd like you to allow your function to accept an optional start value (which defaults to 0) ✔️:

>>> deep_add([[1, 2], [3, 4]], start=2)
12

Bonus 3

For the third bonus, make sure your function works with anything number-like (anything you can use + on except for iterables), not just numbers themselves ✔️:

>>> from datetime import timedelta
>>> deep_add([[timedelta(5), timedelta(10)], [timedelta(3)]], start=timedelta(0))
18

"""

# First solution, solved bonuses 1 and 2
"""
import numbers;

def deep_add(num_list, total=0, start=0):
  for item in num_list:
    if isinstance(item, numbers.Number):
      total += item
    else:
      total += deep_add(item)
  return total + start
"""

