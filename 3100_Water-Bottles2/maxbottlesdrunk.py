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

if __name__ == "__main__":
    print(maxBottlesDrunk(13, 6)) # output: 15
    print(maxBottlesDrunk(10, 3)) # output: 13
    print(maxBottlesDrunk(3, 1))  # output: 5