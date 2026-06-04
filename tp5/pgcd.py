
def pgcd(a: int, b: int) -> int:
    a, b = abs(a), abs(b)
    if b == 0:
        return a
    return pgcd(b, a % b)


if __name__ == "__main__":
        result = pgcd(-27,36)
        print(f"pgcd({-27}, {36}) = {result} (expected {9})")
