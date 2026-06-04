def premier(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def main():
    primes = []
    n = 2
    while len(primes) < 100:
        if premier(n):
            primes.append(n)
        n += 1
    print(' '.join(map(str, primes)))

if __name__ == "__main__":
    main()