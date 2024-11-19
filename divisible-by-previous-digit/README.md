# Divisible by previous digit?

 - URL:[https://www.codewars.com/kata/5a2809dbe1ce0e07f800004d](https://www.codewars.com/kata/5a2809dbe1ce0e07f800004d)
 - Id: 5a2809dbe1ce0e07f800004d
 - Language: python
 - Completed on: 2022-06-11T11:55:09.056Z
 - Tags: Algorithms
 - Description:
Take a number and check each digit if it is divisible by the digit on its left checked and return an array of booleans.

The booleans should always start with false becase there is no digit before the first one.

## Examples
```
73312        => [false, false, true, false, true]
2026         => [false, true, false, true]
635          => [false, false, false]
```

*** Remember 0 is evenly divisible by all integers but not the other way around ***
