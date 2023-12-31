from utils import *

if __name__ == "__main__":
    public_key, private_key = generate_key_pairs()
    message = "hello how are you"
    ciphertext = encrypt(message, public_key)
    print(f"Encrypted Message: {ciphertext}")
    plaintext = decrypt(ciphertext, private_key)
    print(f"Decrypted Message: {plaintext}")

