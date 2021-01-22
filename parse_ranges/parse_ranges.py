def parse_ranges(ranges):
  # clean up range string
  range_str = ranges.strip(' ').split(',')
  for rng in range_str:
    values = rng.split('-')
    start = int(values[0])
    end = int(values[1]) + 1
    for i in range(start, end):
      yield i
  # return result
