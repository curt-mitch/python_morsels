def minmax(iterable, *, key=lambda x: x):
  iter_list = list(iterable)
  if len(iter_list) == 0:
    raise ValueError('iterable is empty!')
  return (min(iter_list, key=key), max(iter_list, key=key))
