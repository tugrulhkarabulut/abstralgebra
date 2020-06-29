from .Group import Group

class Klein4(Group):
    def __init__(self, elements=[0, 1, 2, 3], eye=0):
        self.__eye = eye
        self.__elements = elements

    @property
    def elements(self):
        return self.__elements

    @property
    def eye(self):
        return self.__eye

    def op(self, x, y):
        if x not in self.__elements or y not in self.__elements:
            raise ValueError('Given values must be in the group elements')

        if x == y:
            return self.eye
        
        if x == self.eye:
            return y

        if y == self.eye:
            return x

        others = filter(lambda a: a != x and a != y, self.elements)
        return list(others)[0]

    def __repr__(self):
        return "Klein4({})".format(self.elements)

    def __str__(self):
        return "Klein({})".format(self.elements)