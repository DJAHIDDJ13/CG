# The Fastest \[[link](https://www.codingame.com/training/medium/the-fastest)\]

 
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
Your program must judge results of marathon runners and choose the best one.  
   
The result of each runner is represented as HH:MM:SS, where HH is hours, MM is minutes and SS is seconds.  
  
You are given N results and the smallest time is the best.  



**INPUT:**
**Line 1:** a integer number N.  
**Next N lines:** 8 characters, a time result.  

**OUTPUT:**
The best result.  

**CONSTRAINTS:**
0 < N ≤ 10  
0 ≤ hours < 24  
0 ≤ minutes < 60  
0 ≤ seconds < 60  

**EXAMPLE:**


**Input**
4  
10:15:46  
03:59:08  
04:00:08  
03:59:09


**Output**
03:59:08

 


Solutions:
| filename | Language | Submission date |
| --- | --- | --- |
| solution_0.py | Python3 | 2021-03-18 Thu 18:33 |
| solution_1.py | Python3 | 2021-03-18 Thu 18:31 |
