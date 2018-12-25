import random


def is_prime(n):
    """
    >>> is_prime(2)
    True
    >>> is_prime(11)
    True
    >>> is_prime(8)
    False
    """
    # PUT YOUR CODE HERE
    for i in range(2, int(n / 2)):
        if n % i == 0:
            print("False")
            break
    else:
        print("True")



def gcd(a, b):
    """Returns the greatest common divisor of a and b.
    Should be implemented using recursion.

    >>> gcd(34, 19)
    1
    >>> gcd(39, 91)
    13
    >>> gcd(20, 30)
    10
    >>> gcd(40, 40)
    40
    """
    if b > a:
        return gcd(b, a)

    if a % b == 0:
        return b

    return gcd(b, a % b)

def generate_keypair(p, q):
    if not (is_prime(p) and is_prime(q)): print("True")

 #       raise ValueError('Both numbers must be prime.')
  #  elif p == q:
   #     raise ValueError('p and q cannot be equal')

    # n = pq
    # PUT YOUR CODE HERE

    n = p * q;

    # phi = (p-1)(q-1)
    # PUT YOUR CODE HERE

    phi = (p -1)*(q -1);

    # Choose an integer e such that e and phi(n) are coprime
    e = random.randrange(1, phi)

    # Use Euclid's Algorithm to verify that e and phi(n) are comprime
    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)

    # Use Extended Euclid's Algorithm to generate the private key
    d = multiplicative_inverse(e, phi)
    # Return public and private keypair
    # Public key is (e, n) and private key is (d, n)
    return ((e, n), (d, n))

def multiplicative_inverse(e, phi):
    e = e % phi;
    for x in range(1, 6):
        if ((e*x) % phi == 1 ):
            return x


if __name__ == '__main__':
    print("RSA Encrypter/ Decrypter")
    p = int(input("Enter a prime number (17, 19, 23, etc): "))
    q = int(input("Enter another prime number (Not one you entered above): "))
    print("Generating your public/private keypairs now . . .")
    public, private = generate_keypair(p, q)
    print("Your public key is ", public, " and your private key is ", private)
    message = input("Enter a message to encrypt with your private key: ")
    encrypted_msg = encrypt(private, message)
    print("Your encrypted message is: ")
    print(''.join(map(lambda x: str(x), encrypted_msg)))
    print("Decrypting message with public key ", public, " . . .")
    print("Your message is:")
    print(decrypt(public, encrypted_msg))
