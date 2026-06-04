def f1(s):
    d = {}
    for i, c in enumerate(s):
        if c not in d:
            d[c] = i
    return d

print(f1("majestueux"))


def f2(s):
    return {f"{c}{i}": i for i, c in enumerate(s)}

print(f2("majestueux"))