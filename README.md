# Sudoku Solver

## About
A Sudoku puzzle solver based on [tutorial][http://norvig.com/sudoku.html] by Peter Norwig.

I wrote this solver just for practice of ideas of Constrain Propagation and Depth First Search

## Content
- `examples.txt` -- examples of Sudoku puzzle in value-dot format to test solver.
- `input.txt` -- contains an input board for the game in a value-dot format, where all rows are concatenated and **dots** represent empty boxes.
- `README.md` -- this file.
- `solver.py` -- is used to solve a board in a `input.txt` file. Board is loaded automaticaly by running solver: `python solver.py`
- `utilities.py` -- utilities file for solver.
