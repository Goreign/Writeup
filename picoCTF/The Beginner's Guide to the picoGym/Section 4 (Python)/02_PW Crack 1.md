# Description
> Can you crack the password to get the flag?
Download the password checker here and you'll need the encrypted flag in the same directory too.

# Solution
```python
flag_enc = open('level1.flag.txt.enc', 'rb').read()

def level_1_pw_check():
    user_pw = input("Please enter correct password for flag: ")
    if( user_pw == "691d"):
        print("Welcome back... your flag, user:")
        decryption = str_xor(flag_enc.decode(), user_pw)
        print(decryption)
        return
    print("That password is incorrect")
```

Python file will open `level1.flag.txt.enc`. 
All we need to do is enter the password. Can u find it?