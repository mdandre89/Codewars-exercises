# The reject() function

 - URL:[https://www.codewars.com/kata/52988f3f7edba9839c00037d](https://www.codewars.com/kata/52988f3f7edba9839c00037d)
 - Id: 52988f3f7edba9839c00037d
 - Language: python
 - Completed on: 2022-06-12T18:28:50.372Z
 - Tags: Arrays,Fundamentals
 - Description:
Implement a function which filters out array values which satisfy the given predicate.

```javascript
reject([1, 2, 3, 4, 5, 6], (n) => n % 2 === 0)  =>  [1, 3, 5]
```
```csharp
Kata.Reject(new int[] {1, 2, 3, 4, 5, 6}, (n) => n % 2 == 0)  =>  new int[] {1, 3, 5}
```
```php
reject([1, 2, 3, 4, 5, 6], function ($n) {return $n % 2 == 0;})  =>  [1, 3, 5]
```
```python
reject([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)  =>  [1, 3, 5]
```
