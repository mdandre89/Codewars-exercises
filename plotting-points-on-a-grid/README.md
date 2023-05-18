# Plotting points on a grid.

 - URL:[https://www.codewars.com/kata/587ac5616d360f6bed000088](https://www.codewars.com/kata/587ac5616d360f6bed000088)
 - Id: 587ac5616d360f6bed000088
 - Language: python
 - Completed on: 2022-06-13T14:21:52.860Z
 - Tags: Strings,Basic Language Features,Language Features,ASCII Art,Puzzles
 - Description:
Make a class Grid which accepts two arguments, `width` and `height` and makes a multiline string containing something like this:

```
width=10
height=10
0000000000
0000000000
0000000000
0000000000
0000000000
0000000000
0000000000
0000000000
0000000000
0000000000
```


It has a function `plot_point` which plots an `X` on the grid. It accepts two arguments, x and y. x and y should be 1-based.


```
x = 5
y = 3
0000000000
0000000000
0000X00000
0000000000
0000000000
0000000000
0000000000
0000000000
0000000000
0000000000
```


It also has an attribute `grid` which contains the multiline string. Your job is to create a class `Grid` which does that.
