def exp_approx(x, n):
    if n > 10: 
        return 0
    
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    
    return (x ** n) / factorial + exp_approx(x, n + 1)


print(exp_approx(1, 10)) 