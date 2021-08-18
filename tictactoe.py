# write your code here
def draw_paint(matrix):
    print('---------')
    print('| ' + matrix[0][0] + ' ' + matrix[0][1] + ' ' + matrix[0][2] + ' ' + '|')
    print('| ' + matrix[1][0] + ' ' + matrix[1][1] + ' ' + matrix[1][2] + ' ' + '|')
    print('| ' + matrix[2][0] + ' ' + matrix[2][1] + ' ' + matrix[2][2] + ' ' + '|')
    print('---------')


def judge_result(matrix):
    X_win = False
    O_win = False
    for i in range(3):
        if matrix[i][0] == matrix[i][1] == matrix[i][2]:
            if matrix[i][0] == 'X':
                X_win = True
            elif matrix[i][0] == 'O':
                O_win = True
        if matrix[0][i] == matrix[1][i] == matrix[2][i]:
            if matrix[0][i] == 'X':
                X_win = True
            elif matrix[0][i] == 'O':
                O_win = True
        if (matrix[0][0] == matrix[1][1] == matrix[2][2]) or (matrix[0][2] == matrix[1][1] == matrix[2][0]):
            if matrix[1][1] == 'X':
                X_win = True
            elif matrix[1][1] == 'O':
                O_win = True
    return X_win, O_win


def print_result(X_win, O_win):
    if X_win:
        print('X wins')
    elif O_win:
        print('O wins')
    else:
        print('Draw')


def determine_the_chess(flag, new_pieces, number_of_X, number_of_O, matrix):
    flag = 0
    if (new_pieces[0] not in number) or (new_pieces[1] not in number):
        print('You should enter number!')
    elif (new_pieces[0] not in right_number) or (new_pieces[1] not in right_number):
        print('Coordinates should be from 1 to 3!')
    elif matrix[int(new_pieces[0]) - 1][int(new_pieces[1]) - 1] != ' ':
        print('This cell is occupied! Choose another one!')
    else:
        if number_of_X == number_of_O + 1:
            matrix[int(new_pieces[0]) - 1][int(new_pieces[1]) - 1] = 'O'
            number_of_O += 1
            flag = 1
        elif number_of_X == number_of_O:
            matrix[int(new_pieces[0]) - 1][int(new_pieces[1]) - 1] = 'X'
            number_of_X += 1
            flag = 1
    return flag, number_of_X, number_of_O, matrix


flag = 0
number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
right_number = ['1', '2', '3']
number_of_X = 0
number_of_O = 0

cell = '         '
matrix = [[cell[3 * i], cell[3 * i + 1], cell[3 * i + 2]] for i in range(3)]
draw_paint(matrix)

while(1):
    new_pieces = str(input('Enter the coordinates: '))
    new_pieces = new_pieces.split()   # list with 2 str
    flag, number_of_X, number_of_O, matrix = determine_the_chess(flag, new_pieces, number_of_X, number_of_O, matrix)
    if flag:
        draw_paint(matrix)
        flag = 0
    X_win, O_win = judge_result(matrix)
    if X_win or O_win:
        break
    if (number_of_X + number_of_O) == 9:
        break

print_result(X_win, O_win)
