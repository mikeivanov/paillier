import math
import primes

def invmod(a, p, maxiter=1000000):
    '''
    http://code.activestate.com/recipes/576737-inverse-modulo-p/
    The multiplicitive inverse of a in the integers modulo p.
    Return b s.t.
    a * b == 1 mod p
    '''
    if a == 0:
        raise ValueError('0 has no inverse mod %d' % p)
    r = a
    d = 1
    for i in xrange(min(p, maxiter)):
        d = ((p // r + 1) * d) % p
        r = (d * a) % p
        if r == 1:
            break
    else:
        raise ValueError('%d has no inverse mod %d' % (a, p))
    return d

class PrivateKey(object):
    def __init__(self, p, q, n):
        self.l = (p-1) * (q-1)
        self.m = invmod(self.l, n)

class PublicKey(object):
    def __init__(self, n):
        self.n = n
        self.n_sq = n * n
        self.g = n + 1

def generate_keypair(bits):
    p = primes.generate_prime(bits / 2)
    q = primes.generate_prime(bits / 2)
    n = p * q
    return PrivateKey(p, q, n), PublicKey(n)

def encrypt(pub, plain):
    while True:
        r = primes.generate_prime(long(round(math.log(pub.n, 2))))
        if r > 0 and r < pub.n:
            break
    x = pow(r, pub.n, pub.n_sq)
    cipher = (pow(pub.g, plain, pub.n_sq) * x) % pub.n_sq
    return cipher

def e_add(pub, a, b):
    return a * b % pub.n_sq

def decrypt(priv, pub, cipher):
    x = pow(cipher, priv.l, pub.n_sq) - 1
    plain = ((x // pub.n) * priv.m) % pub.n
    return plain

