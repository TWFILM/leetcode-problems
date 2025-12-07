import math
def countOdds(low: int, high: int) -> int:
    n = low % 2 != 0
    if high % 2 != 0:
        n += math.ceil((high - low) / 2)
    else:
        n += (high - low) // 2
    return int(n)

low, high = 3, 7
print(countOdds(low, high))

low, high = 8, 10
print(countOdds(low, high))

