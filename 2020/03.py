from os.path import dirname, join
file_name = "./03.txt"
current_dir = dirname(__file__)
file_path = join(current_dir, file_name)

f = open(file_path, "r")
map = [str(i).strip() for i in f.readlines()]

max_x = len(map[0]) - 1
max_y = len(map) - 1
trees = 0
x_position = 0
y_position = 0

while y_position <= max_y:
    if x_position + 3 >= max_x:
        x_position = 0 + ((x_position + 3) - max_x)
    else:
        x_position = x_position + 3

    y_position = y_position + 1
    print(map[y_position][x_position])
    if map[y_position][x_position] == "#":
        trees = trees + 1

# with open(file_path, 'r') as f:

#     # X positions, iterator
#     x_1 = 0
#     x_3 = 0
#     x_5 = 0
#     x_7 = 0
#     x_1_2 = 0
#     i = 0

#     # Tree counts
#     trees_1 = 0
#     trees_3 = 0
#     trees_5 = 0
#     trees_7 = 0
#     trees_1_2 = 0

#     for line in f:
#         # Check for trees
#         if line[x_1] == '#':
#             trees_1 += 1
#         if line[x_3] == '#':
#             trees_3 += 1
#         if line[x_5] == '#':
#             trees_5 += 1
#         if line[x_7] == '#':
#             trees_7 += 1
#         if i % 2 == 0 and line[x_1_2] == '#':
#             trees_1_2 += 1

#         # Adjust x movement with wraparound
#         x_1 = (x_1 + 1) % (len(line) - 1)
#         x_3 = (x_3 + 3) % (len(line) - 1)
#         x_5 = (x_5 + 5) % (len(line) - 1)
#         x_7 = (x_7 + 7) % (len(line) - 1)
#         if i % 2 == 0:
#             x_1_2 = (x_1_2 + 1) % (len(line) - 1)

#         i += 1

#     print("Part 1: ", trees_3)
#     print("Part 2: ", trees_1 * trees_3 * trees_5 * trees_7 * trees_1_2)
