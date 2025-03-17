with open('password.enc') as file:
    content = int(file.read())
    print(content)

c_two = 4707619883686427763240856106433203231481313994680729548861877810439954027216515481620077982254465432294427487895036699854948548980054737181231034760249505
print('--------------------')
print(str(content * c_two).encode())

passwd = int("a9573f66360", 16) // 2

passwd = 232740238640
print("passwd: ", passwd)
# print(passwd.to_bytes(5, "big"))

print(passwd.to_bytes((passwd.bit_length() + 7) // 8, "big"))

number = 97
byte_data = number.to_bytes(1, "big")
print(byte_data)

print(b"2")
print("2".encode)
print(ord("2"))
print(b"\x02")