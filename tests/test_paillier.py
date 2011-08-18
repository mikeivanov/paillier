import random
from nose.tools import assert_raises
import paillier

def test_invmod():
    assert_raises(ValueError,  paillier.invmod, 0, 7)
    assert paillier.invmod(1, 7) == 1
    p = 101
    for i in range(1, p):
        iinv = paillier.invmod(i, p)
        assert (iinv * i) % p == 1

def test_keys_int():
    priv = paillier.PrivateKey(7, 11, 77)
    assert priv.l == 60
    assert priv.m == 9
    pub = paillier.PublicKey(77)
    assert pub.g == 78

def test_keys_long():
    priv, pub = paillier.generate_keypair(256)
    for i in range(5):
        assert paillier.invmod(priv.m, pub.n) == priv.l

def test_encrypt_non_repeatable():
    pub = paillier.PublicKey(15484279*32451217)
    for i in range(10):
        pt = random.randint(0, 1000000)
        assert paillier.encrypt(pub, pt) != paillier.encrypt(pub, pt)

def test_decrypt():
    for i in range(5):
        priv, pub = paillier.generate_keypair(64)
        for j in range(5):
            pt = long(random.randint(0, 1000000))
            ct = paillier.encrypt(pub, pt)
            assert pt == paillier.decrypt(priv, pub, ct)

def test_e_add():
    for i in range(5):
        priv, pub = paillier.generate_keypair(128)
        for j in range(5):
            a = long(random.randint(0, 1000000))
            b = long(random.randint(0, 1000000))
            ca, cb = paillier.encrypt(pub, a), paillier.encrypt(pub, b)
            cs = paillier.e_add(pub, ca, cb)
            s = paillier.decrypt(priv, pub, cs)
            assert a + b == s
        
def test_e_add_const():
    for i in range(5):
        priv, pub = paillier.generate_keypair(128)
        for j in range(5):
            a = long(random.randint(0, 1000000))
            c = paillier.encrypt(pub, a)
            for n in range(0, 11):
                cs = paillier.e_add_const(pub, c, n)
                s = paillier.decrypt(priv, pub, cs)
                assert a + n == s
        
def test_e_mul_const():
    for i in range(5):
        priv, pub = paillier.generate_keypair(128)
        for j in range(5):
            a = long(random.randint(0, 1000000))
            c = paillier.encrypt(pub, a)
            for n in range(0, 11):
                cs = paillier.e_mul_const(pub, c, n)
                s = paillier.decrypt(priv, pub, cs)
                assert a * n == s

