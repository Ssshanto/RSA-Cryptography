from utils import *
import argparse

# Default message, if given no input
message = "CSE-4743 final exam was difficult"

# Parser to parse command-line flags
# Flags-list mentioned in README.md
parser = argparse.ArgumentParser()
parser.add_argument("-e", "--encrypt", type=str, help="Encrypts given string")
parser.add_argument("-d", "--decrypt", type=str, help="Decrypts given string")
parser.add_argument("-ef", "--encrypt_file", action='store_true', help="Encrypts given string from message.txt")
parser.add_argument("-df", "--decrypt_file", action='store_true', help="Decrypts given string from message.txt")
parser.add_argument("-l", "--load", action='store_true', help="Reads Public/Private keys from file")
parser.add_argument("-s", "--save", action='store_true', help="Stores Public/Private keys into file")
parser.add_argument("-v", "--verbose", action='store_true', help="Shows all outputs and key values")
parser.add_argument("-w", "--write", action='store_true', help="Writes output message into message.txt")
args = parser.parse_args()

if __name__ == "__main__":
    if args.load:
        public_key, private_key = load_keys()
        print("Loaded keys from 'public_keys.txt' and 'private_keys.txt'")
    else:
        public_key, private_key = generate_key_pairs()
        print("Generated new pair of public and private keys.")

    if args.verbose:
        print(f"Public Key pair: e = {public_key[0]}, n = {public_key[1]}")
        print(f"Private Key pair: d = {private_key[0]}, n = {private_key[1]}")

    if args.encrypt != None:
        message = args.encrypt
    elif args.decrypt != None:
        message = args.decrypt
    elif args.encrypt_file or args.decrypt_file:
        if not os.path.exists('message.txt'):
            raise ValueError("'message.txt' file does not exist.")
        with open('message.txt', 'r') as message_file:
            message = message_file.readline()

    if args.decrypt or args.decrypt_file:
        plaintext = decrypt(message, private_key)
        print(f"Decrypted Plaintext: {plaintext}")
        if args.write:
            with open('message.txt', 'w') as message_file:
                message_file.write(ciphertext)
            print("Wrote output to 'message.txt'")
    
    else:
        ciphertext = encrypt(message, public_key)
        print(f"Encrypted Ciphertext: {ciphertext}")
        if args.write:
            with open('message.txt', 'w') as message_file:
                message_file.write(ciphertext)

    if args.save:
        write_keys(public_key, private_key)
        print("Wrote keys to 'private_keys.txt' and 'public_keys.txt'")


"""
Example Commands:
python main.py -l -v -df
"""
