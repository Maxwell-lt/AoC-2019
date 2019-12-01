#! /usr/bin/python3

from FuelCounterUpper import getFuel

def getFuelRecursive(total: int, last: int) -> int:
    new = getFuel(last)
    if new > 0:
        return getFuelRecursive(total + new, new)
    else:
        return total

if __name__ == "__main__":
    total: int = 0
    with open("./day01-1", 'r') as f:
        for line in f:
            total = total + getFuelRecursive(0, int(line))
    print("Total fuel: ", total)
