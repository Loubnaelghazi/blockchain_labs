import random
import secrets
from sympy import primerange

# pgcd
def pgcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# inverse modulaire de e modulo ohi 
#but dan RSA : est de trouver la cle d 
def modinv(e, phi):
    d = 0
    x1, x2, x3 = 1, 0, phi
    y1, y2, y3 = 0, 1, e

    while y3 != 0:
        q = x3 // y3
        x1, x2, x3, y1, y2, y3 = (y1, y2, y3, 
                                   x1 - q * y1, x2 - q * y2, x3 - q * y3)
   
   
    if x3 == 1:
        return x2 % phi
    return None

# grands premiers
def generate_large_prime():
    primes = list(primerange(50, 200))
    return random.choice(primes)





def generate_keys():
    p = generate_large_prime()
    q = generate_large_prime()
    while p == q:
        q = generate_large_prime()

    N = p * q
    phi = (p - 1) * (q - 1)

    e = random.randrange(1, phi)
    while pgcd(e, phi) != 1:
        e = random.randrange(1, phi)

    d = modinv(e, phi)
    return ((N, e), d)



def encrypt(message, public_key):
    N, e = public_key
    k = secrets.randbits(1024)
    encrypted_message = [(pow(ord(char), e, N) + k) for char in message]
    return encrypted_message, k  


def decrypt(encrypted_message, private_key, N, k):
    decrypted_message = ''.join([chr(pow(char - k, private_key, N)) for char in encrypted_message])
    return decrypted_message







###################################################################
public_key, private_key = generate_keys()
N, e = public_key

message = "Salam"

encrypted_message, k = encrypt(message, public_key)
print(f"Message chiffré : {encrypted_message}")
#print(f"Constante aléatoire utilisée : {k}")


decrypted_message = decrypt(encrypted_message, private_key, N, k)
print(f"Message déchiffré : {decrypted_message}")
