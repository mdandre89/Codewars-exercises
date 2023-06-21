# Numericals of a String

 - URL:[https://www.codewars.com/kata/5b4070144d7d8bbfe7000001](https://www.codewars.com/kata/5b4070144d7d8bbfe7000001)
 - Id: 5b4070144d7d8bbfe7000001
 - Language: python
 - Completed on: 2022-06-13T13:20:54.109Z
 - Tags: Puzzles,Performance,Algorithms
 - Description:
You are given an input string.

For each symbol in the string if it's the first character occurrence, replace it with a '1', else replace it with the amount of times you've already seen it.

___

## Examples:

```
input   =  "Hello, World!"
result  =  "1112111121311"

input   =  "aaaaaaaaaaaa"
result  =  "123456789101112"
```

There might be some non-ascii characters in the string.

<hr>

~~~if:java
Note: there will be no int domain overflow (character occurrences will be less than 2 billion).
~~~
~~~if:c
(this does not apply to the C language translation)
~~~


Take note of **performance**

