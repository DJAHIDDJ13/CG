# Rectangular block spinner \[[link](https://www.codingame.com/training/easy/rectangular-block-spinner)\]


 Goal
-----


You have to rotate sizeXsize block counterclockwise by an angle angle. The block is filled with single ASCII characters. Angle is provided in degrees and is an odd multiple of 45. The output will always have a diamond shape.



Input
Line 1: Size of the block, size.  
Line 2: Angle angle.  
size following lines: Content of the block. ASCII characters are separated with spaces.


Output
Rotated block with spaces on both ends.


Constraints
2 =< size <= 100   
45 =< angle <= 2295   
angle % 90 == 45 (Dimond shape)


Example


Input

```
5
45
# # # # #
# - . . #
# # - . #
# # # - #
# # # # #
```



Output

```
    #    
   # #   
  # . #  
 # . . # 
# - - - #
 # # # # 
  # # #  
   # #   
    #    

```





Solutions:
| filename | Language | Submission date |
| --- | --- | --- |
| solution_0.py | Python3 | 2023-01-31 Tue 14:23 |
