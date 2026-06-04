def PGCD_ITER(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def PGCD_REC(a, b):
    if b == 0:
        return a
    return PGCD_REC(b, a % b)


if __name__ == "__main__":
    print(PGCD_ITER(48, 18))   # Output: 6
    print(PGCD_REC(48, 18))   # Output: 6