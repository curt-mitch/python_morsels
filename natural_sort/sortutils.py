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

Bonus 1

For the first bonus, you can try adding three more features to your natural_sort function:

    The sorting should be "stable", just like Python's built-in sorting algorithm
    Your function should accept a key argument which will allow a custom key function to be used
    The default key function should live in the same module and should be called natural_key

Here's an example of stable sorting (note the unchanged order of all three "McDonald" variants):

>>> natural_sort(['McDonald', 'MCDONALD', 'Mcdonald', 'MacDonald'])
['MacDonald', 'McDonald', 'MCDONALD', 'Mcdonald']

Here's an example of using the natural_key function and key argument to natural_sort:

>>> from sortutils import natural_key, natural_sort
>>> def reverse_name(name):
...     # Key function to sort by last name first.
...     first, last = name.rsplit(' ', 1)
...     return natural_key(last + ' ' + first)
...
>>> names = ['Sarah Clarke', 'Sara Hillard', 'Sarah Chiu']
>>> natural_sort(names, key=reverse_name)
['Sarah Chiu', 'Sarah Clarke', 'Sara Hillard']
>>> natural_sort(names)
['Sara Hillard', 'Sarah Chiu', 'Sarah Clarke']

Depending on how you implemented your original natural_sort function, this key argument and maintaining a stable sort might be something your function already supports.

The requirements for this bonus might sound challenging, but there's a built-in function that can help with all of the requirements for this bonus.

"""
natural_key = str.lower

def natural_sort(list, reverse=False, key=natural_key):
    return sorted(list, key=key, reverse=reverse)