"""
This week I'd like you to implement a function which sorts strings case-insensitively.

This function will be called natural_sort and it'll sort strings similar to how humans sort strings.

For example:

>>> natural_sort(['uncle', 'Yankee', 'India', 'hotel', 'zebra', 'Oscar'])
['hotel', 'India', 'Oscar', 'uncle', 'Yankee', 'zebra']
>>> natural_sort(['Uruguay', 'echo', 'Charlie', 'golf'])
['Charlie', 'echo', 'golf', 'Uruguay']

This function should also accept an optional reverse argument which will reverse the sorting order:

>>> natural_sort(['Uruguay', 'echo', 'Charlie', 'golf'], reverse=True)
['Uruguay', 'golf', 'echo', 'Charlie']

This function doesn't need to handle symbols or sorting of non-ASCII characters specially.

The module you put this sorting function in should be called sortutils.py.
"""

def natural_sort(list, reverse=False):
    return sorted(list, key=str.lower, reverse=reverse)