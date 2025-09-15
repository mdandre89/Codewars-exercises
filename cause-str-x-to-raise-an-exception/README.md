# Cause str(x) to raise an exception

 - URL:[https://www.codewars.com/kata/5ae786ad68e644e861000075](https://www.codewars.com/kata/5ae786ad68e644e861000075)
 - Id: 5ae786ad68e644e861000075
 - Language: python
 - Completed on: 2022-06-25T21:14:30.863Z
 - Tags: Strings,Puzzles
 - Description:
My 7th kata, a Python puzzle, define `x` such that `str(x)` raises an exception.

Note that `str()` calls rarely raise an exception, for example:

    print(str(1))
    #1
    print(str(sum))
    #<built-in function sum>
    print(str(i for i in range(2)))
    #<generator object <genexpr> at 0x7f5c0b54e798>
    import sys
    print(str(sys))
    #<module 'sys' (built-in)>

You cannot simply define a custom class and overide `__str__` (actually it is possible, but I've forbiden the easiest ways), or redefine `str`, but there are multiple other solutions.
