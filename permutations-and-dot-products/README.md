# Permutations and Dot Products

 - URL:[https://www.codewars.com/kata/5457ea88aed18536fc000a2c](https://www.codewars.com/kata/5457ea88aed18536fc000a2c)
 - Id: 5457ea88aed18536fc000a2c
 - Language: python
 - Completed on: 2022-06-14T14:26:47.838Z
 - Tags: Linear Algebra,Mathematics,Algorithms
 - Description:
### Task
The __dot product__ is usually encountered in linear algebra or scientific computing. It's also called __scalar product__ or __inner product__ sometimes:

> In mathematics, the __dot product__, or __scalar product__ (or sometimes __inner product__ in the context of Euclidean space), is an algebraic operation that takes two equal-length sequences of numbers (usually coordinate vectors) and returns a single number. <cite>[Wikipedia](https://en.wikipedia.org/w/index.php?title=Dot_product&oldid=629717691)</cite>

In our case, we define the dot product algebraically for two vectors `a = [a1, a2, …, an]`, `b = [b1, b2, …, bn]` as 
    
    dot a b = a1 * b1 + a2 * b2 + … + an * bn.
Your task is to find permutations of `a` and `b`, such that `dot a b` is minimal, and return that value. For example, the dot product of `[1,2,3]` and `[4,0,1]` is minimal if we switch `0` and `1` in the second vector.

### Examples
```haskell
minDot [1,2,3,4,5] [0,1,1,1,0]  = 6
minDot [1,2,3,4,5] [0,0,1,1,-4] = -17
minDot [1,3,5]     [4,-2,1]     = -3
```
```javascript
minDot( [1,2,3,4,5], [0,1,1,1,0] ) = 6
minDot( [1,2,3,4,5], [0,0,1,1,-4]) = -17
minDot( [1,3,5]    , [4,-2,1]    ) = -3
```
```python
min_dot([1,2,3,4,5], [0,1,1,1,0] ) = 6
min_dot([1,2,3,4,5], [0,0,1,1,-4]) = -17
min_dot([1,3,5]    , [4,-2,1]    ) = -3
```
```clojure
(minDot [1 2 3 4 5] [0 1 1 1 0]) ; returns 6
(minDot [1 2 3 4 5] [0 0 1 1 -4]) ; returns -17
(minDot [1 3 5]     [4 -2 1]) ; returns -3
```
```ruby
min_dot([1,2,3,4,5], [0,1,1,1,0] ) = 6
min_dot([1,2,3,4,5], [0,0,1,1,-4]) = -17
min_dot([1,3,5]    , [4,-2,1]    ) = -3
```

### Remarks
If the list or array is empty, `minDot` should return 0. All arrays or lists will have the same length. Also, for the dynamically typed languages, all inputs will be valid lists or arrays, you don't need to check for `undefined`, `null` etc.

Note: This kata is inspired by [GCJ 2008](https://code.google.com/codejam/contest/32016/dashboard#s=p0).
