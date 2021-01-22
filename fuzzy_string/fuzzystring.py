class FuzzyString(object):
  def __init__(self, string):
    self.string = string

  def __str__(self):
    return self.string

  def __repr__(self):
    return f"'{self.string}'"

  def __eq__(self, other):
    if not (isinstance(other, FuzzyString) or isinstance(other, str)):
      return NotImplemented

    if isinstance(other, FuzzyString):
      return self.string.lower() == other.string.lower()
    else:
      return str(self.string.lower()) == other.lower()
