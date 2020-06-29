from .Element import Element

class Group():
    def __init__(self, elements=None, eye=None, op=None):
        if len(elements) == 0:
            raise ValueError('Elements are empty.')
        if isinstance(elements[0], Element):
            self.elements_ = elements
        else:
            self.elements_ = list(map(lambda el: Element(el, self), elements))

        self.eye_ = eye
        self.op_ = op

    # Defines which operation the group is under
    def op(self, x, y):
        return self.op_(x, y)

    @property
    def elements(self):
        return self.elements_

    @property
    def values(self):
        return list(map(lambda x: x.value, self.elements_))
    
    @property
    def eye(self):
        return self.eye_

    def __len__(self):
        return len(self.elements)

    def cartesianProduct(self, group):
        product = []
        for i in self.elements:
            for j in group.elements:
                product.append((i.value, j.value))

        return product

    __mul__ = cartesianProduct

    def externalDirectProduct(self, group):
        elements = self.cartesianProduct(group)
        op = lambda a,b: (self.op(a[0], b[0]), group.op(a[1], b[1]))
        eye = (self.eye, group.eye)
        return Group(elements=elements, eye=eye, op=op)


    def __getitem__(self, index):
        return self.elements[index]