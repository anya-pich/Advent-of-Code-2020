from helpers import get_input

input = get_input(2).split('\n')

part_1, part_2 = 0, 0

for line in input:
    [range, char, password] = line.replace(':', '').split(' ')
    [x, y] = [int(n) for n in range.split('-')]
    if x <= password.count(char) <= y:
        part_1 += 1
    if (password[x-1] == char) != (password[y-1] == char):
        part_2 += 1

print(part_1, part_2)
