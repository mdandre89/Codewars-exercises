# Simple Fun #114: "abacaba"

 - URL:[https://www.codewars.com/kata/589d237fdfdef0239a00002e](https://www.codewars.com/kata/589d237fdfdef0239a00002e)
 - Id: 589d237fdfdef0239a00002e
 - Language: javascript
 - Completed on: 2017-03-21T16:09:26.740Z
 - Tags: Puzzles
 - Description:
## Task
 Consider the following algorithm for constructing 26 strings S(1) .. S(26):
```
S(1) = "a";
For i in [2, 3, ..., 26]:
S(i) = S(i - 1) + character(i) + S(i - 1).
```

 For example:
 
```
S(1) = "a"  
S(2) = S(1) + "b" + S(1) = "a" + "b" + "a" = "aba"  
S(3) = S(2) + "c" + S(2) = "aba" + "c" +"aba" = "abacaba"
...
S(26) = S(25) + "z" + S(25)
```
Finally, we got a long string S(26). Your task is to find the `k`th symbol (indexing from 1) in the string S(26). All strings consist of lowercase letters only.

## Input / Output


 - `[input]` integer `k`

  1 ≤ k < 2<sup>26</sup>


 - `[output]` a string(char in C#)

  the `k`th symbol of S(26)
