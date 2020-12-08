import requests
import os

cookies = dict(session=os.environ.get('SESSION_ID'))
r = requests.get('https://adventofcode.com/2020/day/2/input', cookies=cookies)
input = r.text.strip().split('\n')

part_1, part_2 = 0, 0

for line in input:
    [range, char, password] = line.replace(':', '').split(' ')
    [x, y] = [int(n) for n in range.split('-')]
    if x <= password.count(char) <= y:
        part_1 += 1
    if (password[x-1] == char) != (password[y-1] == char):
        part_2 += 1

print(part_1, part_2)
