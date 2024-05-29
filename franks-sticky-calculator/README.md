# Frank's Sticky Calculator 

 - URL:[https://www.codewars.com/kata/5900750cb7c6172207000054](https://www.codewars.com/kata/5900750cb7c6172207000054)
 - Id: 5900750cb7c6172207000054
 - Language: python
 - Completed on: 2017-05-20T18:21:33.659Z
 - Tags: Strings,Fundamentals
 - Description:
Frank just bought a new calculator.
But, this is no normal calculator. 
This is a **'Sticky Calculator**.

Whenever you add add, subtract, multiply or divide two numbers the two numbers first stick together: 

For instance: 
```javascript
50 + 12 becomes 5012
```
and then the operation is carried out as usual: 
```javascript
(5012) + 12 = 5024
```

## Task

It is your job to create a function which takes 3 parameters:
```javascript
stickyCalc(operation, val1, val2)
```
which works just like Frank's sticky calculator

## Some Examples

```javascript
stickyCalc('+', 50, 12)     // Output: (5012 + 12) = 5024
stickyCalc('-', 7, 5)       // Output: (75 - 5) = 70
stickyCalc('*', 13, 20)     // Output: (1320 * 20 ) = 26400
stickyCalc('/', 10, 10)     // Output: (1010 / 10) = 101
```

## Note


* The calculator only works for positive integers only.
* The calculator rounds any non-integer before operating.
* The calculator rounds any output to nearest integer.
 
For example: 

```javascript
stickyCalc('/', 12.1, 6.8), 18);   
```

12.1 and 6.8 are rounded to 12 and 7 respectively & they 'stick together' to make 127. <br><br>

Although 127 / 7 = 18.1428 ; 18 is outputted instead. 






