#  File: Spiral.py
#  Student Name: SaiSathvik Katta
#  Student UT EID: sk49699

import sys
# Input: in_data - handle to the input file
# Output: integer size of the spiral, odd integer between 1 and 100

spiralmatrix = []
def get_dimension(in_data):
    pass
    try:
        #Gets the dimensions of the spiral and makes sure its within the bounds of the spiral
        n = int(in_data.readline())
        if n >= 1 and n <= 99:
            if n % 2 == 0:
                n = n+1
        else:
            print("Invalid spiral size")
            return -1
    except ValueError:
        print("Invalid spiral size")
        return -1

    return int(n)

# Input: n - size of spiral
# Output: returns a 2-D list representing a spiral
def create_spiral(n):
    pass
    #Creates an matrix of only zeros depending on the size of n
    for i in range (n):
        list = []
        for j in range(n):
            list.append(0)
        spiralmatrix.append(list)

    spirals = n // 2
    row = int(spirals)
    column = int(spirals)

    #Initializes the Variables
    number = 1
    columnright = 1
    columndown = 1
    columnleft = 2
    columnup = 2
    columnright2 = 2

    for i in range (spirals):
    #Runs the loop to match the number of spirals
        spiralmatrix[row][column] = number
        number += 1
    #5 for loops are used to create the spiral, one for each time the direction changes
        for r in range(columnright):
        #right, always shifts to the right by 1, increase by 1 for every new spiral
            column += 1
            spiralmatrix[row][column] = number
            number += 1

        for r in range(columndown):
        #down, always increasing, increase by 2 for each spiral
            row +=1
            spiralmatrix[row][column] = number
            number +=1
        columndown += 2

        for r in range(columnleft):
        #left, always decreasing, increase by 2 for each spiral
            column -= 1
            spiralmatrix[row][column] = number
            number += 1
        columnleft += 2

        for r in range(columnup):
        #up, always decreasing, increase by 2 for each spiral
            row -= 1
            spiralmatrix[row][column] = number
            number += 1
        columnup += 2

        for r in range(columnright2):
        #right2, always increasing, increase by 2 for each spiral
            column += 1
            spiralmatrix[row][column] = number
            number += 1
        columnright2 += 2
        number-=1

    print(spiralmatrix)
    return spiralmatrix

# Input: in_data - handle to input file, spiral - the number spiral
# Output: calls method for each integer in file
def print_adjacent_sums(in_data, spiralmatrix):
    pass
    #Processes every line in the file and checks to ensure that the number to find sum is in the spiral
    #Then passes the number to the sum_adjacent_numbers function to calculate sum
    done = False
    while not done:
        try:
            for line in (in_data):
                sum_num = int(line.strip())
                if sum_num > 0:
                    if 1 <= sum_num <= len(spiral) ** 2:
                        sum_adjacent_numbers(spiralmatrix, sum_num)
                    else:
                        print(0)
            done = True
        except ValueError:
            pass

# Input: spiral - the number spiral
#        n - the number to find the adjacent sum for
# Output: integer that is the sum of the
#         numbers adjacent to n in the spiral
#         if n is outside the range return 0
def sum_adjacent_numbers(spiralmatrix, n):
    pass
    #Sum for Corners
    if spiralmatrix[0][0] == n: #top right
        sum = spiralmatrix[0][1] + spiralmatrix[1][0] + spiralmatrix[1][1]
    elif spiralmatrix[0][-1] == n: #top left
        sum = spiralmatrix[0][-2] + spiralmatrix[1][-2] + spiralmatrix[1][-1]
    elif spiralmatrix[-1][0] == n: #bottom right
        sum = spiralmatrix[-2][0] + spiralmatrix[-2][1] + spiralmatrix[-1][1]
    elif spiralmatrix[-1][-1] == n: #bottom left
        sum = spiralmatrix[-1][-2] + spiralmatrix[-2][-2] + spiralmatrix[-2][-1]
    else:
        #For Loops are used to find the exact index of n
        for i in range(len(spiralmatrix)):
            for j in range(len(spiralmatrix[i])):
                if spiralmatrix[i][j] == n:
                    r = i
                    c = j
                    if r == 0: # top edge
                        sum = (spiralmatrix[r][c-1]+ spiralmatrix[r+1][c-1] + spiralmatrix[r+1][c]
                               + spiralmatrix[r+1][c+1] + spiralmatrix[r][c+1])
                    elif c == 0: #left edge
                        sum = (spiralmatrix[r-1][c] + spiralmatrix[r-1][c+1] + spiralmatrix[r][c+1]
                               + spiralmatrix[r+1][c+1] + spiralmatrix[r+1][c])
                    elif r == len(spiralmatrix)-1: # bottom edge
                        sum = (spiralmatrix[r][c-1] + spiralmatrix[r-1][c-1] + spiralmatrix[r-1][c]
                               + spiralmatrix[r-1][c+1] + spiralmatrix[r][c+1])
                    elif c == len(spiralmatrix)-1: # right edge
                        sum = (spiralmatrix[r - 1][c] + spiralmatrix[r - 1][c - 1] + spiralmatrix[r][c -1]
                               + spiralmatrix[r + 1][c - 1] + spiralmatrix[r + 1][c])
                    else: #calculates sum for any number in the middle
                        sum = (spiralmatrix[r][c+1] + spiralmatrix[r+1][c+1] + spiralmatrix[r+1][c]
                               + spiralmatrix[r+1][c-1] + spiralmatrix[r][c-1] + spiralmatrix[r-1][c-1]
                               + spiralmatrix[r-1][c] + spiralmatrix[r-1][c+1])
    print(sum)

# Added for debugging only. No changes needed.
# Do not call this method in submitted version of your code.
# Input: spiral - the number spiral
# Output: printed spiral
def print_spiral(spiral):
    for i in range(0, len(spiral)):
        for j in range(0, len(spiral[0])):
            row_format = '{:>4}'
            print(row_format.format(spiral[i][j]), end='')
        print()

# set the input source - change to False before submitting
debug = False
if debug:
    in_data = open('spiral.in')
else:
    in_data = sys.stdin

# get the spiral size from the file
size = get_dimension(in_data)

# if valid spiral size
if size != -1:
    
    # create the spiral
    spiral = [[]]
    spiral = create_spiral(size)

    # use following line for debugging only
    print_spiral(spiral)

    # process and print adjacent sums
    print_adjacent_sums(in_data, spiral)
