from helpers import get_input

input = get_input(9).split('\n')
input = [int(each) for each in input]
# print(input)


# Part 1

def find_conforming(target, numbers):
    for number in numbers:
        complement = target - number
        if complement in numbers and not number == complement:
            return True
    return False


def find_nonconforming(numbers):
    i = 25
    next = True
    while next:
        if find_conforming(numbers[i], numbers[i-25:i]):
            i += 1
        else:
            return numbers[i]


print(find_nonconforming(input))


# Part 2

def find_subsequence(numbers, goal):
    for i, n in enumerate(input):
        sequence = [n]
        sum = n
        loc = i
        while sum < goal:
            loc += 1
            sequence.append(input[loc])
            sum += input[loc]
        if sum == goal:
            return min(sequence) + max(sequence)


print(find_subsequence(input, 507622668))
