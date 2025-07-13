# filename: permutation_corrected.py
import math
from collections import Counter

def count_permutations(word):
    """Counts the number of distinct permutations of a word."""
    char_counts = Counter(word.lower())
    n = len(word)
    numerator = math.factorial(n)
    denominator = 1
    for count in char_counts.values():
        denominator *= math.factorial(count)
    return numerator // denominator

word = "ALGEbRA"
result = count_permutations(word)
print(result)
