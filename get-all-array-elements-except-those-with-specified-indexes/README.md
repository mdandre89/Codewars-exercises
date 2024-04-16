# Get all array elements except those with specified indexes

 - URL:[https://www.codewars.com/kata/58694d1c2e8d9c6d9b000296](https://www.codewars.com/kata/58694d1c2e8d9c6d9b000296)
 - Id: 58694d1c2e8d9c6d9b000296
 - Language: javascript
 - Completed on: 2017-05-14T15:02:41.675Z
 - Tags: Data Structures,Arrays,Logic,Fundamentals
 - Description:
Extend the Array prototype/class with a function to return all elements of that array, except the ones with the indexes passed in the parameter.

The function should accept either an array or a single integer as parameters, like this:

```javascript
var array = ['a', 'b', 'c', 'd', 'e'];
var array2 = array.except([1,3]);
// array2 should contain ['a', 'c', 'e']
```
or
```javascript
var array = ['a', 'b', 'c', 'd', 'e'];
var array2 = array.except(1);
// array2 should contain ['a', 'c', 'd', 'e']
```

```ruby
array = ['a', 'b', 'c', 'd', 'e']
array.except(1) => ['a', 'c', 'd', 'e']
```
or
```ruby
array = [1, 2, 3, 4, 5, 6, 7]
array.except([0,1]) =< [3,4,5,6,7]
```

```haskell
except takes an array and a Maybe [Int], when Nothing return the original array.
```
