import math

def RSA_angrep(n):
    t = math.ceil(math.sqrt(n))
    d = math.sqrt(t**2-n)
    while(d.is_integer() == False):
        t += 1
        d = math.sqrt(t**2-n)
    return t, d

if __name__ == "__main__":
    t, d = RSA_angrep(152416580095517)
    p = t + d
    q = t - d
    print("Faktorene er {} og {}".format(int(p), int(q)))
    