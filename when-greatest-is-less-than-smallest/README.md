# When greatest is less than smallest

 - URL:[https://www.codewars.com/kata/55f2a1c2cb3c95af75000045](https://www.codewars.com/kata/55f2a1c2cb3c95af75000045)
 - Id: 55f2a1c2cb3c95af75000045
 - Language: python
 - Completed on: 2017-10-17T11:12:22.843Z
 - Tags: Mathematics,Logic,Algorithms
 - Description:
Given an `x` and `y` find the smallest and greatest numbers **above** and **below** a given `n` that are divisible by both `x` and `y`.

### Examples
```python
greatest(2, 3, 20) => 18   # 18 is the greatest number under 20 that is divisible by both 2 and 3
smallest(2, 3, 20) => 24   # 24 is the smallest number above 20 that is divisible by both 2 and 3

greatest(5, 15, 100) => 90
smallest(5, 15, 100) => 105

greatest(123, 456, 789) => 0   # there are no numbers under 789 that are divisible by both 123 and 456
smallest(123, 456, 789) => 18696
```
```ruby
greatest(2, 3, 20) => 18   # 18 is the greatest number under 20 that is divisible by both 2 and 3
smallest(2, 3, 20) => 24   # 24 is the smallest number above 20 that is divisible by both 2 and 3

greatest(5, 15, 100) => 90
smallest(5, 15, 100) => 105

greatest(123, 456, 789) => 0   # there are no numbers under 789 that are divisible by both 123 and 456
smallest(123, 456, 789) => 18696
```
```haskell
greatest 2 3 20 => 18   -- 18 is the greatest number under 20 that is divisible by both 2 and 3
smallest 2 3 20 => 24   -- 24 is the smallest number above 20 that is divisible by both 2 and 3

greatest 5 15 100 => 90
smallest 5 15 100 => 105

greatest 123 456 789 => 0   -- there are no numbers under 789 that are divisible by both 123 and 456
smallest 123 456 789 => 18696
```
```clojure
greatest 2 3 20 => 18   ;; 18 is the greatest number under 20 that is divisible by both 2 and 3
smallest 2 3 20 => 24   ;; 24 is the smallest number above 20 that is divisible by both 2 and 3

greatest 5 15 100 => 90
smallest 5 15 100 => 105

greatest 123 456 789 => 0   ;; there are no numbers under 789 that are divisible by both 123 and 456
smallest 123 456 789 => 18696
```
```csharp
GreatestSmallest.Greatest(BigInteger.Parse("2"), BigInteger.Parse("3"), BigInteger.Parse("20")) => BigInteger.Parse("18") // 18 is the greatest number under 20 that is divisible by both 2 and 3
GreatestSmallest.Smallest(BigInteger.Parse("2"), BigInteger.Parse("3"), BigInteger.Parse("20")) => BigInteger.Parse("24") // 24 is the smallest number above 20 that is divisible by both 2 and 3

GreatestSmallest.Greatest(BigInteger.Parse("5"), BigInteger.Parse("15"), BigInteger.Parse("100")) => BigInteger.Parse("90")
GreatestSmallest.Smallest(BigInteger.Parse("5"), BigInteger.Parse("15"), BigInteger.Parse("100")) => BigInteger.Parse("105")

GreatestSmallest.Greatest(BigInteger.Parse("123"), BigInteger.Parse("456"), BigInteger.Parse("789")) => BigInteger.Parse("0") // there are no numbers under 789 that are divisible by both 123 and 456
GreatestSmallest.Smallest(BigInteger.Parse("123"), BigInteger.Parse("456"), BigInteger.Parse("789")) => BigInteger.Parse("18696")
```
```java
GreatestSmallest.greatest(new BigInteger("2"), new BigInteger("3"), new BigInteger("20")) => BigInteger("18") // 18 is the greatest number under 20 that is divisible by both 2 and 3
GreatestSmallest.greatest(new BigInteger("2"), new BigInteger("3"), new BigInteger("20")) => BigInteger("24") // 24 is the smallest number above 20 that is divisible by both 2 and 3

GreatestSmallest.greatest(new BigInteger("5"), new BigInteger("15"), new BigInteger("100")) => BigInteger("90")
GreatestSmallest.smallest(new BigInteger("5"), new BigInteger("15"), new BigInteger("100")) => BigInteger("105")

GreatestSmallest.greatest(new BigInteger("123"), new BigInteger("456"), new BigInteger("789")) => BigInteger("0") // there are no numbers under 789 that are divisible by both 123 and 456
GreatestSmallest.smallest(new BigInteger("123"), new BigInteger("456"), new BigInteger("789")) => BigInteger("18696")
```

**Notes:** 

1. you should never return `n` even if it is divisible by `x` and `y` always the number above or below it
2. `greatest` should return 0 if there are no numbers under `n` that are divisible by both `x` and `y`
3. and all arguments will be valid (integers greater than 0).


### Note for Haskell users

>Please take a look at [bkaes comment](http://www.codewars.com/kata/when-greatest-is-less-than-smallest/discuss#56418f0fbf1f44834d000050) and give us your opinion
