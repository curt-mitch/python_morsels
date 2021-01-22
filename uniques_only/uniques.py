def uniques_only(iterable):
  uniques = []
  for num in iterable:
    if num not in uniques:
      uniques.append(num)
      yield num
