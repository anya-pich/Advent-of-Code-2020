import copy
import os
import requests

cookies = dict(session=os.environ.get('SESSION_ID'))
r = requests.get('https://adventofcode.com/2020/day/8/input', cookies=cookies)
input = r.text.strip().split('\n')

# Part 1


def play_game(input):
    accumulator = 0
    done_indexes = set()
    i = 0
    while i not in done_indexes:
        done_indexes.add(i)
        move_type, move_value = input[i].split(' ')
        if move_type == 'acc':
            accumulator += int(move_value)
            i += 1
        elif move_type == 'jmp':
            i += int(move_value)
        elif move_type == 'nop':
            i += 1
    return accumulator


print(play_game(input))

# Part 2


def play_game(input):
    accumulator = 0
    done_indexes = set()
    i = 0
    while 0 <= i < len(input) and i not in done_indexes:
        done_indexes.add(i)
        move_type, move_value = input[i].split(' ')
        if move_type == 'acc':
            accumulator += int(move_value)
            i += 1
        elif move_type == 'jmp':
            i += int(move_value)
        elif move_type == 'nop':
            i += 1
    if i == len(input):
        return accumulator
    return None


def fix_game(input):
    for i, instruction in enumerate(input):
        instructions = copy.deepcopy(input)
        if 'jmp' in instruction:
            instructions[i] = instruction.replace('jmp', 'nop')
        elif 'nop' in instruction:
            instructions[i] = instruction.replace('nop', 'jmp')
        result = play_game(instructions)
        if result:
            return result


print(fix_game(input))
