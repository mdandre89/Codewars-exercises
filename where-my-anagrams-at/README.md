# Where my anagrams at?

 - URL:[https://www.codewars.com/kata/523a86aa4230ebb5420001e1](https://www.codewars.com/kata/523a86aa4230ebb5420001e1)
 - Id: 523a86aa4230ebb5420001e1
 - Language: javascript
 - Completed on: 2017-09-10T10:41:06.587Z
 - Tags: Strings,Algorithms
 - Description:
What is an anagram? Well, two words are anagrams of each other if they both contain the same letters. For example:

```
'abba' & 'baab' == true

'abba' & 'bbaa' == true

'abba' & 'abbba' == false

'abba' & 'abca' == false
```

Write a function that will find all the anagrams of a word from a list. You will be given two inputs a word and an array with words. You should return an array of all the anagrams or an empty array if there are none. For example:

```javascript
anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']) => ['aabb', 'bbaa']

anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']) => ['carer', 'racer']

anagrams('laser', ['lazing', 'lazy',  'lacer']) => []
```

**Note for Go**\
For Go: Empty string slice is expected when there are no anagrams found.


