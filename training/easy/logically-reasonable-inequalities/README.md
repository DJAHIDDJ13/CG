# Logically reasonable inequalities \[[link](https://www.codingame.com/training/easy/logically-reasonable-inequalities)\]


 Goal
-----


We are looking at a system of inequalities. Here all inequalities are simple and consist of one variable on each side. Considering a system of strict inequalities, determine whether this system is inherently consistent or if there is a flaw. A flaw is a contradiction of two or more inequalities, e.g. A > B > C > A. This is not possible from a logical point of view.



Input
**Line 1:** a positive integer n  
**The following n lines:** inequalities of format LETTER > LETTER


Output
A string "consistent" if all inequalities are consistent or "contradiction" if there is a contradiction found.


Constraints
0 < n < 26  
LETTER is a single letter in uppercase


Example


Input

```
2
A > B
B > C
```



Output

```
consistent
```





Solutions:
| filename | Language | Submission date |
| --- | --- | --- |
| solution_0.py | Python3 | 2021-03-13 Sat 16:56 |
