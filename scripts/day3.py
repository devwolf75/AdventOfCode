'''
--- Day 3: Perfectly Spherical Houses in a Vacuum ---

Santa is delivering presents to an infinite two-dimensional grid of houses.

He begins by delivering a present to the house at his starting location, and then an elf at the North Pole calls him via radio and tells him where to move next. Moves are always exactly one house to the north (^), south (v), east (>), or west (<). After each move, he delivers another present to the house at his new location.

However, the elf back at the north pole has had a little too much eggnog, and so his directions are a little off, and Santa ends up visiting some houses more than once. How many houses receive at least one present?

For example:

> delivers presents to 2 houses: one at the starting location, and one to the east.
^>v< delivers presents to 4 houses in a square, including twice to the house at his starting/ending location.
^v^v^v^v^v delivers a bunch of presents to some very lucky children at only 2 houses.

--- Part Two ---

The next year, to speed up the process, Santa creates a robot version of himself, Robo-Santa, to deliver presents with him.

Santa and Robo-Santa start at the same location (delivering two presents to the same starting house), then take turns moving based on instructions from the elf, who is eggnoggedly reading from the same script as the previous year.

This year, how many houses receive at least one present?

For example:

^v delivers presents to 3 houses, because Santa goes north, and then Robo-Santa goes south.
^>v< now delivers presents to 3 houses, and Santa and Robo-Santa end up back where they started.
^v^v^v^v^v now delivers presents to 11 houses, with Santa going one direction and Robo-Santa going the other.
'''

from sys import argv
#OPEN THE FILE
script, file = argv
text = open(file)
puzzle = list(text.read())
#PART ONE
x = y = houses = 0
grid = {}
for direction in puzzle:
    if not x in grid:
        grid[x] = {}
    if not y in grid[x]:
        grid[x][y] = 1
        houses +=1
    if(direction == '>'):
        x+=1
    elif(direction == '^'):
        y+=1
    elif(direction == '<'):
        x-=1
    elif(direction == 'v'):
        y-=1
print(houses)
#PART TWO
s_x = s_y = r_x = r_y = houses = 0
grid = {}
robot_turn = False
for direction in puzzle:
    if not robot_turn:
        if not s_x in grid:
            grid[s_x] = {}
        if not s_y in grid[s_x]:
            grid[s_x][s_y] = 1
            houses += 1
        if(direction == '>'):
            s_x+=1
        elif(direction == '^'):
            s_y+=1
        elif(direction == '<'):
            s_x-=1
        elif(direction == 'v'):
            s_y-=1
        robot_turn = True
    else:
        if not r_x in grid:
            grid[r_x] = {}
        if not r_y in grid[r_x]:
            grid[r_x][r_y] = 1
            houses += 1
        if(direction == '>'):
            r_x+=1
        elif(direction == '^'):
            r_y+=1
        elif(direction == '<'):
            r_x-=1
        elif(direction == 'v'):
            r_y-=1
        robot_turn = False
print(houses)
