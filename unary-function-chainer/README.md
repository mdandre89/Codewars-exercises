# Unary function chainer

 - URL:[https://www.codewars.com/kata/54ca3e777120b56cb6000710](https://www.codewars.com/kata/54ca3e777120b56cb6000710)
 - Id: 54ca3e777120b56cb6000710
 - Language: python
 - Completed on: 2017-11-29T10:36:55.401Z
 - Tags: Functional Programming,Fundamentals
 - Description:
Your task is to write a higher order function for chaining together
a list of unary functions. In other words, it should return a function
that does a left fold on the given functions.

```python
chained([a,b,c,d])(input)
```
Should yield the same result as
```python
d(c(b(a(input))))
```
