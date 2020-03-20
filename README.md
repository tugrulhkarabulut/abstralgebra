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

Zn is a cyclic group under addition and it's defined on the ring of integers modulo n. It is defined based on the Group class.

Examples:

`Z14 = Zn(14)`

`Z13 = Zn(13)`

`Z14.elements # Returns [0, 1, ..., 13]`

`Z14.op(9, 7) # Returns 2 (9 + 7 = 16 % 14 = 2)`

`Z14.isGeneratedBy(3) # Returns true since gcd(14, 3) = 1`

`Z14.generateSubgroupBy(4) # Returns the generator of 4 in Z14, i.e. [4, 8, 12, 2, 6, 10, 0]`

`Z14.exists(5) # Checks if 5 exists in Z14`

`Z14.eye # Returns the identity element of Z14`

`Z14.n # Returns n`

`Z14.mod(21) # Returns 21 modulo 14, i.e 7`

`Z14.cartesianProduct(Z13) # Returns elements of the cartesian product`

### Zn_coprime Group

Zn* (Zn_coprime) is a group under multiplication and it's elements are integers less than and coprime with n. It is also defined based on the group class.

Examples:

`Z14_coprime = Zn_coprime(14)`

`Z14_coprime.elements # [1, 3, 5, 9, 11, 13]`

`Z14_coprime.op(4, 5) # 6 (4*5 = 20 % 14 = 6)`

`Z14_coprime.mod(20) # 6`

`Z14_coprime.eye # 1`

`Z14_coprime.generateSubgroupBy(9) # [9, 11, 1]`

`Z13 = Zn(13)`

`Z14_coprime * Z13 # Returns the elements of cartesian product of the two group`

### Element Class
Element class that represents a group element. It can be defined with a value and a group

Examples:

`Z3 = Zn(3)`

`el_1 = Element(2, Z3)`

`el_2 = Element(1, Z3)`

`el_1 * el_2  # 0`

`el_1 > el_2 # True`

`el_2 > 2 # False`

`el_1 ** 2 # 1 (2 + 2 = 4 % 3 = 1)`