import requests
import os
import re

cookies = dict(session=os.environ.get('SESSION_ID'))
r = requests.get('https://adventofcode.com/2020/day/4/input', cookies=cookies)
input = [' '.join(each.split('\n')) for each in r.text.strip().split('\n\n')]
input_dict = [dict([pair.split(':') for pair in passport.split(' ')])
              for passport in input]

compulsory_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

count_1 = 0
for passport in input:
    if all(field in passport.keys() for field in compulsory_fields):
        count_1 += 1
print(count_1)


def check_min_max(num, min, max):
    try:
        return int(num) and min <= int(num) <= max
    except ValueError:
        return False


count_2 = 0
for passport in input_dict:
    if all(field in passport.keys() for field in compulsory_fields):
        check_byr = check_min_max(passport['byr'], 1920, 2002)
        check_iyr = check_min_max(passport['iyr'], 2010, 2020)
        check_eyr = check_min_max(passport['eyr'], 2020, 2030)
        height = re.match(r'(\d+)(cm|in)', passport['hgt'])
        check_hgt = False
        if height and height.end() > 1:
            if height[2] == 'cm' and check_min_max(height[1], 150, 193):
                check_hgt = True
            if height[2] == 'in' and check_min_max(height[1], 59, 76):
                check_hgt = True
        check_hcl = re.match(r'^#[a-f0-9]{6}$', passport['hcl'])
        check_ecl = passport['ecl'] in [
            'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
        check_pid = re.match(r'^\d{9}$', passport['pid'])
        if all([check_byr, check_iyr, check_eyr, check_hgt, check_hcl, check_ecl, check_pid]):
            count_2 += 1

print(count_2)
