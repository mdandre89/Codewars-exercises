# Triangle of Multiples (Easy One)

 - URL:[https://www.codewars.com/kata/58ecc0a8342ee5e920000115](https://www.codewars.com/kata/58ecc0a8342ee5e920000115)
 - Id: 58ecc0a8342ee5e920000115
 - Language: python
 - Completed on: 2017-11-07T16:30:15.081Z
 - Tags: Mathematics,Data Structures,Fundamentals
 - Description:
See the following triangle:
```
____________________________________
 1                                      
 2   4   2                              
 3   6   9   6   3                      
 4   8   12  16  12  8   4             
 5   10  15  20  25  20  15  10  5   
 ___________________________________
 
```
The <b>total sum</b> of the numbers in the triangle, up to the 5th line included, is ```225```, part of it, ```144```, corresponds to the total <b>sum of the even terms</b> and ```81``` to the <b>total sum of the odd terms</b>.

Create a function that may output an array with three results for each value of n.
```groovy
Kata.triangMult(n)  ----> [total_sum, total_even_sum, total_odd_sum]
```
```haskell
triangMult n  ----> (total_sum, total_even_sum, total_odd_sum)
```
```python
triang_mult(n)  ----> [total_sum, total_even_sum, total_odd_sum]
```
```javascript
triang_mult(n)  ----> [total_sum, total_even_sum, total_odd_sum]
```
```ruby
triang_mult(n)  ----> [total_sum, total_even_sum, total_odd_sum]
```
Our example will be:
```groovy
Kata.triangMult(5) ----> [225, 144, 81]
```
```haskell
triangMult 5 ----> (225, 144, 81)
```
```ruby
triang_mult(5) ----> [225, 144, 81]
```
```python
triang_mult(5) ----> [225, 144, 81]
```
```javascript
triang_mult(5) ----> [225, 144, 81]
```

Features of the random tests:
```
number of tests = 100
49 < n < 5000
```
Enjoy it!
This kata will be translated in another languages soon
