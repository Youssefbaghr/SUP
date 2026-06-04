
def facto(n:int):
    if n == 0 :
        return(1)
    else :
        return (n*facto(n-1))
        
print(facto(700))
