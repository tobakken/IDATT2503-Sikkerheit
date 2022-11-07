def hmac(k,m, opad, ipad):
    k_opad = "{:04b}".format(k^opad)
    k_ipad = "{:04b}".format(k^ipad)
    concat = k_opad + midtkvadrat(int(k_ipad + m, 2))
    print(midtkvadrat(int(concat, 2)))
    

def midtkvadrat(x):
    return "{:08b}".format((x**2)%(2**8))[2:6]

if __name__ == "__main__":
    print("Oppgave 1 a)")
    print("Finne HMAC til meldingen '0110'\nResultat:")
    hmac(int('1001', 2), '0110', int('0101', 2), int('0011', 2))
    print("\n\nOppgave 1 b)")
    print("Melding '0111' og HMAC: '0100', stemmer dette?\nFår HMAC:")
    hmac(int('1001', 2), '0111', int('0101', 2), int('0011', 2))
    print("Dette stemmer med HMAC som ble oppgitt, Ingen grunn til å tro at den ikke er autentisk")