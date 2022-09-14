# The Look and Say sequence

 - URL:[https://www.codewars.com/kata/5263c5d011f4233c9d000561](https://www.codewars.com/kata/5263c5d011f4233c9d000561)
 - Id: 5263c5d011f4233c9d000561
 - Language: javascript
 - Completed on: 2017-11-21T17:52:40.762Z
 - Tags: Mathematics,Algorithms
 - Description:
From [Wikipedia](https://en.wikipedia.org/wiki/Look-and-say_sequence):

In mathematics, the look-and-say sequence is the sequence of integers beginning as follows:

```
1, 11, 21, 1211, 111221, 312211, …
```

To generate a member of the sequence from the previous member, read off the digits of the previous member, counting the number of digits in groups of the same digit. For example:

```
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
1211 is read off as "one 1, then one 2, then two 1s" or 111221.
111221 is read off as "three 1s, then two 2s, then one 1" or 312211.
```

---

```if-not:rust,haskell,
Your mission is to write a function which, given an integer "n" as parameter, returns a comma separated list of the first "n" terms of the sequence. For `0`, negative, or `NaN` parameters, `-1` shall be returned.
```
```if:rust,haskell,
Your mission is to write a function which, given an integer `n` as parameter, returns a comma separated list of the first `n` terms of the sequence. For `0`, an empty string shall be returned.
```

For example:

```javascript
getLines(2);  //  "1,11"
getLines(3);  //  "1,11,21"
getLines(5);  //  "1,11,21,1211,111221"
```
```rust
get_lines(2);  //  "1,11"
get_lines(3);  //  "1,11,21"
get_lines(5);  //  "1,11,21,1211,111221"
```
