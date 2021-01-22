from itertools import zip_longest

def interleave(*list_of_iters):
  sentinel = object() # create unique fillvalue to track uneven iterators
  for iter_ in zip_longest(*list_of_iters, fillvalue=sentinel):
    for val in iter_:
      if val is not sentinel:
        yield val
      else:
        pass
