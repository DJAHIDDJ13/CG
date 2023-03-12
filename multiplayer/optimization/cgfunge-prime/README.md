# CGFunge Prime \[[link](https://www.codingame.com/multiplayer/optimization/cgfunge-prime)\]




 
The Goal
===========



 You will be given an integer and have to decide whether it is a prime number or not.   

 But beware, you have to write your program in a slightly modified version of [CG Funge](https://www.codingame.com/training/medium/cgfunge-interpreter) (description below).
   

  

 This is an optimization problem, your program should use as few execution steps as possible to find the correct answer. 
 



 
Rules
========




 CGFunge is a 2-dimensional, positional programming language. This means that execution of a CGFunge program follows a designated pattern on a grid of ASCII characters. Execution always starts on the first character of the first line and proceeds to the right. Each command in the language is a single character. The commands
 are as follow:
   



| Command | Effect |
| --- | --- |
| > | Continue to the right |
| < | Continue to the left |
| ^ | Continue up |
| v | Continue down |
| S | Skip the next character and continue with the subsequent character |
| E | End the program immediately |
| 0-9 | Push a number onto the stack |
| + | Add the first two numbers of the stack (e.g. 43+ results in a 7 on the stack) |
| - | Subtract the first two numbers of the stack (e.g. 43- results in a 1 on the stack) |
| \* | Multiply the first two numbers of the stack (e.g. 43\* results in a 12 on the stack) |
| / | Divide the first two numbers of the stack (e.g. 43/ results in a 1 on the stack) - division will truncate to form an integer |
| P | Pop the top of the stack |
| X | Removes the top value of the stack and takes it as an index. Then removes the value at the index from the stack and push it on top (e.g.: 1X switches the order of the top two stack values) |
| D | Push a duplicate of the top value onto the stack |
| : | Pop the top value of the stack. If it is negative, turn left. If it is positive, turn right. If it is 0, keep the current direction |
| I | Pop the top integer from the stack and print it |
| C | Pop the top integer from the stack and print it as a character (using the ASCII code) |
| " | Toggle string mode. In string mode, every character will push the corresponding ASCII value on the stack |


  

 Any other character will simply be ignored.
 




 
Game Input
=============



Initially the program will hold one single value N on the stack: the number which shall be tested for being prime.


Output

A single line saying PRIME or NOT PRIME
   

 To submit your solution, write a program in any language that prints CGFunge code to stdout. The first line of output should be the lineCount. The next lineCount lines should be the actual program.   

 It is recommended to code in PHP, then you can write CGFunge code directly (you have to delete <?php as well).
 


Constraints

1 ≤ N ≤ 10000  

lineCount ≤ 30   

lineLength ≤ 40   

maximum number of turns ≤ 3000





Solutions:
| filename | Language | Submission date |
| --- | --- | --- |
| solution_0.php | PHP | 2023-01-05 Thu 07:22 |
| solution_1.php | PHP | 2023-01-05 Thu 07:15 |
| solution_2.php | PHP | 2023-01-05 Thu 07:02 |
| solution_3.php | PHP | 2023-01-04 Wed 21:39 |
| solution_4.php | PHP | 2023-01-04 Wed 21:37 |
| solution_5.php | PHP | 2023-01-04 Wed 21:11 |
| solution_6.php | PHP | 2023-01-04 Wed 20:58 |
| solution_7.php | PHP | 2023-01-04 Wed 20:55 |
| solution_8.php | PHP | 2023-01-04 Wed 20:05 |
| solution_9.php | PHP | 2023-01-04 Wed 19:52 |
| solution_10.php | PHP | 2023-01-04 Wed 18:41 |
| solution_11.php | PHP | 2023-01-04 Wed 18:39 |
| solution_12.php | PHP | 2023-01-04 Wed 12:33 |
