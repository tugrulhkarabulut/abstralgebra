from math import gcd
from .Group import Group
from .Element import Element

"""
    Z/n is a group under addition.
    It is a cyclic group.
    Its elements are 0, 1, ..., n-1
"""


class Zn(Group):
    def __init__(self, n):
        self.n = n
        super().__init__(elements=list(range(self.n)), eye=0)

    def mod(self, k):
        return k % self.n

    # Zn is a group under addition
    def op(self, x, y):
        return self.mod(x + y)

    def exists(self, k):
        value = k.value if isinstance(k, Element) else k
        return value in self.values
        

    # If n and k are coprime, then the element k generates Zn
    def isGeneratedBy(self, k, convertMod=False):
        if convertMod is True:
            k = self.mod(k)

        if self.exists(k):
            return gcd(self.n, k) == 1

        raise ValueError('Zn does not contain ' + str(k) +
                         '\n Use convertMod=True to allow the function to take the modulo n of the given number')

    def generateSubgroupBy(self, k, sorted=False, convertMod=False):
        if convertMod is True:
            k = self.mod(k)

        if k not in self.elements:
            raise ValueError('Zn does not contain ' + str(k) +
                             '\n Use convertMod=True to allow the function to take the modulo n of the given number')

        generatedGroup = [k]
        currentElement = self.mod(2*k)

        # Repeat until the cycle finishes, that is, when we return to the generator element k
        while (self.mod(currentElement) != k):
            generatedGroup.append(currentElement)
            currentElement = (currentElement + k) % self.n

        if sorted is True:
            generatedGroup.sort()
        return generatedGroup

    def __repr__(self):
        return "Zn({})".format(self.n)

    def __str__(self):
        return "Z/{}".format(self.n)
