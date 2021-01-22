def pluck(dict, value_path, sep='.'):
  keys = value_path.split(sep)
  current_value = dict[keys[0]]
  if len(keys) == 1:
    return current_value
  for index, key in enumerate(keys[1:], start=1):
    if index == len(keys) - 1:
      return current_value[key]
    else:
      current_value = current_value[key]

