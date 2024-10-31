# Endless String

 - URL:[https://www.codewars.com/kata/57048c1275263af10b00063e](https://www.codewars.com/kata/57048c1275263af10b00063e)
 - Id: 57048c1275263af10b00063e
 - Language: python
 - Completed on: 2017-11-12T20:38:41.172Z
 - Tags: Strings,Fundamentals
 - Description:
Create a function that accepts 3 inputs, a string, a starting location, and a length.  The function needs to simulate the string endlessly repeating in both directions and return a substring beginning at the starting location and continues for length.

Example:
```python
endless_string('xyz', -23, 6) == 'yzxyzx'
```
To visualize:

           Negative                               Positive
    3         2         1         *         1         2         3      
    0987654321098765432109876543210123456789012345678901234567890
    xyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyzx
           ******
         -23 for a length of 6 == 'yzxyzx'
       
Some more examples:
```python
endless_string('xyz', 0, 4) == 'xyzx'
endless_string('xyz', 19, 2) == 'yz'
endless_string('xyz', -4, -4) == 'zxyz'
```

A negative length needs to include the starting position and return the characters to the left of the starting position.
