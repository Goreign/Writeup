# Description
Can you abuse the oracle?
An attacker was able to intercept communications between a bank and a fintech company. They managed to get the message (ciphertext) and the password that was used to encrypt the message.
Additional details will be available after launching your challenge instance.

# Solution
**CPA**
```
$ xxd -p secret.enc | tr -d '\n'
53616c7465645f5f6a58c1eff3395629e1705433cfbe71fb0324aa714573fc35b66e5c4b353dc12563bab309dc51d33973ba1a0e312171754dfe308d9534aa87
```
you can not send `2` via CLI cause it will send `0x32` (ASCII)
```
print(b"2")
print("2".encode)
print(ord("2"))
print(b"\x02")

output ->
b'2'
<built-in method encode of str object at 0x7f87ea46fdb0>
50
b'\x02'
```