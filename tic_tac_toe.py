board = [" " for _ in range(9)]

def print_board():
    print()
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("--+---+--")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("--+---+--")
    print(board[6] + " | " + board[7] + " | " + board[8])
    print()

def check_winner(board, player):

    wins = [
        [0,1,2],
        [3,4,5],
        [6,7,8],
        [0,3,6],
        [1,4,7],
        [2,5,8],
        [0,4,8],
        [2,4,6]
    ]

    for combo in wins:
        if all(board[i] == player for i in combo):
            return True

    return False

def is_draw(board):
    return " " not in board

def human_move():

    while True:

        try:
            move = int(input("Choose position (1-9): ")) - 1

            if 0 <= move <= 8 and board[move] == " ":
                board[move] = "X"
                break
            else:
                print("Invalid move!")

        except:
            print("Enter a number.")

def minimax(board, is_maximizing):

    if check_winner(board, "O"):
        return 1

    if check_winner(board, "X"):
        return -1

    if is_draw(board):
        return 0

    if is_maximizing:

        best_score = -1000

        for i in range(9):

            if board[i] == " ":

                board[i] = "O"

                score = minimax(board, False)

                board[i] = " "

                best_score = max(score, best_score)

        return best_score

    else:

        best_score = 1000

        for i in range(9):

            if board[i] == " ":

                board[i] = "X"

                score = minimax(board, True)

                board[i] = " "

                best_score = min(score, best_score)

        return best_score

def ai_move():

    best_score = -1000
    move = None

    for i in range(9):

        if board[i] == " ":

            board[i] = "O"

            score = minimax(board, False)

            board[i] = " "

            if score > best_score:
                best_score = score
                move = i

    board[move] = "O"

while True:

    print_board()

    human_move()

    if check_winner(board, "X"):
        print_board()
        print("You win!")
        break

    if is_draw(board):
        print_board()
        print("Draw!")
        break

    ai_move()

    if check_winner(board, "O"):
        print_board()
        print("AI wins!")
        break

    if is_draw(board):
        print_board()
        print("Draw!")
        break