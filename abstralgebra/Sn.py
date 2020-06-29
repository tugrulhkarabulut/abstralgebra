from .Group import Group
from .Element import Element
from .helpers.permutation import permute, permute_n

"""
    Symmetric group element implementation
"""
class Permutation(Element):
    def __eq__(self, value):
        if isinstance(value, Permutation):
            return self.toList() == value.toList()
        return self.toList() == value
    
    def toList(self):
        return list(self.value.values())
    
    """
        String conversions
    """

    def __repr__(self):
        return "Permutation({}, {})".format(self.value, str(self.group))

    def __str__(self):
        return "{}, {}".format(self.value, str(self.group))


"""
    Symmetric group (Sn) implementation
"""


class Sn(Group):
    def __init__(self, n):
        self.n = n
        elements = self.__compute_elements()
        eye = self.__compute_eye()
        super().__init__(elements=elements, eye=eye)
    
    def __compute_elements(self):
        if isinstance(self.n, int):
            return list(map(lambda el:  Permutation(el, self), permute_n(self.n)))
        if isinstance(self.n, list) or isinstance(self.n, str):
            return list(map(lambda el:  Permutation(el, self), permute(self.n)))
        raise ValueError("Parameter 'n' must be an int or a list.")

    def __compute_eye(self):
        if isinstance(self.n, int):
            return list(range(self.n))
        if isinstance(self.n, list):
            return self.n

    # Zn is a group under addition
    def op(self, x, y):
        return { y_i: x[y_i_image] for (y_i, y_i_image) in zip(y.keys(), y.values()) }

    def __repr__(self):
        return "Sn({})".format(self.n)

    def __str__(self):
        return "S_{}".format(self.n)
