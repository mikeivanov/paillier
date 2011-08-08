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

License and Copyright
---------------------
LGPL v3, see [LICENSE][3]
(C) 2011 Mike Ivanov

References
----------
[1]: http://code.google.com/p/thep/
[2]: http://readthedocs.org/docs/nose/en/latest/index.html
[3]: ./LICENSE

