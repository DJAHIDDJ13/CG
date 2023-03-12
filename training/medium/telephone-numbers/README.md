# Telephone Numbers \[[link](https://www.codingame.com/training/medium/telephone-numbers)\]
## Problem Description:
Boy, all those telephone numbers are impossible to remember! What if we were to invent a new way to store phone numbers so that they take the least memory space? It is your task today to achieve that hard work. Then call me, maybe ?

<br>
<br>
<u>Topic</u>: storage optimization.<br>
<br>
 


  The Goal
----------


By joining the iDroid smartphone development team, you have been given the responsibility of developing the contact manager. Obviously, what you were not told is that there are strong technical constraints for iDroid: the system doesn’t have much memory and the processor is as fast as a Cyrix from the 90s...  

  

In the specifications, there are two points in particular that catch your attention:  

  

**1. Intelligent Assistance for entering numbers**  

The numbers corresponding to the first digits entered will be displayed to the user almost instantly.  

 
![](https://www.codingame.com/fileservlet?id=250713201118)
  

**2. Number storage optimization**  

First digits which are common to the numbers should not be duplicated in the memory.  

  

Fortunately, the specifications also have this little chart to guide you in the implementation:  

 
![](https://www.codingame.com/fileservlet?id=266985027077)  

Fig 1. Structure of data to stock phone numbers on *iDroid*
  

Your task is to write a program that displays the number of items (which are numbers) required to store a list of telephone numbers with the structure presented above.



  Game Input
------------




Input

Line 1: The number N of telephone numbers.


N following lines: Each line contains a phone number, with a maximum length L. Telephone numbers consist of only the digits 0 to 9 included, without any spaces.






Output
The number of elements (referencing a number) stored in the structure.



Constraints
0 ≤ N ≤ 10000  

2 ≤ L ≤ 20



Examples



Input

```

1
0467123456
```



Output

```

10
```





Input

```

2
0123456789
1123456789
```



Output

```

20
```





Input

```

2
0123456789
0123
```



Output

```

10
```





Input

```

5
0412578440
0412199803
0468892011
112
15
```



Output

```

28
```








Solutions:
| filename | Language | Submission date |
| --- | --- | --- |
| solution_0.py | Python3 | 2023-01-30 Mon 22:17 |
