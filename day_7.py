import requests
import os
import re

cookies = dict(session=os.environ.get('SESSION_ID'))
r = requests.get('https://adventofcode.com/2020/day/7/input', cookies=cookies)
input = r.text.strip().split('\n')

rules = dict([line.split(' bags contain ') for line in input])

# Part 1


def find_outer_bags(bags):
    if not bags:
        return set()
    else:
        new_bags = set()
        for bag in bags:
            for key, value in rules.items():
                if bag in value:
                    new_bags.add(key)
        return bags | find_outer_bags(new_bags)


outer_bags = find_outer_bags({'shiny gold'}) - {'shiny gold'}
print(len(outer_bags))

#  Part 2


rules = {k: re.sub(r' bag[s]?[.]?', '', v).split(', ') for (k, v) in rules.items()}
rules = {k: [b.split(' ', 1) for b in v if b != 'no other'] for (k, v) in rules.items()}
print(rules)


def find_inner_bags(bag):
    bags_inside = rules[bag]
    if not bags_inside:
        return 0
    else:
        return sum(int(bag[0]) * (find_inner_bags(bag[1]) + 1) for bag in bags_inside)


print(find_inner_bags('shiny gold'))
