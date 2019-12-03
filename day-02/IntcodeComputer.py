#! /usr/bin/python3

def parseInput(data: str) -> list:
    return [int(i) for i in data.split(",")]

class StateError(Exception):
    """Exception raised if invalid opcode is reached or if the intcode computer is run from a halted state"""
    def __init__(self, value):
        self.expression = "Recieved opcode " + str(value)
        self.message = "Invalid opcode!"
        

class IntcodeComputer:
    memory: list
    position: int
    state: bool
    
    def __init__(self, memory: list):
        self.memory = memory.copy()
        self.position = 0
        self.state = True
    
    def iterate(self):
        """Executes one step of the intcode computer."""
        if not self.state:
            raise StateError("Halted")
        opcode: int = self.memory[self.position]
        if not (opcode == 1 or opcode == 2 or opcode == 99):
            raise StateError(opcode)
        if opcode == 1:
            operand1 = self.memory[self.memory[self.position + 1]]
            operand2 = self.memory[self.memory[self.position + 2]]
            self.memory[self.memory[self.position + 3]] = operand1 + operand2
            self.position += 4
            self.state = True
        if opcode == 2:
            operand1 = self.memory[self.memory[self.position + 1]]
            operand2 = self.memory[self.memory[self.position + 2]]
            self.memory[self.memory[self.position + 3]] = operand1 * operand2
            self.position += 4
            self.state = True
        if opcode == 99:
            self.state = False
    
    def setValue(self, position: int, value: int):
        self.memory[position] = value
    
    def getValue(self, position: int) -> int:
        return self.memory[position]
        
    def getState(self) -> bool:
        return self.state
        
if __name__ == "__main__":
    with open("./day02", 'r') as f:
        data = parseInput(f.read())
    computer = IntcodeComputer(data)
    
    computer.setValue(1, 12)
    computer.setValue(2, 2)
    
    while computer.getState():
        computer.iterate()
        
    print("Value at position 0: ", computer.getValue(0))
