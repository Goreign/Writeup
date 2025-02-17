# Description
> Can you crack the password to get the flag?
Download the password checker here and you'll need the encrypted flag and the hash in the same directory too.
There are 7 potential passwords with 1 being correct. You can find these by examining the password checker script.

# Solution
**hexdump**
displays the contents of a file or data in hexadecimal (base-16) format.
```bash
$ hexdump -C level3.hash.bin 
00000000  16 02 6d 60 ff 9b 54 41  0b 34 35 b4 03 af d2 26  |..m`..TA.45....&|
00000010
```
```python
values = ["8799", "d3ab", "1ea2", "acaf", "2295", "a9de", "6f3d"]

for value in values:
    print(hash_pw(value))

output:
b'\xe6\x05\x1b;\xfeql\xc4\xa3\x8c/9\xec\x19\x98s'
b'+&\x89A\xeb\xe6\xa0)HBf\x06\x0f\xa7\x02C'
b'\x8f`E\x8c\xc6BC\xba;\x88\xf8\xbf\xcf\xa2i\xeb'
b'=\xf19d\xfd\x04=\xad\x82\xac\x80\xb91\xa7\x1f-'
b'\x16\x02m`\xff\x9bTA\x0b45\xb4\x03\xaf\xd2&'        <----
b'\xb9\xcc\xe7\xa7\xa6\x88\xe9\xdb\xca=\xd7\xf0F\x9d\xe5L'
b'\xcb\xdc\x1dV\xd5Jx\xa5\xba\x05CR\x8f\x85\xafj'

\x16 \x02  m   `   \xff \x9b  T   A  \x0b  4   5  \xb4 \x03 \xaf \xd2  &
  16   02  6d  60   ff   9b  54  41   0b  34   35   b4   03   af   d2  26
```

