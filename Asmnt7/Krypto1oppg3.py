ALFABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZÆØÅ"
alfabet = "abcdefghijklmnopqrstuvwxyzæøå"
def crypt_formula(x):
    return (11*x - 5)%29

def print_alfabet():
    for i in range(29):
        print(" f(" + str(i) + ") bokstav " + ALFABET[i] + " blir til " + ALFABET[crypt_formula(i)])

def inverse_formula(y):
    return (8*y + 11)%29

def print_inverse():
    for i in range(29):
        print(" f^-1(" + str(i) + ") bokstav " + ALFABET[i] + " blir til " + ALFABET[inverse_formula(i)])

if __name__ == "__main__":
    print("Oppg 3 a)")
    print_alfabet()

    print("\n\nOppg 3 b)")
    print("f er en permutasjon siden dette er en områkering av alle bokstavene. Hver bokstav har fått ny plass" + 
    " og ingen bokstaver forekommer flere eller ingen ganger.")

    print("\n\nOppg 3 c)")
    print_inverse()
    print("Ved å sette opp to ligninger ut fra tabellen over:")
    print("a + b = 19")
    print("2a + b = 27")
    print("Løser for a og b og får a = 8 og b = 11")
    print("Invers formel blir dermed: (8 * y + 11) mod 29 ")

    print("\n\nOppg d)")
    m = "alice"
    for i in range(len(m)):
        print(ALFABET[crypt_formula(alfabet.index(m[i]))], end='')


    print("\n\nOppg e)")
    c = "SIØPBE"
    for i in range(len(c)):
        print(alfabet[inverse_formula(ALFABET.index(c[i]))], end='')