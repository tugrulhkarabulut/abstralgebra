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
    
    @abstractproperty
    def eye(self):
        pass

    def __len__(self):
        return len(self.elements)

    def cartesianProduct(self, group):
        product = []
        for i in self.elements:
            for j in group.elements:
                product.append((i, j))

        return product

    __mul__ = cartesianProduct


    def __getitem__(self, index):
        return self.elements[index]