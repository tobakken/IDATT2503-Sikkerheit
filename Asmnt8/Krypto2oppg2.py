alfabet = " abcdefghijklmnopqrstuvwxyzæøå,."

def crypt_cbc(m, k):
    IV = 13
    character = (alfabet.index(m[0])^IV)
    res = alfabet[(character+k)%32]
    for i in range(1, len(m)):
        character = (alfabet.index(m[i])^alfabet.index(res[i-1]))
        res += alfabet[(character+k)%32]
    print(res)


def decrypt_cbc(e, k):
    IV = 13
    dec_key = (alfabet.index(e[0])-k)%32
    res = alfabet[dec_key^IV]
    for i in range(1, len(e)):
        dec_key = (alfabet.index(e[i])-k)%32
        res+=alfabet[dec_key^alfabet.index(e[i-1])]
    print(res)

if __name__ == "__main__":
    print("Oppgave 2 a) \nKrypter teksten 'aaaaa'\nResultatet blir:")
    crypt_cbc("aaaaa", 3)

    print("\n\nOppgave 2 b) \nDekrypter teksten 'qvxæyy hkgdgk,,oqhdnc'\nResultatet blir:")
    decrypt_cbc("qvxæyy hkgdgk,,oqhdnc", 3)
