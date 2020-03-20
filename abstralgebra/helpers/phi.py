from is_prime import is_prime
from prime_factorization import prime_factorization
from functools import reduce


def phi(n):
    if is_prime(n):
        # if the number is prime, phi(n) is simply n-1
        return n - 1
    # else you have to factor it, calculate phi for each factor and multiply them
    n_factors = prime_factorization(n)
    phi_factors = map(lambda factor: phi_helper(factor[0], factor[1]), n_factors)
    return reduce(lambda x, y: x * y, phi_factors)


def phi_helper(p, n):
    # Calculating phi of the numbers of the form p^n where p is prime
    return p ** n - p ** (n - 1)
