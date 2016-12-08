instructions = """rect 1x1
rotate row y=0 by 20
rect 1x1
rotate row y=0 by 2
rect 1x1
rotate row y=0 by 3
rect 2x1
rotate row y=0 by 2
rect 1x1
rotate row y=0 by 3
rect 2x1
rotate row y=0 by 2
rect 1x1
rotate row y=0 by 4
rect 2x1
rotate row y=0 by 2
rect 1x1
rotate row y=0 by 2
rect 1x1
rotate row y=0 by 2
rect 1x1
rotate row y=0 by 3
rect 2x1
rotate row y=0 by 2
rect 1x1
rotate row y=0 by 5
rect 1x1
rotate row y=0 by 2
rect 1x1
rotate row y=0 by 6
rect 5x1
rotate row y=0 by 2
rect 1x3
rotate row y=2 by 8
rotate row y=0 by 8
rotate column x=0 by 1
rect 7x1
rotate row y=2 by 24
rotate row y=0 by 20
rotate column x=5 by 1
rotate column x=4 by 2
rotate column x=2 by 2
rotate column x=0 by 1
rect 7x1
rotate column x=34 by 2
rotate column x=22 by 1
rotate column x=15 by 1
rotate row y=2 by 18
rotate row y=0 by 12
rotate column x=8 by 2
rotate column x=7 by 1
rotate column x=5 by 2
rotate column x=2 by 1
rotate column x=0 by 1
rect 9x1
rotate row y=3 by 28
rotate row y=1 by 28
rotate row y=0 by 20
rotate column x=18 by 1
rotate column x=15 by 1
rotate column x=14 by 1
rotate column x=13 by 1
rotate column x=12 by 2
rotate column x=10 by 3
rotate column x=8 by 1
rotate column x=7 by 2
rotate column x=6 by 1
rotate column x=5 by 1
rotate column x=3 by 1
rotate column x=2 by 2
rotate column x=0 by 1
rect 19x1
rotate column x=34 by 2
rotate column x=24 by 1
rotate column x=23 by 1
rotate column x=14 by 1
rotate column x=9 by 2
rotate column x=4 by 2
rotate row y=3 by 5
rotate row y=2 by 3
rotate row y=1 by 7
rotate row y=0 by 5
rotate column x=0 by 2
rect 3x2
rotate column x=16 by 2
rotate row y=3 by 27
rotate row y=2 by 5
rotate row y=0 by 20
rotate column x=8 by 2
rotate column x=7 by 1
rotate column x=5 by 1
rotate column x=3 by 3
rotate column x=2 by 1
rotate column x=1 by 2
rotate column x=0 by 1
rect 9x1
rotate row y=4 by 42
rotate row y=3 by 40
rotate row y=1 by 30
rotate row y=0 by 40
rotate column x=37 by 2
rotate column x=36 by 3
rotate column x=35 by 1
rotate column x=33 by 1
rotate column x=32 by 1
rotate column x=31 by 3
rotate column x=30 by 1
rotate column x=28 by 1
rotate column x=27 by 1
rotate column x=25 by 1
rotate column x=23 by 3
rotate column x=22 by 1
rotate column x=21 by 1
rotate column x=20 by 1
rotate column x=18 by 1
rotate column x=17 by 1
rotate column x=16 by 3
rotate column x=15 by 1
rotate column x=13 by 1
rotate column x=12 by 1
rotate column x=11 by 2
rotate column x=10 by 1
rotate column x=8 by 1
rotate column x=7 by 2
rotate column x=5 by 1
rotate column x=3 by 3
rotate column x=2 by 1
rotate column x=1 by 1
rotate column x=0 by 1
rect 39x1
rotate column x=44 by 2
rotate column x=42 by 2
rotate column x=35 by 5
rotate column x=34 by 2
rotate column x=32 by 2
rotate column x=29 by 2
rotate column x=25 by 5
rotate column x=24 by 2
rotate column x=19 by 2
rotate column x=15 by 4
rotate column x=14 by 2
rotate column x=12 by 3
rotate column x=9 by 2
rotate column x=5 by 5
rotate column x=4 by 2
rotate row y=5 by 5
rotate row y=4 by 38
rotate row y=3 by 10
rotate row y=2 by 46
rotate row y=1 by 10
rotate column x=48 by 4
rotate column x=47 by 3
rotate column x=46 by 3
rotate column x=45 by 1
rotate column x=43 by 1
rotate column x=37 by 5
rotate column x=36 by 5
rotate column x=35 by 4
rotate column x=33 by 1
rotate column x=32 by 5
rotate column x=31 by 5
rotate column x=28 by 5
rotate column x=27 by 5
rotate column x=26 by 3
rotate column x=25 by 4
rotate column x=23 by 1
rotate column x=17 by 5
rotate column x=16 by 5
rotate column x=13 by 1
rotate column x=12 by 5
rotate column x=11 by 5
rotate column x=3 by 1
rotate column x=0 by 1
""".splitlines()

screen =[['.' for _ in range(50)] for _ in range(6)]
def transpose(l):
    return  [list(x) for x in zip(*l)]

def rect(screen, a, b):
    for i in range(a):
        for j in range(b):
            screen[j][i] ='#'
    return screen

def show(screen):
    print("\n".join("".join(x) for x in screen))

def rotate_row(screen, a, b):
    screen[a] = screen[a][-b:] + screen[a][:-b]
    return screen

def rotate_column(screen, a, b):
    return transpose(rotate_row(transpose(screen),a,b))

for instruction in instructions:
    if instruction.startswith("rect"):
        coordinates = [int(coordinate) for coordinate in instruction[5:].split('x')]
        screen =rect(screen,coordinates[0], coordinates[1])
    elif instruction.startswith("rotate row"):
        data = [int(coordinate) for coordinate in instruction[13:].split(' by ')]
        screen =rotate_row(screen,data[0], data[1])
    elif instruction.startswith("rotate column"):
        data = [int(coordinate) for coordinate in instruction[16:].split(' by ')]
        screen =rotate_column(screen,data[0], data[1])
show(screen)
print(sum(1 for x in screen for y in x if y=='#'))        
