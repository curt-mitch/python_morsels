def tail(sequence, n):
  new_seq = list(sequence)
  length = len(new_seq)
  tail_count = 0 if n > length else length - n
  return new_seq[tail_count:]
