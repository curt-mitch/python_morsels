from itertools import chain

def interleave(list1, list2):
  return chain.from_iterable(pair for pair in zip(list1, list2))
