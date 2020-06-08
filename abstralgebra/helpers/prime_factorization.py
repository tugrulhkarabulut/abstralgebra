from find_primes_up_to import find_primes_up_to

from math import sqrt, log, floor
from functools import reduce

def prime_factorization(n):
    """
        This function factors a number n by checking the primes up to n/2 to
        see if n has a factor of a prime and calcuates the power of that factor.
        If no factor is found, it just returns the number itself with power 1

        Function returns a list of tuples with the prime factor and power.
        For example, 60 = 2^2 * 3 * 5. For 60, the function will return
        [ (2, 2), (3, 1), (5, 1)].
        If the number is prime, say 11, the function will return [ (11, 1) ]
    """
    
    primes_up_to_n_2 = find_primes_up_to(floor(n/2))

    factorization = []
    current_num = 1
    for p in primes_up_to_n_2:
        if current_num >= n:
            break
        
        if n % p == 0:
            factor = (p, log_simple(n, p))
            current_num *= factor[0] ** factor[1]
            factorization.append(factor)
    
    if len(factorization) == 0:
        factorization.append((n, 1))
    return factorization

def log_simple(n, k):
    """
        A function that simply finds how many k's does n have.
        For example 28 = 2 * 2 * 7, so log_simple(28, 2) will return 2
        and log_simple(28, 7) will return 1
    """

    log_result = 0
    while (n % k == 0):
        log_result += 1
        n /= k
    return log_result
