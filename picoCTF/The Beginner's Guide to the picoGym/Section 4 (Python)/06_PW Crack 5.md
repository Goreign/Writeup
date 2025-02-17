# Description
> Can you crack the password to get the flag?
Download the password checker here and you'll need the encrypted flag and the hash in the same directory too. Here's a dictionary with all possible passwords based on the password conventions we've seen so far.
# Solution 1
```python
correct_pw_hash = open('level5.hash.bin', 'rb').read()
print(correct_pw_hash)

...

pos_pw_list = []
with open('dictionary.txt', 'r') as file:
    for line in file:
        pos_pw_list.append(line.strip())

for value in pos_pw_list:
    h = hash_pw(value)
    if(h == b'\x126P\xdd\x05`Xy\x18\xb3\xd7q\xcf\x0c\x01q'):
        print(value, hash_pw(value))

level_5_pw_check()
```

Brute Force