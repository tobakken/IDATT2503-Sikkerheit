
def order_of_element(x, z):
    for i in range(1,z):
        if(x**i) % z == 1:
            return i



def elements_of_z(z):
    for i in range(1, z):
        print(f"Order of element {i} in Z_{z} is {order_of_element(i, z)}")


def find_discrete_logarithm(alpha, beta, z):
    for i in range(z):
        if (alpha ** i) % z == beta:
            return i
    return None


def dl_log_table():
    print("{:<26}{:<4}".format("", "beta"))
    print("{:<12}".format(""), end="")
    b_range = range(1, 11)
    for i in b_range:
        print(i, end="   ")
    print("")
    print("{:<10}----------------------------------------".format(""))
    for a in range(2, 11):
        print("{:<7}{:<2}|  ".format("" if a != 5 else "alpha", a), end="")
        for b in b_range:
            print(ans if (ans := find_discrete_logarithm(a, b, 11)) is not None else "x", end="   ")
        print("")


if __name__ == '__main__':
    print("Task 1:")
    elements_of_z(11)
    print("\n\nTask 2:\n")
    dl_log_table()
