
import sys

sys.setrecursionlimit(3000)

def est_pair(n: int) -> bool:
    n = abs(int(n))
    if n == 0:
        return True
    return est_impair(n - 1)

def est_impair(n: int) -> bool:
    n = abs(int(n))
    if n == 0:
        return False
    return est_pair(n - 1)

if __name__ == "__main__":
    tests = [0, 1, 2, 3, 10, -1, -4, 999]
    for t in tests:
        print(f"{t}: pair? {est_pair(t)}, impair? {est_impair(t)}")