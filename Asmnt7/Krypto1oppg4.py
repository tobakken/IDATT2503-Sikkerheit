ALFABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZÆØÅ"
alfabet = "abcdefghijklmnopqrstuvwxyzæøå"

def decrypt(m, k):
    return (m-k)%29

def decrypt_string(c, k):
        for i in range(len(c)):
            if c[i] != " ":
                print(alfabet[decrypt(ALFABET.index(c[i]), k)], end='')

def decrypt_brute_force(c, n):
    for i in range(n):
        print(str(i) + ": ", end='')
        for j in range(len(c)):
            if c[j] != " ":
                print(alfabet[decrypt(ALFABET.index(c[j]), i)], end='')
        print()


if __name__ == "__main__":
    print("Dekrypterer...")
    c = "YÆVFB VBVFR ÅVBV"
    decrypt_brute_force(c, 28)
    decrypt_string(c, 17)
    print("\nRiktig nøkkel er 17, det gir svaret: Hjernen er alene")
