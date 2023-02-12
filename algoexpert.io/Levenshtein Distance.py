"""
https://www.algoexpert.io/questions/levenshtein-distance
Levenshtein Distance
"""


def levenshteinDistance(str1, str2):
    d = [] * len(str1)
    for i in range(len(str1) + 1):
        d.append([0 for _ in range(len(str2) + 1)])

    for oneindex in range(len(str1) + 1):
        for twoindex in range(len(str2) + 1):
            if oneindex == 0:
                comp1 = ' '
            else:
                comp1 = str1[oneindex - 1]
            if twoindex == 0:
                comp2 = ' '
            else:
                comp2 = str2[twoindex - 1]

            if comp1 != comp2:
                v = d[oneindex]  # v for variable
                if v != str2[twoindex - 1]:
                    if v[twoindex - 1] == 0:
                        v[twoindex] = 1
                    else:
                        v[twoindex] = v[twoindex - 1] + 1
            else:  # then i don't need to operate anything.
                d[oneindex][twoindex] = d[oneindex][twoindex - 1]

    ...


assert levenshteinDistance("gumbo", "gambol") == 1
assert levenshteinDistance('abc', 'yabd') == 2
assert levenshteinDistance('', 'abc') == 3
assert levenshteinDistance("biting", "mitten") == 4
levenshteinDistance("abcdefghij", "a234567890")
