def maxBottlesDrunk(numBottles: int, numExchange: int) -> int:
    full_bottles = numBottles
    empty_bottles, bottles_drunk = 0, 0
    while full_bottles > 0:
        bottles_drunk += full_bottles
        empty_bottles += full_bottles
        full_bottles = 0
        # print(f"Bottles Drunk: {bottles_drunk}, Empty Bottles: {empty_bottles}, Full Bottles: {full_bottles}, Num Exchange: {numExchange}")

        while empty_bottles >= numExchange:
            exchange = 1
            full_bottles += exchange
            empty_bottles -= numExchange
            numExchange += 1
            # print(f"Exchange: {exchange}, Full Bottles: {full_bottles}, Empty Bottles: {empty_bottles}, Num Exchange: {numExchange}")

    return bottles_drunk


numBottles = 13
numExchange = 6
print(maxBottlesDrunk(numBottles, numExchange))

numBottles = 10
numExchange = 3
print(maxBottlesDrunk(numBottles, numExchange))
