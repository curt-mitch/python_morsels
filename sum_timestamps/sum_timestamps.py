def sum_timestamps(timestamp_list):
  hours_total = 0
  minutes_total = 0
  seconds_total = 0
  for timestamp in timestamp_list:
    minutes, seconds = map(int, timestamp.split(':'))
    minutes_total += minutes
    seconds_total += seconds
  minutes_total += int(seconds_total / 60)
  seconds_total = seconds_total % 60
  if minutes_total > 59:
    hours_total = int(minutes_total / 60)
    minutes_total = minutes_total % 60
    formatted_hours = f"{hours_total:02d}"
    if hours_total < 10:
      formatted_hours = f"{hours_total:01d}"
    return formatted_hours + ':' + f"{minutes_total:02d}" + ':' + f"{seconds_total:02d}"
  else:
    formatted_minutes = f"{minutes_total:02d}"
    if minutes_total < 10:
      formatted_minutes = f"{minutes_total:01d}"
    return formatted_minutes + ':' + f"{seconds_total:02d}"
