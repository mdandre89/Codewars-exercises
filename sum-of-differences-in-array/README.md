# Sum of differences in array

 - URL:[https://www.codewars.com/kata/5b73fe9fb3d9776fbf00009e](https://www.codewars.com/kata/5b73fe9fb3d9776fbf00009e)
 - Id: 5b73fe9fb3d9776fbf00009e
 - Language: python
 - Completed on: 2022-06-27T12:31:07.909Z
 - Tags: Arrays,Fundamentals
 - Description:
Your task is to sum the differences between consecutive pairs in the array in descending order.

## Example

```
[2, 1, 10]  -->  9
```

In descending order: `[10, 2, 1]`

Sum: `(10 - 2) + (2 - 1) = 8 + 1 = 9`

If the array is empty or the array has only one element the result should be `0` (`Nothing` in Haskell, `None` in Rust).

~~~if:lambdacalc
#### Encodings

purity: `LetRec`  
numEncoding: `BinaryScott`  
export constructors `nil, cons` for your `List` encoding  
~~~

