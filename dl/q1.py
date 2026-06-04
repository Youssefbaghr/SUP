def est_bien_parenthesee(s):
    if s == "":
        return True
    
    if s[0] == '(' and s[-1] == ')':
        inner = s[1:-1]
        if est_bien_parenthesee(inner):
            return True
    
    for i in range(1, len(s)):
        w1 = s[:i]
        w2 = s[i:]
        if est_bien_parenthesee(w1) and est_bien_parenthesee(w2):
            return True
    
    return False


# TEST

print(est_bien_parenthesee("()"))  # True
print(est_bien_parenthesee("(())"))  # True 
print(est_bien_parenthesee("(()())"))  # True
print(est_bien_parenthesee("(()"))  # False 
print(est_bien_parenthesee("(())()()()()()()(9()"))  # False 
