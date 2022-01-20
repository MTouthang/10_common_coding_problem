# An anagram of a string is another string that contains the same characters,
# only the order of characters can be different.
# Example s1 = 'garden' s2 = 'danger', the two string are Anagram

from collections import Counter;


def valid_anagram(s1, s2):
    if len(s1) != len(s2):
        return False
    return sorted(s1) == sorted(s2)

    # return Counter(s1) == Counter(s2)


result = valid_anagram(s1="garden", s2='danger')
print("The two word anagram?:", result)
