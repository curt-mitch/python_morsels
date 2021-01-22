def total_length(*iterables):
  length_ = 0
  for item in iterables:
    length_ += sum(1 for _ in item)
  return length_
