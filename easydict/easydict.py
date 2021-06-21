class EasyDict(object):
    def __init__(self, _dict=None):
        if _dict is not None:
            self.__dict__.update(_dict)

    def __setitem__(self, key, value):
        self.__dict__[key] = value

    def __getitem__(self, key):
        return self.__dict__[key]
