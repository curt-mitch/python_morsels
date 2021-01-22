from dataclasses import dataclass

@dataclass(order=True)
class Month:
  year: int
  month: int

  # printed when variable is argument of 'print' method
  def __repr__(self):
    return 'Month({}, {})'.format(self.year, self.month)

  # value returned for variable in REPL
  def __str__(self):
    return '{}-{:02d}'.format(self.year, self.month)
