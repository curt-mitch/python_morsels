from collections import UserDict, defaultdict
from typing import Callable, Iterable

def default_key(arg):
    return arg

class Grouper(UserDict):
    def __init__(self, iterable: Iterable={}, key: Callable=default_key) -> None:
        self.iterable = iterable
        self.key = key

        if type(iterable) == dict:
            self.data = iterable

        else:
            self.data = defaultdict(list)
            for item in iterable:
                map_key = key(item)
                self.data[map_key].append(item)
