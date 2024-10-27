# Tic-Tac-Toe Game with Leaderboard

This is a terminal-based **Tic-Tac-Toe game** implemented in Python. It supports two players, keeps track of wins, losses, and draws using a leaderboard stored in a JSON file. You can also print or clear the leaderboard through the available commands.

---

## Prerequisites

1. Python 3.x installed on your system.
2. Install the dependencies via:

   ```bash
   pip install termcolor
   ```

---

## How to Run

You can run the program using **command-line arguments** to start the game, print the leaderboard, or clear it.

### Basic Command

```bash
python main.py [options]
```

---

## Commands

1. **Play the game:**

   ```bash
   python main.py --play
   ```

   - **Description**: 
     Starts a new Tic-Tac-Toe game between two players.
   - **Instructions**:
     - You will be prompted to enter the names of the two players.
     - The game alternates turns between players using **X** and **O**.
     - Input moves as **row** and **column** (e.g., `1 2`).
     - A win or draw updates the leaderboard.
     - You can choose to play another round after finishing a game.

2. **View the leaderboard:**

   ```bash
   python main.py --leaderboard
   ```

   - **Description**: 
     Displays the leaderboard with player names, wins, losses, and draws.
   - **Output Example**:
     ```
         player                    w        d       l    
     --------------------------------------------------
     1. Alice                    2        1       0    
     2. Bob                      0        1       2    
     ```

3. **Clear the leaderboard:**

   ```bash
   python main.py --clear
   ```

   - **Description**: 
     Clears the leaderboard data, resetting all player statistics.

4. **Invalid command:**

   - If you run the script without any valid command, you'll get an error message:

     ```
     Invalid command!
     ```

---

## Game Rules

1. **Win:** A player wins by aligning three of their symbols (either X or O) horizontally, vertically, or diagonally.
2. **Draw:** The game is declared a draw if the board is full without any winner.
3. **Leaderboard Updates:**
   - Winner’s win counter (`w`) increments.
   - Loser’s loss counter (`l`) increments.
   - If the game is a draw, both players' draw counter (`d`) increments.

---

## Example Gameplay

```
Enter names of two players separated by a slash(/): Alice/Bob
Hi, Alice! Good luck!
Hi, Bob! Good luck!

Enter your next move, Alice as X (row column): 1 1
| X _ _ |
| _ _ _ |
| _ _ _ |

Enter your next move, Bob as O (row column): 2 2
| X _ _ |
| _ O _ |
| _ _ _ |

...
Congrats, Alice, you have won! 🥳🥳
Would you like to play another round?: yes
```

---

## Leaderboard Data

The leaderboard is stored in `./data/leaderboard.json` in the following format:

```json
{
  "Alice": {
    "w": 2,
    "l": 0,
    "d": 1
  },
  "Bob": {
    "w": 0,
    "l": 2,
    "d": 1
  }
}
```

---

## Handling Errors

- **Invalid Input:** If the input is not a valid row/column number, an error message will be shown.
- **Occupied Cell:** If a player selects an already occupied cell, they will be prompted to choose another.

---

## Conclusion

This project provides a simple way to play Tic-Tac-Toe in the terminal while keeping track of player performance through a leaderboard. Enjoy playing! 😊
