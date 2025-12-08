def countTruoles(n: int) -> int:
    count = 0
    s = set([i**2 for i in range(1, n+1)])

    for x in range(3, n+1):
        for y in range(x, n+1):
            if x**2 + y**2 in s:
                count += 2

    return count

n = 5
# Output: 2
# The triples are (3, 4, 5), (4, 3, 5).
print(countTruoles(n))

n = 10
# Output: 4
# The triples are (3, 4, 5), (4, 3, 5), (6, 8, 10), (8, 6, 10).
print(countTruoles(n))
