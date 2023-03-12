# Reverse Minesweeper \[[link](https://www.codingame.com/training/easy/reverse-minesweeper)\]


 Goal
-----


Given a grid of mine locations (where . are empty cells and x are mines), your goal is to display the grid like it appears if you win the game.  
Each position is a digit indicating the number of mines bordering it (including diagonals). The mines (x) don't appear anymore. Mines and positions that do not border any mines both appear as empty cells (.).



Input
**Line 1 :** an integer w for the width of the grid.  
**Line 2 :** an integer h for the height of the grid.  
**Next h lines :** each line of the minefield, with dots (.) or mines (x).


Output
h lines of width w showing the completed game of Minesweeper.


Constraints
1 <= w <= 30  
1 <= h <= 30


Example


Input

```
16
9
................
................
................
................
................
....x...........
................
................
................
```



Output

```
................
................
................
................
...111..........
...1.1..........
...111..........
................
................
```





Solutions:
| filename | Language | Submission date |
| --- | --- | --- |
| solution_0.py | Python3 | 2023-02-16 Thu 21:40 |
| solution_1.py | Python3 | 2023-02-16 Thu 21:40 |
| solution_2.py | Python3 | 2023-02-16 Thu 21:39 |
