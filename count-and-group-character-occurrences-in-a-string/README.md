# Count and Group Character Occurrences in a String

 - URL:[https://www.codewars.com/kata/543e8390386034b63b001f31](https://www.codewars.com/kata/543e8390386034b63b001f31)
 - Id: 543e8390386034b63b001f31
 - Language: python
 - Completed on: 2022-06-25T10:26:44.721Z
 - Tags: Fundamentals
 - Description:
Write a method that takes a string as an argument and groups the number of time each character appears in the string as a hash sorted by the highest number of occurrences.

The characters should be sorted alphabetically e.g:

```ruby
get_char_count("cba") => {1=>["a", "b", "c"]}
```
```python
get_char_count("cba") == {1: ["a", "b", "c"]}
```

You should ignore spaces, special characters and count uppercase letters as lowercase ones.

For example: 
```ruby
get_char_count("Mississippi") => {4=>["i", "s"], 2=>["p"], 1=>["m"]}
get_char_count("Hello. Hello? HELLO!!") => {6=>["l"], 3=>["e", "h", "o"]}
get_char_count("aaa...bb...c!") => {3=>["a"], 2=>["b"], 1=>["c"]}
get_char_count("aaabbbccc") => {3=>["a", "b", "c"]}
get_char_count("abc123") => {1=>["1", "2", "3", "a", "b", "c"]}
```
```python
get_char_count("Mississippi")           ==  {4: ["i", "s"], 2: ["p"], 1: ["m"]}
get_char_count("Hello. Hello? HELLO!")  ==  {6: ["l"], 3: ["e", "h", "o"]}
get_char_count("aaa...bb...c!")         ==  {3: ["a"], 2: ["b"], 1: ["c"]}
get_char_count("abc123")                ==  {1: ["1", "2", "3", "a", "b", "c"]}
get_char_count("aaabbbccc")             ==  {3: ["a", "b", "c"]}
```
