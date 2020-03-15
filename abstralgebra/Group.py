from abc import ABC, abstractmethod, abstractproperty


class Group(ABC):
    def __init__(self):
        super().__init__()

    # Defines which operation the group is under
    @abstractmethod
    def op(self):
        pass

    @abstractproperty
    def elements(self):
        return []

    def cartesianProduct(self, group):
        product = []
        for i in self.elements:
            for j in group.elements:
                product.append((i, j))

        return product