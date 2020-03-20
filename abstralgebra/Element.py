class Element:
    """
        A class representing a group element.
        It is defined by a value and a group
    """

    def __init__(self, value, group):
        self.value = value
        self.group = group

    """
        Arithmetic Operations
    """

    def __mul__(self, other):
        if isinstance(other, Element):
            other = other.value
        return Element(self.group.op(self.value, other), self.group)
    
    def __imul__(self, other):
        if isinstance(other, Element):
            other = other.value
        self = self * other
        return self

    def __pow__(self, power):
        neg = False

        if isinstance(power, Element):
            power = power.value

        if power < 0:
            neg = True
            power = abs(power)

        result = self
        for _ in range(1, power):
            result = self * result

        if neg is True:
            result = ~result
        
        return result

    def __invert__(self):
        inverse = None
        for el in self.group.elements:
            if self * el == self.group.eye:
                inverse = el
        return inverse

    """
        Logical operations
    """

    def __eq__(self, value):
        if isinstance(value, Element):
            return self.value == value.value
        return self.value == value
    
    def __lt__(self, value):
        if isinstance(value, Element):
            return self.value < value.value
        return self.value < value
    
    def __gt__(self, value):
        if isinstance(value, Element):
            return self.value > value.value
        return self.value > value
    
    def __le__(self, value):
        if isinstance(value, Element):
            return self.value <= value.value
        return self.value <= value
    
    def __ge__(self, value):
        if isinstance(value, Element):
            return self.value >= value.value
        return self.value >= value
    
    def __ne__(self, value):
        if isinstance(value, Element):
            return self.value != value.value
        return self.value != value

    
    """
        String conversions
    """

    def __repr__(self):
        return "Element({}, {})".format(self.value, str(self.group))

    def __str__(self):
        return "{}, {}".format(self.value, str(self.group))
