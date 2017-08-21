"""
The project Euler module for Sophie's project Euler problems. This is personal
code, some of it may have ben inspired by others and I intend to cite where
that's true. Otherwise, everthing is free to use with attribution.

is_prime: tests for primeness
sieve_of_eratosthenes: most efficient way to find primes I know of
prime_factors: recursively find prime factors
powerset: return powerset of a set. prolly adapted from itertools docs.
"""

from itertools import chain, combinations
import math
import numpy
import hashlib


def is_prime(num):
    """Return True if num is prime, else False"""
    prime_flag = True
    if num < 2:
        return False
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            prime_flag = False
            break
    return prime_flag


def test_prime():
    """test is_prime"""
    assert is_prime(7)
    assert is_prime(997)
    assert not is_prime(999)
    assert not is_prime(1)


def sieve_of_eratosthenes(num):
    """return all primes <= num"""
    limit = int(math.ceil(math.sqrt(num)))
    prime_array = numpy.ones((num, 1), dtype=bool)
    prime_array[0] = 0
    prime_array[1] = 0

    for i in range(2, limit + 1):
        if prime_array[i]:
            for j in range(i**2, num, i):
                prime_array[j] = False
    return set(numpy.where(prime_array)[0])


def primesfrom2to(n):
    # http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    """ Input n>=6, Returns a array of primes, 2 <= p < n """
    sieve = numpy.ones(n // 3 + (n % 6 == 2), dtype=numpy.bool)
    sieve[0] = False
    for i in range(int(n**0.5) // 3 + 1):
        if sieve[i]:
            k = 3 * i + 1 | 1
            sieve[((k * k) // 3)::2 * k] = False
            sieve[(k * k + 4 * k - 2 * k * (i & 1)) // 3::2 * k] = False
    return numpy.r_[2, 3, ((3 * numpy.nonzero(sieve)[0] + 1) | 1)]


def test_sieve():
    """test sieve_of_eratosthenes"""
    assert sum(sieve_of_eratosthenes(10)) == 17


def t_num(x): return x * (x + 1) / 2  # pylint: disable=invalid-name


def p_num(x): return x * (3 * x - 1) / 2  # pylint: disable=invalid-name


def h_num(x): return x * (2 * x - 1)  # pylint: disable=invalid-name


def test_shape_nums():
    """test shape nums"""
    assert p_num(4) + p_num(7) == p_num(8)
    assert t_num(285) == p_num(165) == h_num(143) == 40755

# def prime_factors(n):
#     i = 2
#     factors = {}
#     while i <= n:
#         while n%i == 0:
#             n /= i
#             factors[i] = factors.get(i,0) + 1
#         i = i + 1
#     return factors


def prime_factors(num):
    """return all prime factors of num"""
    # step returns the ith number that is neither divisible by 2 nor 3
    def step(x): return 1 + (x << 2) - ((x >> 1) << 1)
    max_query = int(math.floor(math.sqrt(num)))
    q_index = 1
    # next line catches edge cases of 2 & 3 being a factor
    query = 2 if num % 2 == 0 else 3  # query is 2 if divisible by 2 otherwise 3
    while query <= max_query and num % query != 0:
        query = step(q_index)
        q_index += 1

    if query <= max_query:
        out = [query] + prime_factors(num // query)
    else:
        out = [num]
    return out


def test_p_factors():
    """test prime factors"""
    assert len(set(prime_factors(14))) == 2
    assert len(set(prime_factors(15))) == 2
    assert len(set(prime_factors(644))) == 3
    assert len(set(prime_factors(645))) == 3
    assert len(set(prime_factors(646))) == 3


def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    input_list = list(iterable)
    return chain.from_iterable(combinations(input_list, r) for r in range(len(input_list) + 1))


def test_powerset():
    """test powerset"""

    assert list(powerset([1, 2, 3])) == [(), (1, ), (2, ),
                                         (3, ), (1, 2), (1, 3), (2, 3), (1, 2, 3)]


def F():
    a, b = 0, 1
    yield a
    yield b
    while True:
        a, b = b, a + b
        yield b


def hash(answer):
    return hashlib.md5(bytes(str(answer), 'ascii')).hexdigest()
