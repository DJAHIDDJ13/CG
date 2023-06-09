# Sudoku Validator \[[link](https://www.codingame.com/training/easy/sudoku-validator)\]


 Goal
-----


You get a **sudoku grid** from a player and you have to check if it has been correctly filled.  
  
A sudoku grid consists of 9×9 = 81 cells split in 9 sub-grids of 3×3 = 9 cells.  
For the grid to be correct, each row must contain one occurrence of each digit (1 to 9), each column must contain one occurrence of each digit (1 to 9) and each sub-grid must contain one occurrence of each digit (1 to 9).  
  
You shall answer true if the grid is correct or false if it is not.



Input
**9 rows** of 9 space-separated digits representing the sudoku grid.


Output
true or false


Constraints
For each digit n in the grid: 1 ≤ n ≤ 9.


Example


Input

```
1 2 3 4 5 6 7 8 9
4 5 6 7 8 9 1 2 3
7 8 9 1 2 3 4 5 6
9 1 2 3 4 5 6 7 8
3 4 5 6 7 8 9 1 2
6 7 8 9 1 2 3 4 5
8 9 1 2 3 4 5 6 7
2 3 4 5 6 7 8 9 1
5 6 7 8 9 1 2 3 4
```



Output

```
true
```





Solutions:
| filename | Language | Submission date |
| --- | --- | --- |
| solution_0.c | C | 2021-03-11 Thu 20:35 |
| solution_1.c | C | 2021-03-11 Thu 20:34 |
| solution_2.c | C | 2021-03-11 Thu 20:34 |
| solution_3.c | C | 2021-03-11 Thu 20:32 |
