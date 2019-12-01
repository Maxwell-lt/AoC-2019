#! /usr/bin/python3

def getFuel(moduleMass: int) -> int:
    return int(moduleMass/3) - 2

if __name__ == "__main__":
    total: int = 0
    with open("./day01-1", 'r') as f:
        for line in f:
            total = total + getFuel(int(line))
    print("Total fuel: ", total)
