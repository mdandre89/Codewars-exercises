# [Code Golf] Get the Square of a Number without ** or * or pow()

 - URL:[https://www.codewars.com/kata/58a8807c5336a3f613000157](https://www.codewars.com/kata/58a8807c5336a3f613000157)
 - Id: 58a8807c5336a3f613000157
 - Language: python
 - Completed on: 2022-06-12T20:09:29.185Z
 - Tags: Mathematics,Restricted,Puzzles
 - Description:
# Task
Write a function that gets a square of a number without the following:

* Your code mustn't contain any `*`s and you cannot use the `pow` function. **Edit: You also cannot use **`__mul__ / imul`** function**
* You cannot import any external libraries (unless you are satisfied with `random` being pre-imported).
* Only one function can be defined.
* Loophole solutions will not be accepted (see below).
* If I use `test.expect` in my restriction tests, **that is okay.** This is not an issue.
* Input will always be positive or 0
* The code has a length limit:
~~~if:python
Your code must be under or equal to **50 characters** (and you already have to use 6 for the function name).
~~~
~~~if:javascript
Your code must be under or equal to **25 characters** (and you already have to use 6 for the function name).
~~~

Example of a loophole solution:

```python
square=lambda n:eval(')2,n(wop'[::-1])
```
