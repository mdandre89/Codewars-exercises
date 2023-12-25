# How much will you spend?

 - URL:[https://www.codewars.com/kata/585d7b4685151614190001fd](https://www.codewars.com/kata/585d7b4685151614190001fd)
 - Id: 585d7b4685151614190001fd
 - Language: python
 - Completed on: 2017-03-28T18:23:33.668Z
 - Tags: Mathematics,Algorithms
 - Description:
<h1>How much will you spend?</h1>

Given a dictionary of items and their costs and an array specifying the items bought, calculate the total cost of the items plus a given tax.

If item doesn't exist in the given cost values, the item is ignored.

Output should be rounded to two decimal places.

Python:
```python
costs = {'socks':5, 'shoes':60, 'sweater':30}
get_total(costs, ['socks', 'shoes'], 0.09)
#-> 5+60 = 65
#-> 65 + 0.09 of 65 = 70.85
#-> Output: 70.85
```
