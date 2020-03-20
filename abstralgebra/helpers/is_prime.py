from math import sqrt, ceil

from find_primes_up_to import find_primes_up_to


def is_prime(n):
    """
        Function to check whether a given number is prime or not
    """
    n_sqr = ceil(sqrt(n))
    for i in range(2, n_sqr):
        if n % i == 0:
            return False
    return True
