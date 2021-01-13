from helpers import get_input

input = [int(n) for n in get_input(10).split('\n')]
input.append(0)  # to account for outlet joltage
input.sort()

# Part 1

one_jolt_counter = 0
three_jolt_counter = 1  # to account for device joltage always being 3J higher

for i, num in enumerate(input):
    if i < len(input) - 1:
        jolt_delta = input[i+1] - num
        if jolt_delta == 1:
            one_jolt_counter += 1
        if jolt_delta == 3:
            three_jolt_counter += 1


print(one_jolt_counter * three_jolt_counter)

# Part 2

# count all the ways to get from 0 to max(input)
# where each sequential adapter is previous adapter =+ (1-3)

# example = [0, 1, 4, 5, 6, 7, 10, 11, 12, 15, 16, 19]


def count_arrangements(sequence):
    # if len(sequence) == 1:
    #     return 1
    # else:
    #     limit = 4 if len(sequence) > 3 else len(sequence)
    #     start = sequence[0]
    #     sub_arrangements = 0
    #     for i, num in enumerate(sequence[1:limit]):
    #         if num <= start + 3:
    #             sub_arrangements += count_arrangements(sequence[i+1:])
    #     return sub_arrangements
    deltas = []
    for i, n in enumerate(sequence[:-1]):
        deltas.append(sequence[i+1]-n)
        print(f'{n} to {sequence[i+1]} delta {sequence[i+1]-n}')

    for streak in deltas:
        permutations = 1
        if streak // 2:
            permutations += streak // 2

    return deltas


# print(count_arrangements(example))
print(count_arrangements(input))
