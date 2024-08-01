# Exclamation marks series #6: Remove n exclamation marks in the sentence from left to right

 - URL:[https://www.codewars.com/kata/57faf7275c991027af000679](https://www.codewars.com/kata/57faf7275c991027af000679)
 - Id: 57faf7275c991027af000679
 - Language: javascript
 - Completed on: 2017-03-30T15:37:32.246Z
 - Tags: Fundamentals
 - Description:
### Description:

 Remove `n` exclamation marks in the sentence from left to right. `n` is positive integer.

### Examples

```
remove("Hi!",1) === "Hi"
remove("Hi!",100) === "Hi"
remove("Hi!!!",1) === "Hi!!"
remove("Hi!!!",100) === "Hi"
remove("!Hi",1) === "Hi"
remove("!Hi!",1) === "Hi!"
remove("!Hi!",100) === "Hi"
remove("!!!Hi !!hi!!! !hi",1) === "!!Hi !!hi!!! !hi"
remove("!!!Hi !!hi!!! !hi",3) === "Hi !!hi!!! !hi"
remove("!!!Hi !!hi!!! !hi",5) === "Hi hi!!! !hi"
remove("!!!Hi !!hi!!! !hi",100) === "Hi hi hi"
```
