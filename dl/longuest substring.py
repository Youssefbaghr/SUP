#2 chaine , la plus longue sous chaine communes entre les deux chaine

def longest_common_substring(s1, s2):
    m = len(s1)
    n = len(s2)
    longest = 0
    end_index_s1 = 0
    
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] > longest:
                    longest = dp[i][j]
                    end_index_s1 = i
    
    return s1[end_index_s1 - longest:end_index_s1]  

def longest_common_substring_v2(s1, s2):
    max_sub = ""
    for i in range(len(s1)):
        for j in range(i + 1, len(s1) + 1):
            sub = s1[i:j]
            if sub in s2 and len(sub) > len(max_sub):
                max_sub = sub
    return max_sub


# Exemples
print(longest_common_substring("z3abcde", "z3abcdfce"))  # "z3abcd"
print(longest_common_substring("abcdef", "zabcf"))  # "abc"
print(longest_common_substring("xyz", "abc"))      # ""


print(longest_common_substring_v2("z3abcde", "z3abcdfce"))  # "z3abcd"
print(longest_common_substring_v2("abcdef", "zabcf"))  # "abc"
print(longest_common_substring_v2("xyz", "abc"))      # ""