class EasyDict(object):
  def __init__(self, _dict=None):
    if _dict is not None:
      self.__dict__.update(_dict)
      for key, value in _dict.items():
        self[str(key)] = value
  def __setattr__(self, key, value):
    self[key] = value
  def __getattr__(self, key):
    return self[key]
