# Ultimate Tic Tac Toe : AI Battle 🧮

Ultimate Tic Tac Toe is a combinatorial variation on the game of Tic-Tac-Toe. It's a two-player turn-based game (player1 with crosses, player2 with circles). 

## Rules 📏
It is composed of a 3x3 tic-tac-toe grid. The winner is the first to align (in a row, column, or diagonal) 3 won tic-tac-toes. Otherwise, if it is no longer possible to place any more markers, the game is declared a draw. The choice of the tic-tac-toe grid where player A can play is conditioned by the last position of player B on their tic-tac-toe. For example, if player A starts the game by playing in the central tic-tac-toe, specifically in the top-left square, then player B must play on the tic-tac-toe grid in the top-left, and so on, taking turns.

## Constraints imposed by the model ❗
The AI must be based on a Minimax algorithm, ideally with an Alpha-Beta pruning technique. It is strictly forbidden to use pre-defined lists of moves. Each decision must be calculated dynamically. Additionally, the AI must be able to make a decision within a maximum of 10 seconds.

## Battles ⚔️
The game mode offers the possibility of playing either a human vs. human duel, facing off against an artificial intelligence, or letting two artificial intelligences battle it out.

## Start the game ⏱️
```python
python .\main.py
```

Enjoy 😊
