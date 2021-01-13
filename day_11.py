input = '''
L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL
'''
input = input.strip().split('\n')
input_matrix = [[letter for letter in line] for line in input]
print(input_matrix)


def round_one(seating):
    # If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
    # If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
    height = len(seating)
    width = len(seating[0])
    for h in range(height):
        for w in range(width):
            print(seating[h][w])


round_one(input_matrix)
