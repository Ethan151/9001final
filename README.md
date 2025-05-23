
# Minesweeper

A console-based Minesweeper game developed in Python. Left-click to reveal a tile, right-click to mark a tile as suspected mine. Reveal all non-mine tiles to win, reveal any mine to lose.

## Features

- Console-based gameplay
- Left-click to reveal tiles
- Right-click to mark/unmark suspected mines
- Customizable map size and mine count
- Tester mode with functional map display

## Installation

Run the game in any environment that supports Python, such as VS Code.

## Gameplay Instructions

1. Run the program to see the introduction and game controls in the console.
2. You will be asked if you are a tester. If yes, the functional map will be displayed after generating mines.
3. Enter the map size: two numbers between 2 and 20 separated by a space (e.g., `5 20`).
4. Enter the number of mines (limited by map size).
5. If you are a tester, you will see the functional map: `0-8` indicates the number of surrounding mines, `9` indicates a mine.
6. Regardless of tester status, the unrevealed map will be displayed to start the game.
7. Enter `<command> x y` to play:
   - `L` for left-click (reveal)
   - `R` for right-click (mark/unmark)
8. Enter `END` to terminate the game.
9. Reveal all non-mine tiles to win, reveal any mine to lose.

## Disclaimer

This project is developed for educational purposes (COMP9001 Assignment). Not intended for commercial use.

## Author

- **Name**: Xudong Chen
- **University**: University of Sydney
- **Course**: COMP9001 Final Project
- **Email**: 2201961842@qq.com
