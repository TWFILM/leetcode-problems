def numWaterBottles(numBottles: int, numExchange: int) -> int:
    totol_drunk = numBottles
    empty_bottles = numBottles

    while empty_bottles >= numExchange:
        new_bottles = empty_bottles // numExchange
        totol_drunk += new_bottles
        empty_bottles = empty_bottles % numExchange + new_bottles

    return totol_drunk


numBottles = 9
numExchange = 3
print(numWaterBottles(numBottles, numExchange))

numBottles = 15
numExchange = 4
print(numWaterBottles(numBottles, numExchange))
