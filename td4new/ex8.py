def decompose_facteur_premier(n: int) -> list[int]:
    if n < 2:
        return []
    def rec(n: int, div: int = 2) -> list[int]:
        if n == 1:
            return []
        if div * div > n:  
            return [n]
        if n % div == 0:
            return [div] + rec(n // div, div)
        return rec(n, div + 1)
    return rec(n)

print(decompose_facteur_premier(9)  )