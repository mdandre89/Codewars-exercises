# Remove Duplicates

 - URL:[https://www.codewars.com/kata/53e30ec0116393fe1a00060b](https://www.codewars.com/kata/53e30ec0116393fe1a00060b)
 - Id: 53e30ec0116393fe1a00060b
 - Language: python
 - Completed on: 2017-05-29T13:22:45.069Z
 - Tags: Arrays,Fundamentals
 - Description:
# Remove Duplicates

You are to write a function called `unique` that takes an array of integers and returns the array with duplicates removed. It must return the values in the same order as first seen in the given array. Thus no sorting should be done, if 52 appears before 10 in the given array then it should also be that 52 appears before 10 in the returned array.

## Assumptions

* All values given are integers (they can be positive or negative).
* You are given an array but it may be empty.
* They array may have duplicates or it may not.

## Example

```ruby
puts unique([1, 5, 2, 0, 2, -3, 1, 10]).inspect
[1, 5, 2, 0, -3, 10]

puts unique([]).inspect
[]

puts unique([5, 2, 1, 3]).inspect
[5, 2, 1, 3]
```
```coffeescript
unique([1, 5, 2, 0, 2, -3, 1, 10])
# -> [1, 5, 2, 0, -3, 10]

unique([])
# -> []

unique([5, 2, 1, 3])
# -> [5, 2, 1, 3]
```
```java
UniqueArray.unique([1, 5, 2, 0, 2, -3, 1, 10]) 
// -> [1, 5, 2, 0, -3, 10]
```
```haskell
λ unique [1,5,2,0,2,-3,1,10]
[1,5,2,0,-3,10]
```
```python
print unique([1, 5, 2, 0, 2, -3, 1, 10])
[1, 5, 2, 0, -3, 10]

print unique([])
[]

print unique([5, 2, 1, 3])
[5, 2, 1, 3]
```
