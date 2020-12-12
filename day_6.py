import requests
import os

cookies = dict(session=os.environ.get('SESSION_ID'))
r = requests.get('https://adventofcode.com/2020/day/6/input', cookies=cookies)
input = r.text.strip().split('\n\n')

group_strings = [''.join(group.split('\n')) for group in input]
sum_1 = 0
for group in group_strings:
    sum_1 += len(set(group))
print(sum_1)

group_lists = [group.split('\n') for group in input]
sum_2 = 0
for group in group_lists:
    yesses = set(group[0])
    if len(group) > 1:
        for person in group[1:]:
            yesses = yesses.intersection(set(person))
    sum_2 += len(yesses)
print(sum_2)
