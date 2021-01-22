import math

def percent_to_grade(percent, suffix=False):
  grade_map = {
    '100': 'A',
    '90': 'A',
    '80': 'B',
    '70': 'C',
    '60': 'D',
    '50': 'F',
    '40': 'F',
    '30': 'F',
    '20': 'F',
    '10': 'F',
    '0': 'F',
  }
  return grade_map[str(math.floor(percent / 10.0) * 10)]
