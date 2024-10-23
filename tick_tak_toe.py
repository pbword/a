import math

# Constants for players
X = 'X'
O = 'O'
EMPTY = ' '

# Helper function to print the Tic-Tac-Toe board
def print_board(board):
    for row in range(3):
        print(' | '.join(board[row]))
        if row < 2:
            print('---------')

# Check for a win condition
def check_winner(board, player):
    # Check rows, columns and diagonals
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or \
           all(board[j][i] == player for j in range(3)):
            return True
    if board[0][0] == board[1][1] == board[2][2] == player or \
       board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False

# Check if the board is full
def is_full(board):
    return all(board[row][col] != EMPTY for row in range(3) for col in range(3))

# Check for a draw (no winner and board is full)
def is_draw(board):
    return is_full(board) and not (check_winner(board, X) or check_winner(board, O))

# Get all possible moves for the current player
def get_valid_moves(board):
    return [(row, col) for row in range(3) for col in range(3) if board[row][col] == EMPTY]

# Minimax algorithm with alpha-beta pruning
def minimax_alpha_beta(board, depth, alpha, beta, is_maximizing, player):
    if check_winner(board, X):
        return 10 - depth
    if check_winner(board, O):
        return depth - 10
    if is_draw(board):
        return 0

    if is_maximizing:  # Maximizing for X
        max_eval = -math.inf
        for (row, col) in get_valid_moves(board):
            board[row][col] = X
            eval = minimax_alpha_beta(board, depth + 1, alpha, beta, False, O)
            board[row][col] = EMPTY
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:  # Beta cutoff
                break
        return max_eval
    else:  # Minimizing for O
        min_eval = math.inf
        for (row, col) in get_valid_moves(board):
            board[row][col] = O
            eval = minimax_alpha_beta(board, depth + 1, alpha, beta, True, X)
            board[row][col] = EMPTY
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:  # Alpha cutoff
                break
        return min_eval

# Find the best move for the current player
def best_move(board, player):
    best_score = -math.inf if player == X else math.inf
    move = None
    for (row, col) in get_valid_moves(board):
        board[row][col] = player
        score = minimax_alpha_beta(board, 0, -math.inf, math.inf, player == O, X if player == O else O)
        board[row][col] = EMPTY
        if (player == X and score > best_score) or (player == O and score < best_score):
            best_score = score
            move = (row, col)
    return move

# Main Tic-Tac-Toe game loop
def play_tic_tac_toe():
    board = [[EMPTY for _ in range(3)] for _ in range(3)]
    print("Tic-Tac-Toe Game!")
    print_board(board)

    while True:
        # X's move (AI)
        print("\nX's Move (AI):")
        move = best_move(board, X)
        if move:
            board[move[0]][move[1]] = X
            print_board(board)
            if check_winner(board, X):
                print("X wins!")
                break
        else:
            print("It's a draw!")
            break

        # O's move (Player)
        print("\nO's Move (Player):")
        valid_moves = get_valid_moves(board)
        if not valid_moves:
            print("No valid moves left!")
            break

        move = None
        while move not in valid_moves:
            try:
                row, col = map(int, input("Enter row and column (0-2): ").split())
                move = (row, col)
            except ValueError:
                print("Invalid input. Please enter two numbers between 0 and 2.")
            if move not in valid_moves:
                print("Invalid move. Try again.")
        
        board[row][col] = O
        print_board(board)
        if check_winner(board, O):
            print("O wins!")
            break
        elif is_draw(board):
            print("It's a draw!")
            break

if __name__ == "__main__":
    play_tic_tac_toe()
