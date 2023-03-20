board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]

def print_board(bo):

    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - -")

        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print("| ", end = "")

            if j == 8:
                print (bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end = "")

def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j) # row, col
    return False

def is_valid(bo, pos, num):

    #check valid column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False
    
    #check valid row
    for j in range(len(bo[0])):
        if bo[pos[0]][j] == num and pos[1] != j:
            return False

    #check valid box
    box_row = pos[0] // 3
    box_col = pos[1] // 3
    for i in range(box_row * 3, box_row * 3 + 3):
        for j in range(box_col * 3, box_col * 3 + 3):
            if bo[i][j] == num and pos != (i, j):
                return False
    return True

#recursive solving algorithm
def solve(bo):
    #base case
    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find

    for x in range(1, 10):
        if is_valid(bo, (row, col), x):
            bo[row][col] = x

            if solve(bo):
                return True

            bo[row][col] = 0

    return False

print_board(board)
solve(board)
print("________________________")
print_board(board)