ALFABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZÆØÅ"
alfabet = "abcdefghijklmnopqrstuvwxyzæøå"

def vig_encrypt(m, k):
    return (alfabet.index(m) + alfabet.index(k))%29

def vig_decrypt(c, k):
    return (ALFABET.index(c) - ALFABET.index(k))%29

def vig_encrypt_text(m, k):
    for i in range(len(m)):
        if m[i] != ' ':
            print(ALFABET[vig_encrypt(m[i], k[i%len(k)])], end='')

def vig_decrypt_text(c, k):
    for i in range(len(c)):
        if c[i] != ' ':
            print(alfabet[vig_decrypt(c[i], k[i%len(k)])], end='')

if __name__ == "__main__":
    print("Oppg 5 a)")
    vig_encrypt_text("snart helg", "torsk")

    print("\n\nOppg 5 b)")
    vig_decrypt_text("QZQOBVCAFFKSDC", "BRUS")
    print("\nDen dekrypterte teksten er: Pizza eller taco")

    print("\n\nOppg5 c)")
    print("Et ord på 15 bokstaver og det norske alfabetet gir 29^15 mulige kombinasjoner")
    keys = 29**15
    print("Altså {:,} muligheter".format(keys).replace(",", " "))
    print("Dette bør regnes som rimelig sikkert mot brute force på vanlig \"lineær\" maskin")