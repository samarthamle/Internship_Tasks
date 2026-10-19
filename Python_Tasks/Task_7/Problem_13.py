

def isValid(s):
    from collections import Counter

    freq = Counter(s)
    count = Counter(freq.values())

    if len(count) == 1:
        return "YES"

    if len(count) == 2:
        first, second = count.items()

        if first[1] == 1 and (first[0] == 1 or first[0] - second[0] == 1):
            return "YES"

        if second[1] == 1 and (second[0] == 1 or second[0] - first[0] == 1):
            return "YES"

    return "NO"