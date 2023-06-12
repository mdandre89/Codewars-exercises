# Palindromes Below

 - URL:[https://www.codewars.com/kata/530d0298e09e54a3620006c2](https://www.codewars.com/kata/530d0298e09e54a3620006c2)
 - Id: 530d0298e09e54a3620006c2
 - Language: javascript
 - Completed on: 2017-09-11T17:01:01.597Z
 - Tags: Logic,Algorithms
 - Description:
The aim of this Kata is to modify the `Fixnum` ( **JS**: `Number` **CS**: extension for `int`) class to give it the `palindrome_below` ( **JS**: `palindromeBelow` **CS**: `PalindromeBelow` ) method. This method returns all numbers from and including 1 up to but not including itself that are palindromes for a given **[base](http://en.wikipedia.org/wiki/Radix)**.

For example in base 2 (binary)

    1 = "1"
    2 = "10"
    3 = "11"
    4 = "100"

Therefore 1 and 3 are palindromes in base two and the method should return the following.

```ruby
    5.palindrome_below(2)
    => [1, 3]
```
```javascript
    5..palindromeBelow(2)
    => [1, 3]
```
```csharp
    5.PalindromeBelow(2)
    => [1, 3]
```

