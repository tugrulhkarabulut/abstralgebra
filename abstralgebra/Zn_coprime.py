from math import gcd
from .Group import Group

"""
    Zn* is a group under multiplication.
    Its element are the numbers less than and coprime of n
"""


class Zn_coprime(Group):
    def __init__(self, n):
        self.n = n

    @property
    def elements(self):
        elements = []
        for i in range(self.n):
            if gcd(self.n, i) == 1:
                elements.append(i)

        return elements

    def mod(self, k):
        return k % self.n

    # Zn* is a group under multiplication
    def op(self, x, y):
        return x * y

    def generateSubgroupBy(self, k, sorted=False, convertMod=False):
        if convertMod is True:
            k = self.mod(k)

        if k not in self.elements:
            raise ValueError('Zn* does not contain ' + str(k))

        generatedGroup = [k]
        currentElement = self.mod(k * k)

        # Repeat until the cycle finishes, that is, when we return to the generator element k
        while (self.mod(currentElement) != k):
            generatedGroup.append(currentElement)
            currentElement = (currentElement * k) % self.n

        if sorted is True:
            generatedGroup.sort()
        return generatedGroup
