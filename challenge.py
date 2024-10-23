import random
from sympy import primerange

#  pgcd 
def pgcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

#inverse modulaire
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

def generate_large_prime():
    primes = list(primerange(50, 200))  # nbrs premiers entre 50 et 200
    return random.choice(primes)

def generate_keys():
    p = generate_large_prime()  # Premier
    q = generate_large_prime()  # 2 eme premier
    while p == q:  # Assurer que p et q sont diifferent
        q = generate_large_prime()

    N = p * q
    phi = (p - 1) * (q - 1)

    # Choisir e
    e = random.randrange(1, phi)
    while pgcd(e, phi) != 1:
        e = random.randrange(1, phi)

    # Calcule d
    d = modinv(e, phi)

    return ((N, e), d)

def encrypt(message, public_key):
    N, e = public_key
    encrypted_message = [(pow(ord(char), e, N)) for char in message]
    return encrypted_message

def decrypt(encrypted_message, private_key, N):
    decrypted_message = ''.join([chr(pow(char, private_key, N)) for char in encrypted_message])
    return decrypted_message






public_key, private_key = generate_keys()
N, e = public_key

message = "8493"
print(f"Message original : {message}")

encrypted_message = encrypt(message, public_key)
print(f"Message chiffré : {encrypted_message}")

decrypted_message = decrypt(encrypted_message, private_key, N)
print(f"Message déchiffré : {decrypted_message}")
