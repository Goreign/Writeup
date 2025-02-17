# Description
> Can you crack the password to get the flag?
Download the password checker here and you'll need the encrypted flag and the hash in the same directory too.
There are 100 potential passwords with only 1 being correct. You can find these by examining the password checker script.

# Solution 1
```python
flag_enc = open('level4.flag.txt.enc', 'rb').read()
correct_pw_hash = open('level4.hash.bin', 'rb').read()
print(correct_pw_hash)     

...

pos_pw_list = ["8c86", "7692",...]
for value in pos_pw_list:
    h = hash_pw(value)
    if(h == b'd\xc1\xef\x006\xa9\xa8\xd1v\xfb\xc3\x81\xc4\xab\xdaR'):
        print(value, hash_pw(value))
level_4_pw_check()

output: 
$ python level4.py 
b'd\xc1\xef\x006\xa9\xa8\xd1v\xfb\xc3\x81\xc4\xab\xdaR'
9f63 b'd\xc1\xef\x006\xa9\xa8\xd1v\xfb\xc3\x81\xc4\xab\xdaR'
Please enter correct password for flag:
```

# Solution 2: xor
```python
pos_pw_list = ["8c86", "7692",...]
for value in pos_pw_list:
    h = hash_pw(value)
    res = bytes(a ^ b for a, b in zip(h, correct_pw_hash))
    num = int.from_bytes(res, byteorder="big")
    if(num == 0):
        print(value, hash_pw(value))
...
```
