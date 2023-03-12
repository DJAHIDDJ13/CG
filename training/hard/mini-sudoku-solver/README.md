# Mini sudoku solver \[[link](https://www.codingame.com/training/hard/mini-sudoku-solver)\]

 
.statement\_wrapping\_div, .statement {font-size: 14px;font-weight: 400;} 
.statement\_wrapping\_div {margin-bottom: 10px;}
.statement\_wrapping\_div ul {padding-left: 40px;}
.statement {background-color:rgba(255, 255, 255, 0.85);padding: 20px;padding-top:0px;}
code, span.const {display:inline-block;font-family:Inconsolata,consolas,monospace;padding-left:5px;padding-right:5px;padding-top:1px;padding-bottom:1px;background-color:#18a1ea;white-space: nowrap;margin-right:2px;color: white;}
span.var {display: inline-block;padding-left:5px;padding-right:5px;padding-top:1px;padding-bottom:2px;background-color:#f2dd00;white-space:nowrap;margin-left:1px;margin-right:2px;color:black;}
.stat\_mid\_title {font-weight:700;margin-bottom:5px;}
.protocol\_title{color:#ffd200;}
.cross-statementBlock{position:relative;}
The program:
You must write a program that solves a 4×4 sudoku grid that have only one solution.  
A solved sudoku is a latin square for which each 2×2 corner square must also contain all the digits 1 to 4.  



**INPUT:**
You are given a 4×4 grid, the empty cells are represented by 0. For example:  
2000  
0130  
3001  
0240  

**OUTPUT:**
The output must be the only solution, all the zeros must be filled by the correct digits.  
Here:  
2314  
4132  
3421  
1243  

**CONSTRAINTS:**
There are six hints or more.  

**EXAMPLE:**


**Input**
2043  
0020  
4300  
0034


**Output**
2143  
3421  
4312  
1234

 


Solutions:
| filename | Language | Submission date |
| --- | --- | --- |
| solution_0.py | Python3 | 2021-05-25 Tue 07:42 |
