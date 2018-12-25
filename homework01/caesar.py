import random

def encrypt_caesar(plaintext):
    """
    Encrypts plaintext using a Caesar cipher.

    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = ""
    n = ord('z') - ord('a') + 1
    for c in plaintext:
        if not c.isalpha():
            ciphertext += c
            continue
        isUpper = c.isupper()
        newC = c.lower()
        asciiCode = ord(newC) - ord("a")
        asciiCode += 3
        asciiCode %= n
        asciiCode += ord("a")
        newC = chr(asciiCode)
        if isUpper:
            newC = newC.upper()
        ciphertext += newC

    return ciphertext


def decrypt_caesar(ciphertext):
    """
    Decrypts a ciphertext using a Caesar cipher.

    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ""
    n = ord('z') - ord('a') + 1
    for c in ciphertext:
        if not c.isalpha():
            plaintext += c
            continue
        isUpper = c.isupper()
        newC = c.lower()
        asciiCode = ord(newC) - ord("a")
        asciiCode += n-3
        asciiCode %= n
        asciiCode += ord("a")
        newC = chr(asciiCode)
        if isUpper:
            newC = newC.upper()
        plaintext += newC

    return plaintext
    pass
