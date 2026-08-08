"""
Tic-Tac-Toe Game
A simple two-player tic-tac-toe game played in the terminal.
Players: X and O
"""

def create_board():
    """Create and return an empty 3x3 board"""
    return [' ' for _ in range(9)]


def display_board(board):
    """Display the current state of the board"""
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")


def display_positions():
    """Show position numbers to help players"""
    print("\nPosition numbers:")
    print(" 1 | 2 | 3 ")
    print("---+---+---")
    print(" 4 | 5 | 6 ")
    print("---+---+---")
    print(" 7 | 8 | 9 ")
    print("\n")


def is_valid_move(board, position):
    """Check if the move is valid"""
    if position < 1 or position > 9:
        return False
    if board[position - 1] != ' ':
        return False
    return True


def make_move(board, position, player):
    """Place the player's mark on the board"""
    board[position - 1] = player


def check_winner(board):
    """Check if there's a winner. Returns 'X', 'O', or None"""
    # All possible winning combinations
    winning_combinations = [
        [0, 1, 2],  # Top row
        [3, 4, 5],  # Middle row
        [6, 7, 8],  # Bottom row
        [0, 3, 6],  # Left column
        [1, 4, 7],  # Middle column
        [2, 5, 8],  # Right column
        [0, 4, 8],  # Diagonal from top-left
        [2, 4, 6]   # Diagonal from top-right
    ]
    
    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != ' ':
            return board[combo[0]]
    
    return None


def is_board_full(board):
    """Check if the board is full (draw)"""
    return ' ' not in board


def get_player_move(board, player):
    """Get valid move from the player"""
    while True:
        try:
            position = int(input(f"Player {player}, enter position (1-9): "))
            if is_valid_move(board, position):
                return position
            else:
                print("Invalid move! Position is already taken or out of range.")
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 9.")


def play_game():
    """Main game loop"""
    print("=" * 40)
    print("Welcome to Tic-Tac-Toe!")
    print("=" * 40)
    
    # Initialize game
    board = create_board()
    current_player = 'X'
    game_over = False
    
    # Show position guide
    display_positions()
    
    # Game loop
    while not game_over:
        # Display current board
        display_board(board)
        
        # Get player move
        position = get_player_move(board, current_player)
        make_move(board, position, current_player)
        
        # Check for winner
        winner = check_winner(board)
        if winner:
            display_board(board)
            print(f"🎉 Congratulations! Player {winner} wins! 🎉")
            game_over = True
        elif is_board_full(board):
            display_board(board)
            print("It's a draw! The board is full.")
            game_over = True
        else:
            # Switch player
            current_player = 'O' if current_player == 'X' else 'X'
    
    print("\nThanks for playing!")


def main():
    """Main function to start the game"""
    while True:
        play_game()
        
        # Ask if players want to play again
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != 'yes' and play_again != 'y':
            print("Goodbye! Thanks for playing Tic-Tac-Toe!")
            break


if __name__ == "__main__":
    main()
