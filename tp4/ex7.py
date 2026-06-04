import math

def plus_petit(n: int) -> int:
    
    if n <= 2:
        raise ValueError("n doit être strictement supérieur à 2")
    if n % 2 == 0:
        return 2
    limit = math.isqrt(n)
    i = 3
    while i <= limit:
        if n % i == 0:
            return i
        i += 2
    return n

if __name__ == "__main__":
    print(plus_petit(5001))  
