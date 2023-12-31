# RSA-Cryptography
A naive implementation of the RSA algorithm for the course CSE-4743 Cryptography and Network Security at Islamic University of Technology.

# Example Usage
`python main.py -s -v -w -e "Hello, how are you doing today?"`

Generated new pair of public and private keys.
Public Key pair: e = 1211302656003, n = 3446597376811
Private Key pair: d = 1705028247435, n = 3446597376811
Encrypted Ciphertext: WzMyNTMzMDE1MzI0MTMsIDQwNzMwMzEwMzcxNSwgMjE1NjgwNTQxMDc1LCAyMTU2ODA1NDEwNzUsIDEyNjcwOTU1ODc1NDIsIDEwMTE1MjI4ODYzNjksIDE3ODg0NTAxNDIwMjEsIDExNzA0MDY5NTI0MywgMTI2NzA5NTU4NzU0MiwgMTIxNjE2MzI1OTM1LCAxNzg4NDUwMTQyMDIxLCAyMTgxNjAwMDkzMDk5LCAyNjc2MTEyMjg4MzEwLCA0MDczMDMxMDM3MTUsIDE3ODg0NTAxNDIwMjEsIDQyNTI0NjY4NjA5MywgMTI2NzA5NTU4NzU0MiwgMTAwNDMzMzMxNTk5NCwgMTc4ODQ1MDE0MjAyMSwgMjYxMjI0MDE2NzE5NywgMTI2NzA5NTU4NzU0MiwgMTc3NzEwNzQ2OTE2OCwgMjI3MjA3NjE0MTU5NSwgMTAxNTgyMzY3NjQyNCwgMTc4ODQ1MDE0MjAyMSwgMjk2MTExOTA5MjI2MywgMTI2NzA5NTU4NzU0MiwgMjYxMjI0MDE2NzE5NywgMjE4MTYwMDA5MzA5OSwgNDI1MjQ2Njg2MDkzLCAzMTc3MDc4NTI0MjU2XQ==
Wrote keys to 'private_keys.txt' and 'public_keys.txt'

`python main.py -l -v -df`

Loaded keys from 'public_keys.txt' and 'private_keys.txt'
Public Key pair: e = 1211302656003, n = 3446597376811
Private Key pair: d = 1705028247435, n = 3446597376811
Decrypted Plaintext: Hello, how are you doing today?

# Arguments
## Encryption and Decryption:

-e, --encrypt &lt;string>: Encrypts the given string.
-d, --decrypt &lt;string>: Decrypts the given string.
-ef, --encrypt_file: Encrypts the string content from a file named "message.txt".
-df, --decrypt_file: Decrypts the string content from a file named "message.txt".

## Key Management:

-l, --load: Reads public and private keys from their respective files.
-s, --save: Stores public and private keys into their respective files.

## Output and Logging:

-v, --verbose: Displays detailed output, including key values.
-w, --write: Writes the output message to a file named "message.txt".
