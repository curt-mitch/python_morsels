def section_helper(length, n):
  """Return start and end for the n sections of an iterable of given length."""
  count, remainder = divmod(length, n)
  for i in range(n):
    start = min(i, remainder) + i*count
    end = min(i+1, remainder) + (i+1)*count
    yield start, end

def divide(sequence, n):
  """Return a sequence by dividing sequence into n parts."""
  return [
    sequence[start:end]
    for start, end in section_helper(len(sequence), n)
  ]
