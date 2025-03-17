user_input = 't\u200best '
print(user_input)

if 'test' in user_input:
    print("Matched!")
else:
    print("Not Matched!")
    eval(user_input + '()')

def test():
    print("trigger successfully")
    
    


# def conn():
#     r = remote("titan.picoctf.net", 53763)
#     r.recvuntil(b"==> ")
#     return r

# r = conn()


# s = "\x77\x69\x6e"
# if b'\x77' in s :
#     print("sad")

# print(s)

# def decrypt(cipher):
#     r.sendline(b"D")
#     r.recvuntil(b"Enter text to decrypt: ")
#     r.sendline(cipher)
#     print(r.recvuntil(b"decrypted ciphertext as hex (c ^ d mod n): "))

#     return r.recvline().strip().decode()