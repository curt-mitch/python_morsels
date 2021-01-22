def chunked(iterable, n=1):
  arr = list(iterable)
  length = len(arr)
  for x in range(0, length, n):
    start = x
    stop = x + n
    yield arr[start:stop]
