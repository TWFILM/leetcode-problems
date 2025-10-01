def numWaterBottles(numBottles: int, numExchange: int) -> int:
    totol_drunk = numBottles
    empty_bottles = numBottles

    while empty_bottles >= numExchange:
        new_bottles = empty_bottles // numExchange
        totol_drunk += new_bottles
        empty_bottles = empty_bottles % numExchange + new_bottles
    
    return totol_drunk

if __name__ == "__main__":
    print(numWaterBottles(9, 3))  # Output: 13
    print(numWaterBottles(15, 4))  # Output: 19
    print(numWaterBottles(5, 5))  # Output: 6
    print(numWaterBottles(2, 3))  # Output: 2