import os
import random
import ast
import base64

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Extended Euclidean Algorithm to calculate Modulo Multiplicative Inverse
# Implemented manually, instead of using Python's in-built modulo multiplicative inverse (pow(p, -1) % M)
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

# Checks if "primes.txt" exists. If not, generates primes up to 1e7 using Sieve of Eratosthenes and stores them in 'primes.txt'
# Returns a list of prime numbers
def generate_primes():
    primes = []
    if os.path.exists("primes.txt"):
        with open("primes.txt", "r") as file:
            primes = [int(line.strip()) for line in file]

    else:
        n = int(1e7)

        sieve = [True] * (n + 1)
        sieve[0] = sieve[1] = False
        for i in range(2, int(n**0.5) + 1):
            if sieve[i]:
                for j in range(i * i, n + 1, i):
                    sieve[j] = False
        primes = [i for i, is_prime in enumerate(sieve) if is_prime]

        with open("primes.txt", "w") as file:
            file.write("\n".join(map(str, primes)))

    return primes

# Saves key used in this session in their corresponding text files for subsequent encryption/decryption
def write_keys(public_key, private_key):
    with open('public_keys.txt', 'w') as public_file:
        public_file.writelines(map(str, public_key) + ['\n'])

    with open('private_keys.txt', 'w') as private_file:
        private_file.writelines(map(str, private_key) + ['\n'])

# Loads pre-existing keys from corresponding text files if they've been saved beforehand
def load_keys():
    private_keys_path = "private_keys.txt" 
    public_keys_path = "public_keys.txt"

    with open(public_keys_path, 'r') as public_keys_file:
        e = int(public_keys_file.readline())
        n = int(public_keys_file.readline())

    with open(private_keys_path, 'r') as private_keys_file:
        d = int(private_keys_file.readline())
        n = int(private_keys_file.readline())
    
    return ((e,n), (d,n))

def generate_key_pairs():
    # Selects two random different primes p, q
    primes = generate_primes()
    index1, index2 = random.sample(range(len(primes)), 2)
    while primes[index1] == primes[index2]:
        index2 = random.randint(0, len(primes) - 1)

    p, q = primes[index1], primes[index2]

    # Calculates N and phi(N) or Euler's Totient of N
    n = p * q

    phi = (p - 1) * (q - 1)
    
    # Chooses random value of e co-prime to phi, ie. gcd(e, phi) = 1
    e = random.randint(1, phi)
    g = gcd(e,phi) 
    while g != 1:
        e = random.randint(1, phi)
        g = gcd(e, phi)

    # Calculates d = modulo inverse of e under phi using Extended Euclidean Algorithm
    d = egcd(e, phi)[1]
    
    d = d % phi
    if(d < 0):
        d += phi
        
    return ((e,n), (d,n))

# Encrypts given string using public key pair (e, n)
def encrypt(message, public_key):
    key, n = public_key
    # Iterates through the characters of the message (c), raises its ASCII value to the power of key (c ^ key) modulo n.
    ciphertext = [pow(ord(char), key, n) for char in message]

    # Converts the array to a string representation, applies base-64 encoding, then converts the base-64 blocks back to ASCII
    return base64.b64encode(bytes(str(ciphertext), 'ascii')).decode()

# Decrypts given string using private key pair (d, n)
def decrypt(message, private_key):
    key, n = private_key
        
    # Decodes base-64 blocks into strings
    message_decoded = base64.b64decode(message).decode()
    # Parses the string representation into list of numbers
    arr = ast.literal_eval(message_decoded)

    plaintext = ""
    # Iterates through each number, performs (c ^ key) modulo n, essentially decrypting
    message_decrypted = [chr(pow(char, key, n)) for char in arr]
    
    return plaintext.join(message_decrypted)