def multimax(num_list):
  num_list = list(num_list)
  max_val = max(num_list, default=[])
  max_list = []
  for num in num_list:
    if num == max_val:
      max_list.append(num)
  return max_list

