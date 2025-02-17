# Description
> Can you crack the password to get the flag?
Download the password checker here and you'll need the encrypted flag in the same directory too.

# Solution
```python
flag_enc = open('level2.flag.txt.enc', 'rb').read()

def level_2_pw_check():
    # i added this line. So u can see the passwd directly.
    print(chr(0x64) + chr(0x65) + chr(0x37) + chr(0x36))  

    user_pw = input("Please enter correct password for flag: ")
    if( user_pw == chr(0x64) + chr(0x65) + chr(0x37) + chr(0x36) ):
        print("Welcome back... your flag, user:")
        ...
```
