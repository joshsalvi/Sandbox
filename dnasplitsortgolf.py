import itertools


def golf(s, n):
    a = [s[p * n:(p + 1) * n] for p in range(len(s) // n)]
    return "".join(sorted(a, key=lambda s: sum(1 for p, q in itertools.combinations(s, 2) if p > q)))


print golf("ACGGCATAACCCTCGA", 3)
