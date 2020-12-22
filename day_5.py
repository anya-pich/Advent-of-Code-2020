from helpers import get_input

input = get_input(5).split('\n')


def decipher_binary(binary, total, hi, lo):
    options = list(range(total))
    for letter in binary:
        i = len(options)//2
        if letter == hi:
            options = options[i:]
        if letter == lo:
            options = options[:i]
    return options[0]


max_seat_id = 0
ids = []
for each in input:
    row, seat = each[:7], each[7:]
    row_number = decipher_binary(row, 128, 'B', 'F')
    seat_number = decipher_binary(seat, 8, 'R', 'L')
    seat_id = row_number * 8 + seat_number
    ids.append(seat_id)
    max_seat_id = seat_id if seat_id > max_seat_id else max_seat_id
print(max_seat_id)


ids.sort()
all_ids = set(range(ids[0], ids[-1]+1))
empty_seat = all_ids.difference(set(ids))

print(empty_seat)
