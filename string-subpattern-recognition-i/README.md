# String subpattern recognition I

 - URL:[https://www.codewars.com/kata/5a49f074b3bfa89b4c00002b](https://www.codewars.com/kata/5a49f074b3bfa89b4c00002b)
 - Id: 5a49f074b3bfa89b4c00002b
 - Language: python
 - Completed on: 2018-02-08T15:48:09.742Z
 - Tags: Strings,Regular Expressions,Fundamentals
 - Description:
In this kata you need to build a function to return either `true/True` or `false/False` if a string can be seen as the repetition of a simpler/shorter subpattern or not.

For example:

```cpp,java
hasSubpattern("a") == false; //no repeated pattern
hasSubpattern("aaaa") == true; //created repeating "a"
hasSubpattern("abcd") == false; //no repeated pattern
hasSubpattern("abababab") == true; //created repeating "ab"
hasSubpattern("ababababa") == false; //cannot be entirely reproduced repeating a pattern
```
```javascript
hasSubpattern("a") === false; //no repeated pattern
hasSubpattern("aaaa") === true; //created repeating "a"
hasSubpattern("abcd") === false; //no repeated pattern
hasSubpattern("abababab") === true; //created repeating "ab"
hasSubpattern("ababababa") === false; //cannot be entirely reproduced repeating a pattern
```
```haskell
hasSubpattern "a" == False -- no repeated pattern
hasSubpattern "aaaa" == True -- created repeating "a"
hasSubpattern "abcd" == False -- no repeated pattern
hasSubpattern "abababab" == True -- created repeating "ab"
hasSubpattern "ababababa" == False -- cannot be entirely reproduced repeating a pattern
```
```python
has_subpattern("a") == False #no repeated pattern
has_subpattern("aaaa") == True #created repeating "a"
has_subpattern("abcd") == False #no repeated pattern
has_subpattern("abababab") == True #created repeating "ab"
has_subpattern("ababababa") == False #cannot be entirely reproduced repeating a pattern
```
```ruby
has_subpattern("a") == false #no repeated pattern
has_subpattern("aaaa") == true #created repeating "a"
has_subpattern("abcd") == false #no repeated pattern
has_subpattern("abababab") == true #created repeating "ab"
has_subpattern("ababababa") == false #cannot be entirely reproduced repeating a pattern
```
```crystal
has_subpattern("a") == false #no repeated pattern
has_subpattern("aaaa") == true #created repeating "a"
has_subpattern("abcd") == false #no repeated pattern
has_subpattern("abababab") == true #created repeating "ab"
has_subpattern("ababababa") == false #cannot be entirely reproduced repeating a pattern
```
```csharp
HasSubpattern("a") == false; //no repeated pattern
HasSubpattern("aaaa") == true; //created repeating "a"
HasSubpattern("abcd") == false; //no repeated pattern
HasSubpattern("abababab") == true; //created repeating "ab"
HasSubpattern("ababababa") == false; //cannot be entirely reproduced repeating a pattern
```
Strings will never be empty and can be composed of any character (just consider upper- and lowercase letters as different entities) and can be pretty long (keep an eye on performances!).

If you liked it, go for the [next kata](https://www.codewars.com/kata/string-subpattern-recognition-ii/) of the series!

