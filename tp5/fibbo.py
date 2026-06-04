import sys

def fib(n: int) -> int:
    if n < 0:
        raise ValueError("n doit être >= 0")
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)

def fib_sequence(n: int):
    if n < 0:
        raise ValueError("n doit être >= 0")
    if n == 0:
        return [0]
    if n == 1:
        return [0, 1]
    seq = fib_sequence(n - 1)
    seq.append(seq[-1] + seq[-2])
    return seq

if __name__ == "__main__":
    try:
        n = int(sys.argv[1]) if len(sys.argv) > 1 else 10
    except ValueError:
        print("Argument invalide : fournir un entier >= 0")
        sys.exit(1)

    if n < 0:
        print("n doit être >= 0")
        sys.exit(1)

    seq = fib_sequence(n)
    print(seq)
    print(f"Fibonacci({n}) = {seq[-1]}")