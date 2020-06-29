from math import sqrt, ceil


def is_prime(n):
    """
        Function to check whether a given number is prime or not
    """
    n_sqr = ceil(sqrt(n) + 1)
    for i in range(2, n_sqr):
        if n % i == 0:
            return False
    return True
