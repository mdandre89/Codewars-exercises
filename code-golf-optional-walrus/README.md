# [Code Golf] Optional Walrus?

 - URL:[https://www.codewars.com/kata/60a82776de1604000e29eb50](https://www.codewars.com/kata/60a82776de1604000e29eb50)
 - Id: 60a82776de1604000e29eb50
 - Language: python
 - Completed on: 2022-06-25T21:30:30.015Z
 - Tags: Restricted,Puzzles
 - Description:
Re-write the initial function below so that it is `31` characters or less:

```python
def f(iterable, integer):
    length = len(iterable)
    if length > integer:
        return length
    else:
        return 0
```

This simple function takes an input iterable and an integer. If the length of the iterable is larger than the integer it returns that length. Otherwise it returns zero. All inputs will be valid and and all iterables will have a defined length.
