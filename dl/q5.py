def distanceH(S1, S2):
    distance = 0
    for i in range(len(S1)):
        if S1[i] != S2[i]:
            distance += 1
    return distance

#TEST 
print(distanceH("AGCT", "AGGT"))  # Output: 1
print(distanceH("AAAA", "TTTT"))  # Output: 4


def distanceH_langage(langage):
    min_distance = float('inf')
    for i in range(len(langage)):
        for j in range(i + 1, len(langage)):
            distance = distanceH(langage[i], langage[j])
            min_distance = min(min_distance, distance)
    return min_distance

# TEST
print(distanceH_langage(["aabb", "xayy", "tghy", "xgyy"]))  # Output: 1