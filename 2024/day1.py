locations_ids_left = []
locations_ids_right = []
with open("./inputs/day1.txt", "r", encoding="utf-8") as f:
    for line in f:
        left, right = line.split("   ")
        locations_ids_left.append(int(left))
        locations_ids_right.append(int(right))

sorted_left = sorted(locations_ids_left)
sorted_right = sorted(locations_ids_right)

# Part 1
distances = []
for idx, number in enumerate(sorted_left):
    distances.append(abs(number - sorted_right[idx]))

print(sum(distances))


# Part 2
similarity_table = {}
silimarity_score = []
for idx, number in enumerate(sorted_left):
    if similarity_table.get(number):
        continue
    similarity_table[number] = len(list(filter(lambda x: x == number, sorted_right)))

import json

print(json.dumps(similarity_table, indent=4))
for idx, number in enumerate(sorted_left):
    silimarity_score.append(similarity_table[number] * number)

print(sum(silimarity_score))
