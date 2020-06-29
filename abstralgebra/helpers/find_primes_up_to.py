

from divisible_by import divisible_by
from is_prime import is_prime


def find_primes_up_to(n):
    if n < 2:
        return []
    
    primes = [2]
    currentNumber = 2
    while currentNumber <= n:
        if is_prime(currentNumber):
            primes.append(currentNumber)
        currentNumber = currentNumber + 1
    return primes