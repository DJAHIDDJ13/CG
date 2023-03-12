# Gold Packing \[[link](https://www.codingame.com/training/easy/gold-packing)\]


 Goal
-----


You are packing n gold bars of uniform height and width but variable length into a box of length m with the same height and width. Find the set of gold bars that use up the most space in the box.  
If there are multiple such sets, choose the one with the fewest number of bars.  
If there still are multiple such sets, try to minimize the first bar, then the second bar, and so on.



Input
**Line 1 :** An integer m for the length of the box.  
**Line 2 :** An integer n for the number of gold bars.  
**Line 3 :** n space-separated integers for the lengths of the gold bars, sorted from shortest to longest.


Output
The lengths of gold bars separated by a space and sorted from shortest to longest.


Constraints
0 < m <= 2000  
0 < n <= 20


Example


Input

```
7
5
5 6 7 8 9
```



Output

```
7
```





Solutions:
| filename | Language | Submission date |
| --- | --- | --- |
| solution_0.py | Python3 | 2021-03-13 Sat 00:19 |
| solution_1.py | Python3 | 2021-03-13 Sat 00:17 |
| solution_2.py | Python3 | 2021-03-13 Sat 00:17 |
