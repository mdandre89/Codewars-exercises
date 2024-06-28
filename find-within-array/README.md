# Find within array

 - URL:[https://www.codewars.com/kata/51f082ba7297b8f07f000001](https://www.codewars.com/kata/51f082ba7297b8f07f000001)
 - Id: 51f082ba7297b8f07f000001
 - Language: python
 - Completed on: 2022-06-12T18:23:03.559Z
 - Tags: Arrays,Functional Programming,Fundamentals
 - Description:
We'll create a function that takes in two parameters:

* a sequence (length and types of items are irrelevant)
* a function (value, index) that will be called on members of the sequence and their index. The function will return either true or false.

Your function will iterate through the members of the sequence in order until the provided function returns true; at which point your function will return that item's **index**. 

If the function given returns false for all members of the sequence, your function should return -1.

```javascript
var trueIfEven = function(value, index) { return (value % 2 === 0) };
findInArray([1,3,5,6,7], trueIfEven) // should === 3
```

```python
true_if_even = lambda value, index: value % 2 == 0
find_in_array([1,3,5,6,7], true_if_even) # --> 3
```

```groovy
isEven = { value, index -> value % 2 == 0 }
Kata.findInArray([1,3,5,6,7], isEven) == 3
```

```ruby
true_if_even = lambda { |value, index| value.even? }
find_in_array([1,3,5,6,7], true_if_even) # --> 3
```

