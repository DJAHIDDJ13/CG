# Genome Sequencing \[[link](https://www.codingame.com/training/hard/genome-sequencing)\]
## Problem Description:
Guanine, Thymine, Cytosine... You might have heard of those things in biology class, but forgot them on the spot. Don't worry, we all have. The goal of this exercise is to find how to combine chains of nucleotides (sorry, <i>characters</i>) in a way in which they take the least possible room.<br>
<br>
<u>Topic</u> : Pattern recognition.<br>
<br>
 


  The Goal
----------


You are working as a computer scientist in a laboratory seeking to sequence the genome. A DNA sequence is represented by a character string (of A, C, T and G) such as GATTACA. The problem is that biologists are only able to extract sub-sequences of the complete sequence. Your role is to combine these partial sub-sequences to recover the original sequence.  

  

In this exercise you are asked to calculate the length of the shortest sequence that contains all the sub-sequences of the input data.



  Rules
-------



You are given N sub-sequences and you must return the length of the shortest sequence that contains all the sub-sequences. There may be several sequences of the same minimum length and which fit the requirement. We are not asking you to list these, but only to return their length.  

  

Note that there is always a solution. One can indeed simply concatenate all the sub-sequences to obtain a valid sequence. But by nesting (even partially) the sub-sequences, it is generally possible to obtain a shorter sequence (see the example).




  Example
---------


For example, you have three sub-sequences AGATTA, GATTACA, and TACAGA. The sequence AGATTACAGA is the shortest sequence that contains all the sub-sequences.  

  

Note that in this example, there are other sequences which contain all of the sub-sequences such as TACAGATTACAGATTA.. However, we prefer the former because it is shorter (10 characters instead of 16).

![](https://www.codingame.com/fileservlet?id=215473947480)

Example
AGATTACAGA contains the sub-sequences AGATTA, GATTACA, and TACAGA.


 
 
 
 




  Game Input
------------




Input

Line 1: The number N of sub-sequences


N following lines: one sub-sequence by line, represented by a string of characters from A, C, T and G. Each sub-sequence ranges from 1 to maximum 10 characters long.






Output
The length of the shortest sequence containing all the sub-sequences.



Constraints
0 < N < 6



Examples



Input

```

2
AAC
CCTT
```



Output

```

6
```





Input

```

3
AGATTA
GATTACA
TACAGA
```



Output

```

10
```





Input

```

3
TT
AA
ACT
```



Output

```

5
```








Solutions:
| filename | Language | Submission date |
| --- | --- | --- |
| solution_0.py | Python3 | 2021-03-17 Wed 14:08 |
| solution_1.py | Python3 | 2021-03-17 Wed 14:07 |
