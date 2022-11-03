alfabet = " abcdefghijklmnopqrstuvwxyzæøå,."

def cbc_mac(m):
    IV = 0b0
    prev_c = (m[0]^IV)
    for i in range(1, len(m)):
        c = (m[i]^prev_c)
        prev_c = caesar(c)
    print("{:04b}".format(prev_c))

def caesar(c):
    return (c + 3)%2**4

if __name__ == "__main__":
    print("x")
    cbc_mac([0b1101, 0b1111, 0b1010, 0b0001])
    print("x\'")
    cbc_mac([0b0010, 0b1100, 0b0001, 0b1111])