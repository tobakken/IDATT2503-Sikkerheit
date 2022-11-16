def ext_euclid(a, b):
    # Base Case
    if a == 0 :
        return b,0,1
             
    gcd,x1,y1 = ext_euclid(b%a, a)
     
    # Update x and y using results of recursive
    # call
    x = y1 - (b//a) * x1
    y = x1
     
    return gcd,x,y

def euclid(a, b):
    r = a%b
    while(r):
        a = b
        b = r
        r = a%b
    print(" GDC: " + str(b))

if __name__ == "__main__":
    print("Utvidede euclids algoritme, for å finne den inverse av 12^5: ", ext_euclid(12**5, 19))
    print("-7 mod 19: ",-7%19) 
