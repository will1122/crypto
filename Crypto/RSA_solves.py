import gmpy2

def solvep(q,n):
    p = n/q
    return p

def solveq(p,n):
    q = n/p
    return q

def solven(p,q):
    n = p * q
    return n

def smalle(e,n):
    k = e
    while k > 0:
        d = k*n+1//n
        print(d)
        k-=1
    return null

def encrypt(m,e,n):
    c = pow(m,e,n)
    return c

def decrypt(p,e,n,c):
    q = n//p
    phi = (p-1)*(q-1)
    d = gmpy2.invert(e,phi)
    m = pow(c,d,n)
    return m

def solved(q,p,e):
    phi = (p-1)*(q-1)
    d = gmpy2.invert(e,phi)
    return d

def fermat_factor(n):
    assert n % 2 != 0

    a = gmpy2.isqrt(n)
    b2 = gmpy2.square(a) - n

    while not gmpy2.is_square(b2):
        a += 1
        b2 = gmpy2.square(a) - n

    p = a + gmpy2.isqrt(b2)
    q = a - gmpy2.isqrt(b2)
    print("p = {}".format(p))
    print("q = {}".format(q))

    return int(p), int(q)

def totientn(p,q):
    phi = (p-1)*(q-1)
    return phi
