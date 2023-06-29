# Number of permutations without repetitions

 - URL:[https://www.codewars.com/kata/571bff6082661c8a11000823](https://www.codewars.com/kata/571bff6082661c8a11000823)
 - Id: 571bff6082661c8a11000823
 - Language: python
 - Completed on: 2017-10-24T08:49:08.564Z
 - Tags: Permutations,Combinatorics,Mathematics,Algorithms
 - Description:
Write a function that takes a number or a string and gives back the number of **permutations without repetitions** that can generated using all of its element.; more on permutations [here](https://en.wikipedia.org/wiki/Permutation).

For example, starting with:
```
1
45
115
"abc"
```

You could respectively generate:
```
1
45,54
115,151,511
"abc","acb","bac","bca","cab","cba"
```

So you should have, in turn:
```javascript
perms(1)==1
perms(45)==2
perms(115)==3
perms("abc")==6
```
```ruby
perms(1)==1
perms(45)==2
perms(115)==3
perms("abc")==6
```
```python
perms(1)==1
perms(45)==2
perms(115)==3
perms("abc")==6
```
