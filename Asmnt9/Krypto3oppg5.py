from math import factorial

def euclid(a, b):
    r = a%b
    while(r):
        a = b
        b = r
        r = a%b
    print(" GDC: " + str(b))
    return b

def pollard(n):
    a = 3
    B_factorial = factorial(5)
    A = (a**B_factorial)%n
    D = euclid(A-1, n)
    while D <= 1:
         a += 1
         A = (a**B_factorial)%n
         D = euclid(A-a, n)
    print(D)

if __name__ == "__main__":
    pollard(1829)
    print(1829/31)
    pollard(6319)
    print(6319/71)
    print("a) faktorer i '1829' -> 31 59")
    print("c) faktorer i '6319' -> 71 89")