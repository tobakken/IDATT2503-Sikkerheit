def rsa_encrypt(m, k):
    return (m**k[0])%k[1]

def rsa_decrypt(e, k):
    return (e**k[0])%k[1]

def chosen_msg_attack(sign1, sign2, n):
    return (sign1[0]*sign2[0])%n, (sign1[1]*sign2[1])%n

def validate_msg(x, y, k):
    print("valid") if x == rsa_decrypt(y, k) else print("not valid")

if __name__ == "__main__":
    bob_pub = [13, 437]
    bob_priv = [61, 437]
    alice_pub = [283, 731]
    alice_priv = [19, 731]
    validate_msg(78, 394, bob_pub)
    validate_msg(97, 337, bob_pub)
    print("Begge meldingene blir validert til en korrekt signatur, dermed er de mest sannsynlig sendt fra Bob")
    print("\n\ndel 3: kjent-melding-angrep")
    valid_message = chosen_msg_attack([38,171], [123,289], 437)
    validate_msg(valid_message[0], valid_message[1], bob_pub)

    print("\n\nDel 4: kryptere og signere meldingen 109")
    sign_alice = rsa_decrypt(109, alice_priv)
    crypt_bob = [rsa_encrypt(109, bob_pub), rsa_encrypt(sign_alice, bob_pub)]
    print(crypt_bob)
    decrypt_bob = [rsa_decrypt(crypt_bob[0], bob_priv), rsa_decrypt(crypt_bob[1], bob_priv)]
    print(decrypt_bob)
    validate_msg(decrypt_bob[0], decrypt_bob[1], alice_pub)

