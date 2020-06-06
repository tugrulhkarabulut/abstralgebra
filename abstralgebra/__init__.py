import sys
import pathlib

from .Group import Group
from .Zn import Zn
from .Zn_coprime import Zn_coprime
from .Klein4 import Klein4
from .Element import Element
from .order import O


# Import helpers module
sys.path.insert(1, pathlib.Path(__file__).parent.absolute().__str__() + '/helpers')

from divisible_by import divisible_by
from is_prime import is_prime
from find_primes_up_to import find_primes_up_to
from prime_factorization import prime_factorization
from phi import phi

__all__ = ['Group', 'Zn']