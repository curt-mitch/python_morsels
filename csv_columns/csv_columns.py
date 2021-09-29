"""
 This exercise includes 3 bonuses and 8 hints (hover over the hint links before clicking on them).

We recommend Novice-level users solve up to the first bonus for this exercise.

I'd like you to write a function called csv_columns that accepts a file object and returns a dictionary mapping CSV headers to column data for each header.

If our CSV file contains this data:

h1,h2
1,2
3,4

Then our function will work like this:

>>> csv_columns(open('my_file.csv'))
{'h1': ['1', '3'], 'h2': ['2', '4']}

Your csv_columns function shouldn't close the file given to it.

Note that the CSV data may have commas inside the cells as well, so a simple split-by-commas won't work.

Bonus 1

For the first bonus, I'd like you to make sure the dictionary returned from csv_columns has keys in the same order as the columns that were in our CSV file. ✔️

Depending on your version of Python this may be easy or it may require digging through the standard library.
"""

import csv
from collections import OrderedDict

def csv_columns(csv_file):
    file_obj = OrderedDict()
    reader = csv.reader(csv_file)
    for row in (zip(*reader)):
        file_obj[row[0]] = list(row[1:])
    return file_obj
