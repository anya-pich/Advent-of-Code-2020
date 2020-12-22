import requests
import os


def get_input(day):
    cookies = dict(session=os.environ.get('SESSION_ID'))
    r = requests.get(f'https://adventofcode.com/2020/day/{day}/input', cookies=cookies)
    return r.text.strip()
