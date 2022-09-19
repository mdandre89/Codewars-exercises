# The First Non Repeated Character In A String 

 - URL:[https://www.codewars.com/kata/570f6436b29c708a32000826](https://www.codewars.com/kata/570f6436b29c708a32000826)
 - Id: 570f6436b29c708a32000826
 - Language: python
 - Completed on: 2017-11-27T12:04:45.826Z
 - Tags: Algorithms,Strings,Fundamentals
 - Description:
You need to write a function, that returns the first non-repeated character in the given string.  

If all the characters are unique, return the first character of the string.  
If there is no unique character, return `null` in JS or Java, and `None` in Python.

You can assume, that the input string has always non-zero length.

## Example

```javascript
firstNonRepeated("test") // returns "e"
firstNonRepeated("teeter") // returns "r"
firstNonRepeated("trend") // returns "t" (all the characters are unique)
firstNonRepeated("aabbcc") // returns null (all the characters are repeated)
```

```java
firstNonRepeated("test") // returns "e"
firstNonRepeated("teeter") // returns "r"
firstNonRepeated("trend") // returns "t" (all the characters are unique)
firstNonRepeated("aabbcc") // returns null (all the characters are repeated)
```
```python
first_non_repeated("test") # returns "e"
first_non_repeated("teeter") # returns "r"
first_non_repeated("trend") # returns "t" (all the characters are unique)
first_non_repeated("aabbcc") # returns None (all the characters are repeated)
```
