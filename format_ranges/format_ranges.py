def format_ranges(ranges):
  output = ''
  ranges = list(ranges) # ensure ranges is list
  range_start = ranges[0]
  range_end = ranges[0]
  for i in range(1, len(ranges)):
    if ranges[i] == ranges[i-1] + 1:
      range_end = ranges[i]
    else:
      range_str = "{}-{}".format(range_start, range_end)
      if len(output) == 0:
        output = range_str
      else:
        output += ",{}".format(range_str)
      range_start = ranges[i]
      range_end = ranges[i]
  if len(output) != 0:
    output += ",{}".format("{}-{}".format(range_start, range_end))
  elif range_start != range_end:
    output = "{}-{}".format(range_start, range_end)
  return output
