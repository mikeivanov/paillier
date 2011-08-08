import primes

def test_ipows():
    for a in range(1, 10):
        for b in range (1, 10):
            for n in range(2, 11):
                yield check_ipow, a, b, n

def check_ipow(a, b, n):
    result = list(primes.ipow(a, b, n))
    assert result[-1] == pow(a, b) % n

def test_is_probably_prime():
    known_primes = (15484279, 32451217, 86027297, 179424097, 982451653,
                    2038072919, 18125114801, 22801762469)
    for prime in known_primes:
        yield check_is_probably_prime, prime, True
        for other in known_primes:
            yield check_is_probably_prime, prime * other, False

def check_is_probably_prime(x, is_prime):
    assert primes.is_probably_prime(x) == is_prime

def test_generate_prime():
    for i in xrange(3, 10):
        yield check_generate_prime, pow(2, i)

def check_generate_prime(bits):
    assert primes.is_probably_prime(primes.generate_prime(bits))

