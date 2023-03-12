# Unary - Code Golf \[[link](https://www.codingame.com/multiplayer/codegolf/chuck-norris-codesize)\]
## Problem Description:
Default description.
 



  The Goal
----------



Binary with 0 and 1 is good, but binary with only 0, or almost, is even better!


Write a program that takes an incoming message as input and displays as output the message encoded using this method.






  Rules
-------




Here is the encoding principle:


* The input message consists of ASCII characters (7-bit)
* The encoded output message consists of blocks of 0
* A block is separated from another block by a space
* Two consecutive blocks are used to produce a series of same value bits (only 1 or 0 values):
 - First block: it is always 0 or 00. If it is 0, then the series contains 1, if not, it contains 0  
- Second block: the number of 0 in this block is the number of bits in the series







  Example
---------



Let’s take a simple example with a message which consists of only one character: Capital C. C in binary is represented as 1000011, so with the unary method, this gives:


* 0 0 (the first series consists of only a single 1)
* 00 0000 (the second series consists of four 0)
* 0 00 (the third consists of two 1)


So C is coded as: 0 0 00 0000 0 00



  
 Second example, we want to encode the message CC (i.e. the 14 bits 10000111000011) :


* 0 0 (one single 1)
* 00 0000 (four 0)
* 0 000 (three 1)
* 00 0000 (four 0)
* 0 00 (two 1)


So CC is coded as: 0 0 00 0000 0 000 00 0000 0 00







  Game Input
------------




Input
Line 1: the message consisting of N ASCII characters (without carriage return)



Output
The encoded message



Constraints
0 < N < 100



Example



Input

```
C
```



Output

```
0 0 00 0000 0 00
```







Solutions:
| filename | Language | Submission date |
| --- | --- | --- |
| solution_0.py | Python3 | 2022-06-14 Tue 21:34 |
| solution_1.py | Python3 | 2022-06-14 Tue 21:33 |
| solution_2.py | Python3 | 2022-06-14 Tue 21:32 |
| solution_3.rb | Ruby | 2021-07-31 Sat 04:01 |
| solution_4.rb | Ruby | 2021-07-31 Sat 03:58 |
| solution_5.rb | Ruby | 2021-07-31 Sat 03:53 |
| solution_6.pl | Perl | 2021-07-23 Fri 00:45 |
| solution_7.rb | Ruby | 2021-05-27 Thu 12:57 |
| solution_8.c | C | 2021-04-01 Thu 00:38 |
| solution_9.rb | Ruby | 2021-03-21 Sun 20:23 |
| solution_10.c | C | 2021-03-21 Sun 16:03 |
| solution_11.c | C | 2021-03-21 Sun 00:23 |
| solution_12.c | C | 2021-03-19 Fri 00:58 |
| solution_13.py | Python3 | 2021-03-16 Tue 16:41 |
| solution_14.py | Python3 | 2021-03-16 Tue 16:35 |
| solution_15.py | Python3 | 2021-03-16 Tue 16:33 |
| solution_16.py | Python3 | 2021-03-16 Tue 16:27 |
| solution_17.py | Python3 | 2021-03-15 Mon 22:08 |
| solution_18.rb | Ruby | 2019-06-01 Sat 22:26 |
| solution_19.py | Python3 | 2019-06-01 Sat 22:04 |
