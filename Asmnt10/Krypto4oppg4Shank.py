import math
def shanks(p, alpha, beta):
    m = math.ceil(math.sqrt(p))
    alphalist = {}
    betalist = {}
    for i in range(m):
        alphalist[i] = (alpha**(m*i))%p
    for j in range(m):
        betalist[j] = (beta*pow(alpha, -j, p))%p
    return m, alphalist, betalist


if __name__ == "__main__":
    m, alist, blist = shanks(41,6,3)
    print(alist)
    print(blist)
    for i in range(len(alist)):
        if blist[i] in alist.values():
            print(f"Elementet på plass {i} i blist finnes også i alist, ")
    print(f"log_6 3 = ({m}*2+1) mod 41")
    print("7*2+1 = 15")
    print("6^15 mod 41 = 3, så dette stemmer")