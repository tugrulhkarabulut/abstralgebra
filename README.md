# abstralgebra

Abstract algebra library for Python (Work in progress)

I'm taking an abstract algebra course right now and an idea of creating a library for abstract algebra came to my mind. Any ideas on new features, how to improve etc. are welcome. And of course, any help on coding, optimization are gladly welcomed.

## Documentation

### Group Abstract Class

op - short for operation:
    Is an abstract method for defining the binary operation which is the operation the group is defined with.

elements:
    Is a property that returns the elements of the group

cartesianProduct:
    Returns the elements of the cartesian product of the group with another group

### Zn Group

Zn is a cyclic group under addition and it's defined on the ring of integers modulo n

### Zn_coprime Group

Zn* (Zn_coprime) is a group under multiplication and it's elements are the integers less than and coprime with n.