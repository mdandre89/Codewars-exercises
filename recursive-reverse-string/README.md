# Recursive reverse string

 - URL:[https://www.codewars.com/kata/536a9f94021a76ef0f00052f](https://www.codewars.com/kata/536a9f94021a76ef0f00052f)
 - Id: 536a9f94021a76ef0f00052f
 - Language: javascript
 - Completed on: 2017-08-06T20:20:00.702Z
 - Tags: Fundamentals,Strings,Data Types
 - Description:
##Do you know how to write a recursive function? Let's test it!
---

*
Definition: Recursive function is a function that calls itself during its execution
*
```
Classic factorial counting on Javascript
function factorial(n) {
  return n <= 1 ? 1 : n * factorial(n-1) 
}

```

---
Your objective is to complete a recursive function `reverse()` that receives `str` as String and returns the same string in reverse order

Rules:

- reverse function should be executed exactly N times. `N = length of the input string`
- helper functions are not allowed
- changing the signature of the function is not allowed


Examples:
```
reverse("hello world") = "dlrow olleh" (N = 11)
reverse("abcd") = "dcba" (N = 4)
reverse("12345") = "54321" (N = 5)
```

<i>All tests for this Kata are randomly generated, besides checking the reverse logic they will count how many times the reverse() function has been executed. <i>
