# Range Parser

 - URL:[https://www.codewars.com/kata/57d307fb9d84633c5100007a](https://www.codewars.com/kata/57d307fb9d84633c5100007a)
 - Id: 57d307fb9d84633c5100007a
 - Language: python
 - Completed on: 2018-02-04T14:17:48.895Z
 - Tags: Algorithms,Parsers,Strings,Fundamentals
 - Description:
In this Kata you are to implement a function that parses a string which is composed from tokens of the form 'n1-n2,n3,n4-n5:n6' where 'nX' is a positive integer. Each token represent a different range:

'n1-n2' represents the range n1 to n2 (inclusive in both ends).
'n3' represents the single integer n3.
'n4-n5:n6' represents the range n4 to n5 (inclusive in both ends) but only includes every other n6 integer.

Notes:<br/>
1. The input string doesn't not have to include all the token types.<br/>
2. All integers are assumed to be positive.<br/>
3. Tokens may be separated by `','`, `', '` or ` , `.

Some examples:

'1-10,14, 20-25:2' -> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 14, 20, 22, 24]

'5-10' -> [5, 6, 7, 8, 9, 10]

'2' -> [2]

The output should be a list of integers.
