# Nuggets numbers \[[link](https://www.codingame.com/training/hard/nuggets-numbers)\]


 Goal
-----


A restaurant sells portions of chicken nuggets in boxes. As a tricky client you want to puzzle the waiter by asking the impossible : find the highest number of nuggets that they cannot serve you.  
  
For example, if the restaurant sells boxes of 2 or 5 portions of nuggets, the waiter cannot serve you 1 or 3 portions but they can serve you every other quantity, so the answer should be 3.  
  
If the restaurant sells boxes of 6 or 8 portions however, the waiter cannot serve you any odd number of portions and there is no maximum (=Infinity), so the answer should be -1.



Input
**Line 1 :** The number N of boxes the restaurant serves.  
**N lines :** The number P of nuggets in each box.


Output
The maximal number of nuggets that is impossible to get, -1 if there is no maximum (=Infinity).


Constraints
1<N<20  
2<P<2000


Example


Input

```
2
2
5

```



Output

```
3
```





Solutions:
| filename | Language | Submission date |
| --- | --- | --- |
| solution_0.py | Python3 | 2021-05-16 Sun 07:54 |
| solution_1.rb | Ruby | 2021-05-16 Sun 07:31 |
