
def part1():
    hor = 0
    depth = 0
    with open('a.txt') as f:
        lines = f.read().splitlines()
    for line in lines:
        line = line.split(" ")
        if line[0] == "forward":
            print("ree")
            hor += int(line[1])
        if line[0] == "up":
            
            depth -=  int(line[1])
            print(depth)
        if line[0] == "down":
            depth +=  int(line[1])
    print(hor, depth)
    print(hor*depth)
        


def part2():
    hor = 0
    depth = 0
    aim = 0
    with open('b.txt') as f:
        lines = f.read().splitlines()
    for line in lines:
        line = line.split(" ")
        if line[0] == "forward":
            print("ree")
            hor += int(line[1])
            depth += aim*int(line[1])
        if line[0] == "up":
            
            aim -=  int(line[1])
            print(depth)
        if line[0] == "down":
            aim +=  int(line[1])
    print(hor, depth)
    print(hor*depth)

if __name__ == '__main__':
    #part1()
    part2()