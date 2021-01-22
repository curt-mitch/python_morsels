from math import sqrt

def is_perfect_square(num):
  if num < 1:
    return False
  sq_root = sqrt(num)
  return sq_root % 1 == 0
