# Parse SQL Queries \[[link](https://www.codingame.com/training/easy/parse-sql-queries)\]


 Goal
-----


Puzzle is meant to be a quick intro to SQL. Nothing too wild.  
  
Your inputs are a basic SQL table and a SELECT query command for each test case. Your program needs to parse these and output the correct query results.  
  
For simplicity there are no commands to manipulate tables and only one table to select from. Nothing more advanced than basic SELECT.  
  
Basic structure of query is as follows:  
SELECT column\_name1, column\_name2 FROM table\_name1  
  
SELECT tells you which columns to keep from the input table for your output table. FROM specifies the name of the table. For this puzzle it won't matter, therefore simply keeping the relevant columns is enough for this query.  
  
SELECT **\*** will select all columns.  
  
Slightly more advanced query:  
SELECT column\_name1, column\_name2 FROM table\_name1 WHERE column\_name1 = 
```
ColumnValue
```
 ORDER BY column\_name2 DESC  
  
WHERE tells you what conditions must be met to display a row. Multiple conditions can be concatenated with AND, OR. Since this is an easy puzzle the only condition you need to check for is if the values are equal.  
  
ORDER BY **value** DESC is the criteria for sorting the table rows. The sorting can be either ascending ASC or descending DESC  
  
NOTE: sort numerical columns by their numerical value and not by their string value.  
  
For more info on SQL syntax:  
https://www.w3schools.com/sql/default.asp  
  
  
Image source: https://unsplash.com/photos/PkbZahEG2Ng



Input
**Line 1:** A string containing the query you need to parse.  
**Line 2:** An integer n for the number of table rows (or entries).  
**Line 3:** A string representing a table header, containing the title of each table column, separated by space.  
**Following n Lines:** A string representing the values for each column, separated by space.


Output
**Line 1:** A string representing the header of the table, containing the selected column titles separated by space.  
**Following Lines:** A string representing the values for each selected column, separated by space.


Constraints
2 ≤ Columns ≤ 10  
2 ≤ N ≤ 30


Example


Input

```
SELECT * FROM cats
3
Name Breed
McFur Peterbald
Squeeky Bambino
Greta Laperm
```



Output

```
Name Breed
McFur Peterbald
Squeeky Bambino
Greta Laperm
```





Solutions:
| filename | Language | Submission date |
| --- | --- | --- |
| solution_0.py | Python3 | 2022-12-18 Sun 05:30 |
