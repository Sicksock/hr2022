def director(column,row):
    if column == 1:
        if row == 1:
            direction = '(N)orth.'
        elif row == 2:
            direction = '(N)orth or (E)ast or (S)outh.'
        elif row == 3:
            direction = '(E)ast or (S)outh.'
    elif column == 2:
        if row == 1:
            direction = '(N)orth.'
        elif row == 2:
            direction = '(S)outh or (W)est.'
        elif row == 3:
            direction = '(E)ast or (W)est.'
    elif column == 3:
        if row == 1:
            direction = '(N)orth.'
        elif row == 2:
            direction = '(N)orth or (S)outh.'
        elif row == 3:
            direction = '(S)outh or (W)est.'
    print('You can travel: {}'.format(direction))

    move_input = input('Direction: ')

    waypoint = ''
    for i in range(len(direction)):
        if direction[i].isupper():
            waypoint = waypoint + direction[i]
    waypoint = waypoint + waypoint.lower()
    return waypoint, move_input

def movement(ask_dir,row,column):
    if ask_dir == 'n' or ask_dir == 'N':
        row += 1
    elif ask_dir == 's' or ask_dir == 'S':
        row -= 1
    elif ask_dir == 'w' or ask_dir == 'W':
        column -= 1
    elif ask_dir == 'e' or ask_dir == 'E':
        column += 1
    return column, row

def tile_traveller():
    row = 1
    column = 1

    while not((column == 3) and (row == 1)):
        
        (waypoint,move_input) = director(column,row)

        if move_input in waypoint:
            (column,row) = movement(move_input,row,column)
        else:
            print('Not a valid direction!')
    
    print('Victory!')

tile_traveller()