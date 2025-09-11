# Character frequency

 - URL:[https://www.codewars.com/kata/53e895e28f9e66a56900011a](https://www.codewars.com/kata/53e895e28f9e66a56900011a)
 - Id: 53e895e28f9e66a56900011a
 - Language: python
 - Completed on: 2017-08-15T15:05:01.062Z
 - Tags: Strings,Algorithms
 - Description:
Write a function that takes a piece of text in the form of a string and returns the letter frequency count for the text. This count excludes numbers, spaces and all punctuation marks. Upper and lower case versions of a character are equivalent and the result should all be in lowercase.

The function should return a list of tuples (in Python and Haskell) or arrays (in other languages) sorted by the most frequent letters first. The Rust implementation should return an ordered BTreeMap.
Letters with the same frequency are ordered alphabetically.
For example:

```python
  letter_frequency('aaAabb dddDD hhcc')
```  
```haskell
  letterFrequency "aaAabb dddDD hhcc"
```
```javascript
  letterFrequency('aaAabb dddDD hhcc')
```
```ruby
  letter_frequency('aaAabb dddDD hhcc')
```
```rust
  letter_frequency("aaAabb dddDD hhcc")
```
```C++
  letter_frequency("aaAabb dddDD hhcc")
```

will return

```python
  [('d',5), ('a',4), ('b',2), ('c',2), ('h',2)]
```  
```haskell
  [('d',5), ('a',4), ('b',2), ('c',2), ('h',2)]
```  
```javascript
  [['d',5], ['a',4], ['b',2], ['c',2], ['h',2]]
```
```ruby
  [['d',5], ['a',4], ['b',2], ['c',2], ['h',2]]
```
```rust
  [('d',5), ('a',4), ('b',2), ('c',2), ('h',2)]
```
```C++
  std::vector<std::pair<char, size_t>>{{'d',5}, {'a',4}, {'b',2}, {'c',2}, {'h',2}}
```

Letter frequency analysis is often used to analyse simple substitution cipher texts like those created by the Caesar cipher.

