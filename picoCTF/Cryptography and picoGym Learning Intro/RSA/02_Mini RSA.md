# Description
What happens if you have a small exponent? There is a twist though, we padded the plaintext so that (M ** e) is just barely larger than N. Let's decrypt this: ciphertext

N: 16157656843214...

e: 3

ciphertext (c): 12200123185888...

# Solution:

$c = m^e\:mod\:n$, $e = 3$, from 1 to i(such as 5000), if $i*n + c$ has Cube Root, we can get `m`


