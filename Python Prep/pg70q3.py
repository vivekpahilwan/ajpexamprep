def count_upper_lower(s):
    uc = 0
    lc = 0
    for c in s:
        if c.isupper():
            uc += 1
        elif c.islower():
            lc += 1
    return (uc, lc)
