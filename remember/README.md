# Remember

 - URL:[https://www.codewars.com/kata/55a243393fb3e87021000198](https://www.codewars.com/kata/55a243393fb3e87021000198)
 - Id: 55a243393fb3e87021000198
 - Language: python
 - Completed on: 2017-10-03T11:59:49.374Z
 - Tags: Logic,Strings,Arrays,Algorithms,Search
 - Description:
Write a function that takes a string and returns an array of the repeated characters (letters, numbers, whitespace) in the string.

If a charater is repeated more than once, only show it once in the result array.

Characters should be shown **by the order of their first repetition**. Note that this may be different from the order of first appearance of the character.

Characters are case sensitive.

For F# return a "char list"


## Examples:

```javascript
remember("apple") => returns ["p"]
remember("apPle") => returns []          // no repeats, "p" != "P"
remember("pippi") => returns ["p","i"]   // show "p" only once
remember('Pippi') => returns ["p","i"]   // "p" is repeated first
```
```python
remember("apple") => returns ["p"]
remember("apPle") => returns []          # no repeats, "p" != "P"
remember("pippi") => returns ["p","i"]   # show "p" only once
remember('Pippi') => returns ["p","i"]   # "p" is repeated first
```
```ruby
remember("apple") => returns ["p"]
remember("apPle") => returns []          # no repeats, "p" != "P"
remember("pippi") => returns ["p","i"]   # show "p" only once
remember('Pippi') => returns ["p","i"]   # "p" is repeated first
```
```csharp
Remember("apple") => returns ['p']
Remember("apPle") => returns []          # no repeats, 'p' != 'P'
Remember("pippi") => returns ['p','i']   # show 'p' only once
Remember('Pippi') => returns ['p','i']   # 'p' is repeated first
```

```fsharp
_rem "apple" => returns ['p']       # _rem returns a char list not a List<char>
_rem "apPle" => returns []          # no repeats, 'p' != 'P'
_rem "pippi" => returns ['p','i']   # show 'p' only once
_rem "Pippi" => returns ['p','i']   # 'p' is repeated first
```
