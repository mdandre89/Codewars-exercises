# Word Finder

 - URL:[https://www.codewars.com/kata/525d8c20915a399b5600087b](https://www.codewars.com/kata/525d8c20915a399b5600087b)
 - Id: 525d8c20915a399b5600087b
 - Language: javascript
 - Completed on: 2022-06-13T12:33:05.274Z
 - Tags: Strings,Regular Expressions,Filtering,Algorithms
 - Description:
In this kata you have to extend the dictionary with a method, that returns a list of words matching a pattern. This pattern may contain letters (lowercase) and placeholders ("?"). A placeholder stands for exactly one arbitrary letter.

Example:

```javascript
var fruits = new Dictionary(['banana', 'apple', 'papaya', 'cherry']);
fruits.getMatchingWords('lemon');     // must return []
fruits.getMatchingWords('cherr??');   // must return []
fruits.getMatchingWords('?a?a?a');    // must return ['banana', 'papaya']
fruits.getMatchingWords('??????');    // must return ['banana', 'papaya', 'cherry']
```

```coffeescript
fruits = new Dictionary([
  'banana'
  'apple'
  'papaya'
  'cherry'
])
fruits.getMatchingWords 'lemon'          # must return []
fruits.getMatchingWords 'cherr??'        # must return []
fruits.getMatchingWords '?a?a?a'         # must return ['banana', 'papaya']
fruits.getMatchingWords '??????'         # must return ['banana', 'papaya', 'cherry']
```

Additional Notes:

* the words and patterns are all lowercase
* the order of the returned words doesn't matter
