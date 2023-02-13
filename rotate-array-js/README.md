# Rotate Array (JS)

 - URL:[https://www.codewars.com/kata/54f8b0c7a58bce9db6000dc4](https://www.codewars.com/kata/54f8b0c7a58bce9db6000dc4)
 - Id: 54f8b0c7a58bce9db6000dc4
 - Language: python
 - Completed on: 2017-09-13T09:40:29.078Z
 - Tags: Arrays,Algorithms
 - Description:
> 
**Note**: This kata is a translation of this (Java) one: http://www.codewars.com/kata/rotate-array. I have not translated this first one as usual because I did not solved it, and I fear not being able to solve it (Java is **not** my cup of... tea). @cjmcgraw, if you want to use my translation on your kata feel free to use it.


Create a function named "rotate" that takes an array and returns a new one with the elements inside rotated n spaces.

If n is greater than 0 it should rotate the array to the right. If n is less than 0 it should rotate the array to the left. If n is 0, then it should return the array unchanged.

Example:
```javascript
var data = [1, 2, 3, 4, 5];

rotate(data, 1) // => [5, 1, 2, 3, 4]
rotate(data, 2) // => [4, 5, 1, 2, 3]
rotate(data, 3) // => [3, 4, 5, 1, 2]
rotate(data, 4) // => [2, 3, 4, 5, 1]
rotate(data, 5) // => [1, 2, 3, 4, 5]

rotate(data, 0) // => [1, 2, 3, 4, 5]

rotate(data, -1) // => [2, 3, 4, 5, 1]
rotate(data, -2) // => [3, 4, 5, 1, 2]
rotate(data, -3) // => [4, 5, 1, 2, 3]
rotate(data, -4) // => [5, 1, 2, 3, 4]
rotate(data, -5) // => [1, 2, 3, 4, 5]
```
```csharp
var data = new object[] { 1, 2, 3, 4, 5 };

Kata.Rotate(data, 1); // => [5, 1, 2, 3, 4]
Kata.Rotate(data, 2); // => [4, 5, 1, 2, 3]
Kata.Rotate(data, 3); // => [3, 4, 5, 1, 2]
Kata.Rotate(data, 4); // => [2, 3, 4, 5, 1]
Kata.Rotate(data, 5); // => [1, 2, 3, 4, 5]

Kata.Rotate(data, 0); // => [1, 2, 3, 4, 5]

Kata.Rotate(data, -1); // => [2, 3, 4, 5, 1]
Kata.Rotate(data, -2); // => [3, 4, 5, 1, 2]
Kata.Rotate(data, -3); // => [4, 5, 1, 2, 3]
Kata.Rotate(data, -4); // => [5, 1, 2, 3, 4]
Kata.Rotate(data, -5); // => [1, 2, 3, 4, 5]
```
```coffeescript
data = [1, 2, 3, 4, 5]

rotate(data, 1) # => [5, 1, 2, 3, 4]
rotate(data, 2) # => [4, 5, 1, 2, 3]
rotate(data, 3) # => [3, 4, 5, 1, 2]
rotate(data, 4) # => [2, 3, 4, 5, 1]
rotate(data, 5) # => [1, 2, 3, 4, 5]

rotate(data, 0) # => [1, 2, 3, 4, 5]

rotate(data, -1) # => [2, 3, 4, 5, 1]
rotate(data, -2) # => [3, 4, 5, 1, 2]
rotate(data, -3) # => [4, 5, 1, 2, 3]
rotate(data, -4) # => [5, 1, 2, 3, 4]
rotate(data, -5) # => [1, 2, 3, 4, 5]
```
```python
data = [1, 2, 3, 4, 5];

rotate(data, 1) # => [5, 1, 2, 3, 4]
rotate(data, 2) # => [4, 5, 1, 2, 3]
rotate(data, 3) # => [3, 4, 5, 1, 2]
rotate(data, 4) # => [2, 3, 4, 5, 1]
rotate(data, 5) # => [1, 2, 3, 4, 5]

rotate(data, 0) # => [1, 2, 3, 4, 5]

rotate(data, -1) # => [2, 3, 4, 5, 1]
rotate(data, -2) # => [3, 4, 5, 1, 2]
rotate(data, -3) # => [4, 5, 1, 2, 3]
rotate(data, -4) # => [5, 1, 2, 3, 4]
rotate(data, -5) # => [1, 2, 3, 4, 5]
```
```haskell
data = [1, 2, 3, 4, 5]

rotate 1 data -- => [5, 1, 2, 3, 4]
rotate 2 data -- => [4, 5, 1, 2, 3]
rotate 3 data -- => [3, 4, 5, 1, 2]
rotate 4 data -- => [2, 3, 4, 5, 1]
rotate 5 data -- => [1, 2, 3, 4, 5]

rotate 0 data -- => [1, 2, 3, 4, 5]

rotate -1 data -- => [2, 3, 4, 5, 1]
rotate -2 data -- => [3, 4, 5, 1, 2]
rotate -3 data -- => [4, 5, 1, 2, 3]
rotate -4 data -- => [5, 1, 2, 3, 4]
rotate -5 data -- => [1, 2, 3, 4, 5]
```


Furthermore the method should take ANY array of objects and perform this operation on them:
```javascript
rotate(['a', 'b', 'c'], 1)     // => ['c', 'a', 'b']
rotate([1.0, 2.0, 3.0], 1)     // => [3.0, 1.0, 2.0]
rotate([true, true, false], 1) // => [false, true, true]
```
```csharp
Kata.Rotate(new object[] { 'a', 'b', 'c' }, 1);     // => ['c', 'a', 'b']
Kata.Rotate(new object[] { 1.0, 2.0, 3.0 }, 1);     // => [3.0, 1.0, 2.0]
Kata.Rotate(new object[] { true, true, false }, 1); // => [false, true, true]
```
```coffeescript
rotate(['a', 'b', 'c'], 1)     # => ['c', 'a', 'b']
rotate([1.0, 2.0, 3.0], 1)     # => [3.0, 1.0, 2.0]
rotate([true, true, false], 1) # => [false, true, true]
```
```python
rotate(['a', 'b', 'c'], 1)     # => ['c', 'a', 'b']
rotate([1.0, 2.0, 3.0], 1)     # => [3.0, 1.0, 2.0]
rotate([True, True, False], 1) # => [False, True, True]
```
```haskell
rotate 1 ['a', 'b', 'c']         -- => ['c', 'a', 'b']
rotate 1 [1.0, 2.0, 3.0] 1       -- => [3.0, 1.0, 2.0]
rotate 1 [True, True, False]     -- => [False, True, True]
rotate 1 ["one", "two", "three"] -- => ["three", "one", "two"]
```

Finally the rotation shouldn't be limited by the indices available in the array. Meaning that if we exceed the indices of the array it keeps rotating.

Example:
```javascript
var data = [1, 2, 3, 4, 5]

rotate(data, 7)     // => [4, 5, 1, 2, 3]
rotate(data, 11)    // => [5, 1, 2, 3, 4]
rotate(data, 12478) // => [3, 4, 5, 1, 2]
```
```csharp
var data = new object[] { 1, 2, 3, 4, 5 };

Kata.Rotate(data, 7);     // => [4, 5, 1, 2, 3]
Kata.Rotate(data, 11);    // => [5, 1, 2, 3, 4]
Kata.Rotate(data, 12478); // => [3, 4, 5, 1, 2]
```
```coffeescript
data = [1, 2, 3, 4, 5]

rotate(data, 7)     # => [4, 5, 1, 2, 3]
rotate(data, 11)    # => [5, 1, 2, 3, 4]
rotate(data, 12478) # => [3, 4, 5, 1, 2]
```
```python
data = [1, 2, 3, 4, 5]

rotate(data, 7)     # => [4, 5, 1, 2, 3]
rotate(data, 11)    # => [5, 1, 2, 3, 4]
rotate(data, 12478) # => [3, 4, 5, 1, 2]
```
```haskell
data = [1, 2, 3, 4, 5]

rotate 7 data      -- => [4, 5, 1, 2, 3]
rotate 11 data     -- => [5, 1, 2, 3, 4]
rotate 12478 data  -- => [3, 4, 5, 1, 2]
```

