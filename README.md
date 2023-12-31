# RSA-Cryptography

A naive implementation of the RSA algorithm for the course CSE-4743 Cryptography and Network Security at Islamic University of Technology.

# Example Usage

`python main.py -s -v -w -e "Hello, how are you doing today?"`

Generated new pair of public and private keys.\
Public Key pair: e = 1211302656003, n = 3446597376811\
Private Key pair: d = 1705028247435, n = 3446597376811\
Wrote keys to 'private_keys.txt' and 'public_keys.txt'

`python main.py -l -v -df`

Loaded keys from 'public_keys.txt' and 'private_keys.txt'\
Public Key pair: e = 1211302656003, n = 3446597376811\
Private Key pair: d = 1705028247435, n = 3446597376811\
Decrypted Plaintext: Hello, how are you doing today?

# Arguments

## Encryption and Decryption:

-e, --encrypt &lt;string>: Encrypts the given string.\
-d, --decrypt &lt;string>: Decrypts the given string.\
-ef, --encrypt_file: Encrypts the string content from a file named "message.txt".\
-df, --decrypt_file: Decrypts the string content from a file named "message.txt".\

## Key Management:

-l, --load: Reads public and private keys from their respective files.\
-s, --save: Stores public and private keys into their respective files.

## Output and Logging:

-v, --verbose: Displays detailed output, including key values.\
-w, --write: Writes the output message to a file named "message.txt".
