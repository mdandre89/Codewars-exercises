# Elimination Tournament 

 - URL:[https://www.codewars.com/kata/5f631ed489e0e101a70c70a0](https://www.codewars.com/kata/5f631ed489e0e101a70c70a0)
 - Id: 5f631ed489e0e101a70c70a0
 - Language: python
 - Completed on: 2022-06-25T10:11:33.112Z
 - Tags: Arrays,Fundamentals
 - Description:
In this Kata you will be given an array (or another language-appropriate collection) representing contestant ranks. You must eliminate contestant in series of rounds comparing consecutive pairs of ranks and store all initial and intermediate results in an array.

During one round, the lowest rank of a pair is eliminated while the highest proceeds to the next round. This goes on until one contestant only is left. If the number of contestants is odd, the last one of the current array becomes the first of the next round.

At the end of the competition, return the results of all the rounds in the form of array of arrays.

### Example:

```
input = [9, 5, 4, 7, 6, 3, 8, 2];

output = [
  [9, 5, 4, 7, 6, 3, 8, 2],  // first round is initial input
  [9, 7, 6, 8],              // results of 9 vs 5, 4 vs 7, 6 vs 3, and 8 vs 2 
  [9, 8],                    // results of 9 vs 7 and 6 vs 8
  [9]                        // results of 9 vs 8
];
```

Notes:
- Array length will alway be >= 2 and <= 100
- Elements of the array will always be >=1 and <= 100
- Input must not be altered.

