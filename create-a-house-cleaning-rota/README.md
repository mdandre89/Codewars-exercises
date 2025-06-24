# Create a House Cleaning Rota

 - URL:[https://www.codewars.com/kata/56c89644b2f1981874000046](https://www.codewars.com/kata/56c89644b2f1981874000046)
 - Id: 56c89644b2f1981874000046
 - Language: python
 - Completed on: 2017-10-23T14:37:42.452Z
 - Tags: Fundamentals
 - Description:
You live in a communal house. Each night, one room's residents are required to clean the dayroom. Your task is to make a random rota for the entire week.

Write a function that takes a list/array of the current occupied rooms in the house, and returns a list of 7 random rooms. If the number of occupied rooms is equal to or bigger than 7, duplicates are not allowed. If the number is less than 7, duplicates are allowed. 

Examples: 

```
rota(["One", "Two", "Three", "Four", "Five", "Six", "Seven"]) 
```
Would output
```
[ 'Three', 'Six', 'Four', 'Five', 'Two', 'One', 'Seven' ]
```
And `rota(["One", "Two", "Three"])` would output 
```
[ 'One', 'Three', 'Two', 'One', 'Two', 'Three', 'One' ]
```
