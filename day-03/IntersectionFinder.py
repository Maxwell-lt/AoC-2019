#! /usr/bin/python3

def parseWire(wire: str) -> set:
    """Accepts CSV formatted wire
    Outputs set of points crossed by wire."""
    data = wire.split(',')
    position = [0, 0]
    points = set()
    for line in data:
        if line[0] == "R":
            for i in range(position[0], position[0] + int(line[1:])):
                points.add((i, position[1]))
            position[0] += int(line[1:])
        elif line[0] == "L":
            for i in range(position[0], position[0] - int(line[1:])):
                points.add((i, position[1]))
            position[0] -= int(line[1:])
        elif line[0] == "U":
            for i in range(position[1], position[1] + int(line[1:])):
                points.add((position[0], i))
            position[1] += int(line[1:])
        elif line[0] == "D":
            for i in range(position[1], position[1] - int(line[1:])):
                points.add((position[0], i))
            position[1] -= int(line[1:])

    points.add((position[0], position[1]))
    return points

def findIntersections(wireA: set, wireB: set) -> set:
    return wireA.intersection(wireB)

def findDistanceTaxicab(crosses: set) -> int:
    distance: list = []
    for cross in crosses:
        distance.append(abs(cross[0]) + abs(cross[1]))
    return(min(distance))

if __name__ == "__main__":
    with open("./day03", 'r') as f:
        wire1 = f.readline()
        wire2 = f.readline()
    print("Minimum distance from an intersection to the origin: ",
    	    findDistanceTaxicab(findIntersections(parseWire(wire1), parseWire(wire2))))
