# Rugby score \[[link](https://www.codingame.com/training/easy/rugby-score)\]


 Goal
-----


Given a rugby score, your program must compute the different scoring combinations that lead to that particular score.  
As a reminder:  
 - a try is worth 5 points  
 - after a try, a transformation kick is played and is worth 2 extra points if successful  
 - penalty kicks and drops are worth 3 points



Input
**Line 1**: the score


Output
**N lines**: number of tries, number of transformations, number of penalties / drops, separated by spaces  
The combinations must be ordered by increasing order of tries, then transformations, then penalties/drops


Constraints
No impossible scores are given, there is always at least one valid combination.


Example


Input

```
12
```



Output

```
0 0 4
2 1 0
```





Solutions:
| filename | Language | Submission date |
| --- | --- | --- |
| solution_0.py | Python3 | 2021-03-12 Fri 23:25 |
