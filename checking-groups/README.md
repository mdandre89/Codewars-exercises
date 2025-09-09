# Checking Groups

 - URL:[https://www.codewars.com/kata/54b80308488cb6cd31000161](https://www.codewars.com/kata/54b80308488cb6cd31000161)
 - Id: 54b80308488cb6cd31000161
 - Language: python
 - Completed on: 2017-05-14T15:16:09.490Z
 - Tags: Algorithms,Data Structures,Strings,Data Types
 - Description:
In English and programming, groups can be made using symbols such as `()` and `{}` that change meaning. However, these groups must be closed in the correct order to maintain correct syntax.

Your job in this kata will be to make a program that checks a string for correct grouping. For instance, the following groups are done correctly:

```
({})
[[]()]
[{()}]
```

The next are done incorrectly:
```
{(})
([]
[])
```

A correct string cannot close groups in the wrong order, open a group but fail to close it, or close a group before it is opened.

Your function will take an input string that may contain any of the symbols `()`, `{}` or `[]` to create groups.

It should return `True` if the string is empty or otherwise grouped correctly, or `False` if it is grouped incorrectly.
