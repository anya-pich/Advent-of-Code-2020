from helpers import get_input

input = get_input(3).split('\n')

tree_count = 0
i = 0
for line in input:
    if line[i] == '#':
        tree_count += 1
    i += 3
    if i > len(input[0])-1:
        i -= len(input[0])

print(tree_count)


def count_trees(map, delta_x, delta_y):
    tree_count = 0
    x = 0
    for y in range(0, len(map), delta_y):
        if map[y][x] == '#':
            tree_count += 1
        x += delta_x
        if x >= len(input[0])-1:
            x -= len(input[0])
    return tree_count


print(count_trees(input, 1, 1)*count_trees(input, 3, 1) *
      count_trees(input, 5, 1)*count_trees(input, 7, 1)*count_trees(input, 1, 2))
