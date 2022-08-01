# Urban Dictionary

 - URL:[https://www.codewars.com/kata/5631ac5139795b281d00007d](https://www.codewars.com/kata/5631ac5139795b281d00007d)
 - Id: 5631ac5139795b281d00007d
 - Language: python
 - Completed on: 2017-11-20T15:55:59.030Z
 - Tags: Algorithms
 - Description:
Design a data structure that supports the following two operations:

* `addWord` (or `add_word`) which adds a word,
* `search` which searches a literal word or a regular expression string containing lowercase letters `"a-z"` or `"."` where `"."` can represent any letter

You may assume that all given words contain only lowercase letters.


## Examples
```javascript
addWord("bad")
addWord("dad")
addWord("mad")

search("pad") === false
search("bad") === true
search(".ad") === true
search("b..") === true
```
```python
wd = WordDictionary()

wd.add_word("bad")
wd.add_word("dad")
wd.add_word("mad")

wd.search("pad") == False
wd.search("bad") == True
wd.search(".ad") == True
wd.search("b..") == True
```
```ruby
add_word("bad")
add_word("dad")
add_word("mad")

search("pad") == false
search("bad") == true
search(".ad") == true
search("b..") == true
```

**Note:** the data structure will be initialized multiple times during the tests!
