
"""
    Sieve of Eratosthenes implementation
"""

from divisible_by import divisible_by


def find_primes_up_to(n):
    N = list(range(2, n + 1)) # Numbers from 2 to n
    primes = []
    while (len(N) > 0):
        # The idea is adding the first element of N to the 'primes' and
        # discarding the elements that are multiples of that element
        # since they are not prime
        primes.append(N[0])
        divisible_by_ = divisible_by(N[0])
        N = [k for k in N if divisible_by_(k) is False]
    return primes