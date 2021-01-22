"""
This week I'd like you to write a function called flatten_dict, which will
accept a dictionary-of-dictionaries and "flatten" this structure by joining
the keys in the outer dictionary with the keys in the inner dictionaries with
an _ separator.

>>> flatten_dict({'vowels': {'a': 1, 'e': 4}, 'consonants': {'z': 2, 'v': 3}})
{'vowels_a': 1, 'vowels_e': 4, 'consonants_z': 2, 'consonants_v': 3}

Your flatten_dict function should also accept a sep keyword-only argument (look
at the hints if you get stuck on that) to customize the separator:

>>> flatten_dict({'A': {1: [], 2: ['z']}, 'B': {}}, sep=' / ')
{'A / 1': [], 'A / 2': ['z']}

At first, assume the object passed to your function is a single dictionary
whose values are all also dictionaries. You also only need to flatten one level
deep at first.

Bonus 1

For the first bonus, allow the dictionary passed to flatten_dict to have values
which aren't dictionaries.

>>> flatten_dict({'vowels': {'a': 1, 'e': 2}, 'b': 4})
{'vowels_a': 1, 'vowels_e': 2, 'b': 4}
"""


def flatten_dict(nested_dict, *, sep="_"):
    result_dict = {}
    for outer_key in nested_dict.keys():
        if isinstance(nested_dict[outer_key], dict):
            for inner_key in nested_dict[outer_key]:
                result_dict[str(outer_key) + sep + str(inner_key)] =\
                    nested_dict[outer_key][inner_key]
        else:
            result_dict[str(outer_key)] = nested_dict[outer_key]
    return result_dict
