import string

LOWERCASE_OFFSET = ord("a")
# LOWERCASE_OFFSET is 97
ALPHABET = string.ascii_lowercase[:16]
# ALPHABET is abcdefghijklmnop

def b16_encode(plain):
        enc = ""
        # if plain is 'a'
        for c in plain:
                binary = "{0:08b}".format(ord(c))
                # ord(c) -> 97
                # binary -> 01100001
                enc += ALPHABET[int(binary[:4], 2)]
                # int(binary[:4], 2) -> int(0110) -> 6
                # enc -> ALPHABET[6] -> g
                enc += ALPHABET[int(binary[4:], 2)]
                # int(binary[4:], 2) -> int(0001) -> 1
                # enc -> enc + ALPHABET[1] -> gb
        print(enc)
        return enc

def shift(c, k):
        t1 = ord(c) - LOWERCASE_OFFSET
        t2 = ord(k) - LOWERCASE_OFFSET
        return ALPHABET[(t1 + t2) % len(ALPHABET)]

# flag = "abc"
# key = "c"
# assert all([k in ALPHABET for k in key])
# assert len(key) == 1

# b16 = b16_encode(flag)
# enc = ""
# for i, c in enumerate(b16):
#         enc += shift(c, key[i % len(key)])
# print(enc)

enc = "mlnklfnknljflfjljnjijjmmjkmljnjhmhjgjnjjjmmkjjmijhmkjhjpmkmkmljkjijnjpmhmjjgjj"
for key in ALPHABET:
        s = ""
        res = ""
        for i, c in enumerate(enc):
                s += shift(c, key[i % len(key)])
        for i in range(0, len(s), 2):
                bin1 = "{0:04b}".format(ord(s[i]) - 97)
                bin2 = "{0:04b}".format(ord(s[i+1]) - 97)
                # print(bin1, bin2)
                
                o = int(bin1+bin2, 2)
                res += chr(o)
                # print(chr(o))

        print(ord(key) - 96, res)
        print("------------------")