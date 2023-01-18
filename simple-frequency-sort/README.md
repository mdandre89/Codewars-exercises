# Simple frequency sort

 - URL:[https://www.codewars.com/kata/5a8d2bf60025e9163c0000bc](https://www.codewars.com/kata/5a8d2bf60025e9163c0000bc)
 - Id: 5a8d2bf60025e9163c0000bc
 - Language: python
 - Completed on: 2018-02-22T15:37:33.365Z
 - Tags: Algorithms
 - Description:
In this Kata, you will sort elements in an array by decreasing frequency of elements. If two elements have the same frequency, sort them by increasing value. 

```haskell
solve([2,3,5,3,7,9,5,3,7]) = [3,3,3,5,5,7,7,2,9]
--we sort by highest frequency to lowest frequency. If two elements have same frequency, we sort by increasing value
```

```cpp
solve({2,3,5,3,7,9,5,3,7}) == {3,3,3,5,5,7,7,2,9}
// We sort by highest frequency to lowest frequency.
// If two elements have same frequency, we sort by increasing value.
```

```java
Solution.sortByFrequency(new int[]{2, 3, 5, 3, 7, 9, 5, 3, 7});
// Returns {3, 3, 3, 5, 5, 7, 7, 2, 9}
// We sort by highest frequency to lowest frequency.
// If two elements have same frequency, we sort by increasing value.
```

More examples in test cases. 

Good luck!

Please also try [Simple time difference](https://www.codewars.com/kata/5b76a34ff71e5de9db0000f2)
