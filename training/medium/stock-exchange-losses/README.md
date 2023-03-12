# Stock Exchange Losses \[[link](https://www.codingame.com/training/medium/stock-exchange-losses)\]
## Problem Description:
You sometimes have to take risks buying market shares, and sometimes you have to know when it's time to sell before you lose everything. This is why we propose a little puzzle, to write a program that will do the maths for us, a program in which we can invest all our trust (and money?!).<br>
Don't worry, you won't have to be a market expert, nothing is going to crash.
<br>
<br>
<u>Topic</u> : Search through a set of values.<br>
<br>
 


  The Goal
----------


A finance company is carrying out a study on the worst stock investments and would like to acquire a program to do so. The program must be able to analyze a chronological series of stock values in order to show the largest loss that it is possible to make by buying a share at a given time t0 and by selling it at a later date t1. The loss will be expressed as the difference in value between t0 and t1. If there is no loss, the loss will be worth 0.



  Game Input
------------




Input

Line 1: the number n of stock values available.


Line 2: the stock values arranged in order, from the date of their introduction on the stock market v1 until the last known value vn. The values are integers.






Output
The maximal loss p, expressed negatively if there is a loss, otherwise 0.



Constraints
0 < n < 100000  

0 < v < 231



Examples


![](https://www.codingame.com/fileservlet?id=43114364027)

Input

```

6
3 2 4 2 1 5
```



Output

```

-3
```




![](https://www.codingame.com/fileservlet?id=43127740838)

Input

```

6
5 3 4 2 3 1
```



Output

```

-4
```




![](https://www.codingame.com/fileservlet?id=43130710003)

Input

```

5
1 2 4 4 5
```



Output

```

0
```








Solutions:
| filename | Language | Submission date |
| --- | --- | --- |
| solution_0.py | Python3 | 2017-12-12 Tue 10:36 |
