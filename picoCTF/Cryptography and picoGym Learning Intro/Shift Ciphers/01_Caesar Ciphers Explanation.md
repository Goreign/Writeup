A Caesar cipher is a simple encryption technique that operates by shifting letters within the alphabet. Here’s how it works:

- If the shift is 1 then “a” becomes “b”, “b” becomes “c”, and so on.
- At the end of the alphabet, “z” wraps around to become “a”.
- The magnitude of the shift is the key.
- Since the letters wrap around, there are only so many shifts that one can do within the alphabet. The Caesar Cipher has only 25 possible keys.
- While manually applying each possible shift to a message (brute-forcing) would take a while, computationally, it can be done in less than a second. This greatly simplifies the cryptanalysis to just evaluating each decrypted result.

For more information and code examples, you can explore our [CTF Primer, Substitution Ciphers chapter](https://primer.picoctf.org/#_substitution_ciphers).