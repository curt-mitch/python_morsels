class Point:
  def __init__(self, x, y, z):
    self.x = x
    self.y = y
    self.z = z

  def __eq__(self, other):
    return self.x == other.x and self.y == other.y and self.z == other.z

  def __add__(self, other):
    return Point(self.x + other.x, self.y + other.y, self.z + other.z)

  def __sub__(self, other):
    return Point(self.x - other.x, self.y - other.y, self.z - other.z)

  # performs scalar multiplication
  def __rmul__(self, other):
    return Point(self.x * other, self.y * other, self.z * other)

  def __repr__(self):
    return 'Point(x={}, y={}, z={})'.format(self.x, self.y, self.z)
