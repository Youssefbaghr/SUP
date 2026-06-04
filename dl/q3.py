def prefixe(M, S):

    if len(M) > len(S):
        return False
    
    return S[:len(M)] == M

# TEST
print(prefixe("abc", "abcdef"))  # True
print(prefixe("abc", "ab"))  # False