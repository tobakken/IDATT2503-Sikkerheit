import array as arr
alfabet = "abcdefghijklmnopqrstuvwxyzæøå"

def encrypt_autokey(k, m):
    keystream = create_keystream(k, m)
    print("Nøkkelstrøm: " + keystream)
    res =''
    for i in range(len(m)):
        res += alfabet[(alfabet.index(m[i])+alfabet.index(keystream[i]))%29]
    print(res)

def create_keystream(k,m):
    keystream = k
    for i in range(1, len(m)):
        keystream += m[i-1]
    return keystream

def decrypt_autokey(k, e):
    key = k
    res = ''
    for i in range(len(e)):
        res += alfabet[(e[i]-alfabet.index(key))%29]
        key = res[i]
    print(res)
    
if __name__ == "__main__":
    print("Oppgave 3 a) \nKrypter teksten 'goddag' med autokey")
    encrypt_autokey(alfabet[17], "goddag")

    print("\n\nOppgave 3 b) \nDekrypter  '23 08 23 12 21 02 04 03 17 13 19' med autokey\nResultat:")
    decrypt_autokey(alfabet[5], arr.array('i',[23, 8, 23, 12, 21, 2, 4, 3, 17, 13, 19]))

