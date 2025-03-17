def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def modInverse(A, M):
    if gcd(A, M) > 1:
      
        # modulo inverse does not exist
        return -1
    for X in range(1, M):
        if (((A % M) * (X % M)) % M == 1):
            return X
    return -1

c = 62324783949134119159408816513334912534343517300880137691662780895409992760262021

e = 65537

n = 1280678415822214057864524798453297819181910621573945477544758171055968245116423923
p = 1899107986527483535344517113948531328331
q = 674357869540600933870145899564746495319033

phi_n = (p-1) * (q-1)

d = modInverse(e, phi_n)

print(d)