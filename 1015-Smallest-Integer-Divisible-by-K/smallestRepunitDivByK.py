def smallestRepunitDivByK(k: int) -> int:
    if (k % 2 == 0 or k % 5 == 0): return -1

    n = 1
    c = 1
    while n % k != 0:
        if (n % k == (n*10+1) % k): 
            return -1

        n = n*10 + 1
        c+=1

    return c

k = 1
print(smallestRepunitDivByK(k))

k = 2
print(smallestRepunitDivByK(k))

k = 3
print(smallestRepunitDivByK(k))
