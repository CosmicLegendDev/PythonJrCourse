# Tic-Tac-Toe Game

A simple two-player tic-tac-toe game that runs in the terminal.

## How to Play

1. Run the program:

   ```bash
   python tic_tac_toe.py
   ```

2. Two players take turns (Player X goes first)

3. Enter a position number (1-9) to place your mark:

   ```
   Position numbers:
    1 | 2 | 3
   ---+---+---
    4 | 5 | 6
   ---+---+---
    7 | 8 | 9
   ```

4. The first player to get three marks in a row (horizontally, vertically, or diagonally) wins!

5. If all 9 positions are filled with no winner, the game is a draw.

## Game Rules

- Player X always goes first
- Players alternate turns
- Choose a position from 1-9 that's not already taken
- Get three marks in a row to win:
  - Horizontal: [1,2,3], [4,5,6], or [7,8,9]
  - Vertical: [1,4,7], [2,5,8], or [3,6,9]
  - Diagonal: [1,5,9] or [3,5,7]

## Features

- Input validation (prevents invalid moves)
- Clear board display after each move
- Win detection for all possible winning combinations
- Draw detection when board is full
- Option to play multiple games

## Python Concepts Used

- **Functions**: Modular code organization
- **Lists**: Board representation
- **Loops**: Game loop and input validation
- **Conditionals**: Move validation and win checking
- **Input/Output**: Player interaction
- **String formatting**: Board display

## Example Game

```
Position numbers:
 1 | 2 | 3
---+---+---
 4 | 5 | 6
---+---+---
 7 | 8 | 9

   |   |
---+---+---
   |   |
---+---+---
   |   |

Player X, enter position (1-9): 5

   |   |
---+---+---
   | X |
---+---+---
   |   |

Player O, enter position (1-9): 1
...
```

Enjoy playing! 🎮
