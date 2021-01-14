class Position:
    def __init__(self, row, col):
        self.row = row
        self.col = col
def draw_table(table):
    print(" %c | %c | %c " % (table[0][0], table[0][1], table[0][2]))
    print("___|___|___")
    print(" %c | %c | %c " % (table[1][0], table[1][1], table[1][2]))
    print("___|___|___")
    print(" %c | %c | %c " % (table[2][0], table[2][1], table[2][2]))
    print("   |   |   ")

def is_box_remaining(table):
    for i in range(3):
        for j in range(3):
            if table[i][j] == " ":
                return True
    return False

def check_position(table, row, col):
    if table[row][col] == ' ':
        return True
    return False

def check_winning_condition(table):
    for row in range(3):
        if table[row][0] == table[row][1] and table[row][1] == table[row][2]:
            if table[row][0] == ai:
                return +10
            elif table[row][0] == player:
                return -10

    for col in range(3):
        if table[0][col] == table[1][col] and table[1][col] == table[2][col]:
            if table[0][col] == ai:
                return +10
            elif table[0][col] == player:
                return -10
    if table[0][0] == table[1][1] and table[1][1] == table[2][2]:
        if table[0][0] == ai:
            return +10
        elif table[0][0] == player:
            return -10

    if table[0][2] == table[1][1] and table[1][1] == table[2][0]:
        if table[0][2] == ai:
            return +10
        elif table[0][2] == player:
            return -10


def apply_minmax(table, depth, is_max):
    score = check_winning_condition(table)

    if score == 10:
        return score
    if score == -10:
        return score

    if not is_box_remaining(table):
        return 0

    if is_max:
        best = -1000
        for i in range(3):
            for j in range(3):
                if table[i][j] == ' ':
                    table[i][j] = ai
                    best = max(best, apply_minmax(table, depth + 1, not is_max))
                    table[i][j] = ' '
        return best
    else:
        best = 1000
        for i in range(3):
            for j in range(3):
                if table[i][j] == ' ':
                    table[i][j] = player
                    best = min(best, apply_minmax(table, depth + 1, not is_max))
                    table[i][j] = ' '
        return best


def select_best_box(table):
    best_value = -1000
    best_move = Position(-1, -1)
    for i in range(3):
        for j in range(3):
            if table[i][j] == ' ':
                table[i][j] = ai
                move_val = apply_minmax(table, 0, False)
                table[i][j] = ' '
                if move_val > best_value:
                    best_move.row = i
                    best_move.col = j
                    best_value = move_val
    return best_move

def check_box_vacancy(position):
    if position % 3 == 0 :
        row = int(position / 3) - 1
        col = 2
    else:
        row = int(position / 3)
        col = int(position%3)-1 
    if check_position(main_table, row, col):
         main_table[row][col] = player
         return False
    else:
        print("This box is already filled up. Choose another box.")
        return True
        
if __name__ == "__main__":
    player = 'x'
    ai = 'o'
    demo_table = [
        ['1', '2', '3'],
        ['4', '5', '6'],
        ['7', '8', '9']
    ]
    print("\n\n --------WELCOME TO TIC_TAC_TOE-------\n\nThis are the indices of the table")
    draw_table(demo_table)
    print("\n\n")
    main_table = [
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']
    ]
    while True:
        draw_table(main_table)
        val = check_winning_condition(main_table)
        if val == 10:
            print("\n\n!~!~!~!~!~!~ Computer wins !~!~!~!~!~!~\n\n")
            break
        elif val == -10:
            print("\n\n!~!~!~!~!~! You win !~!~!~!~!~!\n\n")
            break
        elif (val != 10 or -10) and is_box_remaining(main_table) is False:
            print("\n\n====== Game Tied ======\n\n")
            break
        choice = int(input("Choose the index of your preferred blank box >>>>\n"))
        if check_box_vacancy(choice) :
            continue
        draw_table(main_table)
        if is_box_remaining(main_table):
            print("Computer is selecting it's move")
            move_ai = select_best_box(table=main_table)
            main_table[move_ai.row][move_ai.col] = ai