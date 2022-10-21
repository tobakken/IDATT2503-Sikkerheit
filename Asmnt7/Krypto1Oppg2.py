def print_mult_mod(n):
    for i in range(n):
        print(str(i+1).zfill(2), end=' ')
        for j in range(n):
            print(str(((i+1)*(j+1))%n).zfill(2), end=' ')
        print()

def find_mult_inverse(n):
    for i in range(n):
        for j in range(n):
            if ((i+1)*(j+1)%n == 1): print(str(i+1) + " mod " + str(n) + " har multiplikativ invers: " + str(j+1))


def brute_force_mult_invers(a, n):
    for i in range(n):
        if a*(i+1)%n == 1: print(str(a) + " mod " + str(n) + " har multiplikativ invers: " + str(i+1))

if __name__ == "__main__":
    print("Oppgave 2 a)")
    print_mult_mod(12)

    print("\n\nOppgave 2 b)")
    find_mult_inverse(12)

    print("\n\nOppgave 2 c)")
    print_mult_mod(11)
    find_mult_inverse(11)
    print("11 er et primtall så alle tall opp til 11 har multiplikativ invers")

    print("\n\nOppgave 2 d)")
    brute_force_mult_invers(11, 29)

    print("\n\nOppgave 2 e)")
    print("Tallet a har multiplikativ invers mod n dersom det ikke har felles faktorer med n. Eksempel 9 = 3*3 og 12 = 3*4," + 
    "dermed har ikke 9 multiplikativ invers mod 12")