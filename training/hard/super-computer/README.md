# Super Computer \[[link](https://www.codingame.com/training/hard/super-computer)\]
## Problem Description:
Your university research departement recently acquired a brand new, shiny super computer. Problem is, everyone wants to use it. Some dude at the chemistry lab wants to run a one week experiment, your colleague Martin needs it for a "real quick try, I promise", etc... It's not going to be easy to have everyone satisfied with the planning.<br />
Your task will be to schedule the different experiments running on the computer so that as many experiments as possible can be run.<br>
<br>
<u>Topic</u> : Scheduling.<br>
<br>
 


  The Goal
----------


In the Computer2000 data center, you are responsible for planning the usage of a supercomputer for scientists. ​Therefore you've decided to organize things a bit by planning everybody’s tasks. The logic is simple: the higher the number of calculations which can be performed, the more people you can satisfy.



  Rules
-------



Scientists give you the starting day of their calculation and the number of consecutive days they need to reserve the calculator.  

  

For example:
 



| Calculation | Starting Day | Duration |
| --- | --- | --- |
| A | 2 | 5 |
| B | 9 | 7 |
| C | 15 | 6 |
| D | 9 | 3 |




Calculation A starts on day 2 and ends on day 6


Calculation B starts on day 9 and ends on day 15


Calculation starts on day 15 and ends on day 20


Calculation D starts on day 9 and ends on day 11




In this example, it’s not possible to carry out all the calculations because the periods for B and C overlap. 3 calculations maximum can be carried out: A, D and C.




  Game Input
------------




Input

Line 1: The number N of calculations


The N following lines: on each line, the starting day J and the duration D of reservation, separated by a blank space.






Output
The maximum number of calculations that can be carried out.



Constraints
0 < N < 100000  

0 < J < 1000000  

0 < D < 1000



Examples



Input

```

4
2 5
9 7
15 6
9 3
```



Output

```

3
```





Input

```

5
3 5
9 2
24 5
16 9
11 6
```



Output

```

4
```








Solutions:
| filename | Language | Submission date |
| --- | --- | --- |
| solution_0.c | C | 2023-01-18 Wed 15:06 |
| solution_1.py | Python3 | 2023-01-18 Wed 15:03 |
| solution_2.py | Python3 | 2023-01-18 Wed 15:03 |
| solution_3.rb | Ruby | 2023-01-18 Wed 15:03 |
