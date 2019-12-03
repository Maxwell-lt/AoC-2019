#! /usr/bin/python3

from IntcodeComputer import *

def modifyInput(computer: IntcodeComputer, noun: int, verb: int) -> IntcodeComputer:
    computer.setValue(1, noun)
    computer.setValue(2, verb)
    return computer

def getOutputValue(data: list, noun: int, verb: int) -> int:
    computer = IntcodeComputer(data)
    modifyInput(computer, noun, verb)
    while computer.getState():
        computer.iterate()
    return computer.getValue(0)

def tryValues(data: list, target: int) -> int:
    for i in range(0, len(data)):
        for j in range(0, len(data)):
            try:
                if getOutputValue(data, i, j) == target:
                    return 100 * i + j
            except:
                print()
    return 0 # No valid noun/verb
    
if __name__ == "__main__":
    with open("./day02", 'r') as f:
        data = parseInput(f.read())
    OUTPUT = 19690720
    inputValue = tryValues(data, OUTPUT)
    print("Correct input is: ", inputValue)                
