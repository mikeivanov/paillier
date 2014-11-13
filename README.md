Pure Python Paillier Homomorphic Cryptosystem
=============================================

This is a very basic pure Python implementation of the Paillier
Homomorphic Cryptosystem.

Homomorphic Cryptosystems
-------------------------

The idea of homomorphic computation is to encrypt some numbers,
perform algebraic operations like "add" and "multiply" on
*cyphertexts*, then decrypt the result and find it to be exactly the
same as if corresponding "+" and "*" operations were applied to the
plaintexts.

In other words, a homomorphic cryptosystem enables cryptographically
secure computations in an untrusted environment.

Paillier cryptosystem
---------------------

Paillier cryptosystem is a probabilistic asymmetric algorithm for
public key cryptography. Paillier cryptosystem is partially
homomorphic as it can only add encrypted numbers or multiply an
encrypted number by an unencrypted multiplier.

Implementation
--------------

This pure Python implementation exploits Python's long type with
its arbitrary precision arithmetics. Public key is serializable, thus
it can be pickled along with the encrypted numbers and sent to a
remote server for computation.

The code is loosely based on [Thep][1] and a few ActiveState recipes.

Please note that this implementation's primary purpose is education;
it is **not suitable for production use** as it is.

Installation and Tests
----------------------

The paillier.py module has no external dependencies besides included
primes.py. Simply run demo.py to see it in action.

To run unit tests please install [Nose][2]:

    $ pip install -r requirements.txt
    $ nosetests
    ...............
    Ran 814 tests in 11.544s
    OK

Usage
-----

    $ ipython
    Python 2.7.1 (r271:86832, Jun 16 2011, 16:59:05)
    Type "copyright", "credits" or "license" for more information.

    In [1]: from paillier.paillier import *

    In [2]: priv, pub = generate_keypair(128)

    In [3]: x = encrypt(pub, 2)

    In [4]: y = encrypt(pub, 3)

    In [5]: x,y
    Out[5]:
    (72109737005643982735171545918..., 9615446835366886883470187...)

    In [6]: z = e_add(pub, x, y)

    In [7]: z
    Out[7]: 71624230283745591274688669...

    In [8]: decrypt(priv, pub, z)
    Out[8]: 5L


License and Copyright
---------------------
LGPL v3, see [LICENSE][3]

(C) 2011 Mike Ivanov


[1]: http://code.google.com/p/thep/
[2]: http://readthedocs.org/docs/nose/en/latest/index.html
[3]: https://github.com/mikeivanov/paillier/blob/master/LICENSE

