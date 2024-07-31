# Exclamation marks series #7: Remove words from  the sentence if it contains one exclamation mark 

 - URL:[https://www.codewars.com/kata/57fafb6d2b5314c839000195](https://www.codewars.com/kata/57fafb6d2b5314c839000195)
 - Id: 57fafb6d2b5314c839000195
 - Language: python
 - Completed on: 2022-06-25T10:16:34.141Z
 - Tags: Fundamentals
 - Description:
# Description:

Remove words from the sentence if they contain exactly one exclamation mark. Words are separated by a single space, without leading/trailing spaces.

# Examples

```
remove("Hi!") === ""
remove("Hi! Hi!") === ""
remove("Hi! Hi! Hi!") === ""
remove("Hi Hi! Hi!") === "Hi"
remove("Hi! !Hi Hi!") === ""
remove("Hi! Hi!! Hi!") === "Hi!!"
remove("Hi! !Hi! Hi!") === "!Hi!"
```

