# Chess Alignment Game

A simple chess-inspired game developed with **Pygame**, where the objective is to align three pieces. This is a logic and strategy game for two players, based on chess movements but with custom rules.

## 🕹 How to Run

Make sure you have **Python 3** and **Pygame** installed.

```bash
pip3 install pygame
```

Then, run the game with:

```bash
python3 Menu.py
```

## 🎯 Objective

The game ends in one of two ways:
- A player aligns **three of their pieces** vertically, horizontally, or diagonally.
- A player has **no valid moves** left — that player loses the game.

## 🧩 Game Rules

1. **Initial Placement Phase**:
   - Each player takes turns placing their pieces on the board.
   - The placement continues until all pieces are on the board.

2. **Movement Phase**:
   - Once all pieces are placed, players alternate turns.
   - Each piece moves **according to its type**, using standard chess rules (e.g., bishops move diagonally).
   - **Capturing is not allowed** — players cannot remove opponent pieces.

3. **Winning Conditions**:
   - A player wins by forming a line of **three of their own pieces**: vertically, horizontally, or diagonally.
   - If a player has no legal move on their turn, they **lose the game**.

## 📁 Project Structure

```
Projeto de Física/
│
├── images/               # Folder with all image assets
│   ├── Board.png
│   ├── CB.svg, BB.svg, etc.
│
├── Button.py             # Button class
├── Centrar.py            # Utilities for centering elements
├── Chess.py              # Piece definitions and logic
├── Menu.py               # Game launcher and main menu
├── Movements.py          # Handles movement logic
└── README.md             # This file
```

---

Have fun and good luck strategizing!