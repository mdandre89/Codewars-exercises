# Fibonacci Rabbits

 - URL:[https://www.codewars.com/kata/5559e4e4bbb3925164000125](https://www.codewars.com/kata/5559e4e4bbb3925164000125)
 - Id: 5559e4e4bbb3925164000125
 - Language: python
 - Completed on: 2017-11-28T09:44:26.736Z
 - Tags: Algorithms
 - Description:
In his publication *Liber Abaci* Leonardo Bonacci, aka Fibonacci, posed a problem involving a population of idealized rabbits. These rabbits bred at a fixed rate, matured over the course of one month, had unlimited resources, and were immortal.

Create a function that determines the number of pairs of mature rabbits after `n` months, beginning with one **immature** pair of these idealized rabbits that produce `b` pairs of offspring at the end of each month.

To illustrate the problem, consider the following example:

    n = 5 months
    b = 3 births
    -> 19 mature rabbit pairs

Month|Immature pairs|Mature pairs  
:---:|:------------:|:----------:  
  0  |       1      |     0  
  1  |       0      |     1  
  2  |       3      |     1  
  3  |       3      |     4  
  4  |      12      |     7  
  5  |      21      |    19  

~~~if:lambdacalc
#### Encodings

purity: `LetRec`  
numEncoding: `Scott`  
~~~

#### Hint

Any Fibonacci number can be computed using the following equation: `F(n) = F(n-1) + F(n-2)`

