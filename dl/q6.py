# 6.a - Check if a string is a valid DNA strand
def estADN(s):
    valid_chars = {'A', 'C', 'G', 'T'}
    return all(c in valid_chars for c in s) and len(s) > 0

#test 
print(estADN("ACGT"))  # True

# 6.b - Calculate molar mass of a DNA sequence
def masseMolaire(adn):
    masses = {'A': 135, 'T': 126, 'G': 151, 'C': 111}
    return sum(masses[base] for base in adn if base in masses)


# 6.c - Get complementary DNA strand
def brinComp(adn):
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return ''.join(complement[base] for base in adn)


# 6.d - Check if first strand is a subsequence of the second
def sousSequence(brin1, brin2):
    return brin1 in brin2