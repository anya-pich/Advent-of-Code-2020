from helpers import get_input

input = [int(n) for n in get_input(1).split('\n')]


def find_two_numbers(numbers):
    for x in numbers:
        for y in numbers:
            if x+y == 2020:
                return x*y


print(find_two_numbers(input))


def find_three_numbers(numbers):
    for x in numbers:
        for y in numbers:
            for z in numbers:
                if x+y+z == 2020:
                    return x*y*z


print(find_three_numbers(input))
