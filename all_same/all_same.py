def all_same(sequence):
  return all(
    item == sequence[0]
    for item in sequence
  )
