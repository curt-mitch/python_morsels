class EasyDict(object):
    def __init__(self, init=None, **attributes):
        if init is not None:
            self.__dict__.update(init)
        if len(attributes) > 0:
            for key, value in attributes.items():
                self.__setitem__(key, value)

    def __setitem__(self, key, value):
        self.__dict__[key] = value

    def __getitem__(self, key):
        return self.__dict__[key]

    def __eq__(self, other):
        for key in self.__dict__.keys():
            if self.__dict__[key] != other[key]:
                return False
        return True

    def get(self, key, default=None):
        if key in self.__dict__.keys():
            return self.__dict__[key]
        elif default is not None:
            return default
