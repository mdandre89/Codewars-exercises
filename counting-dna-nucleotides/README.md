# Counting DNA Nucleotides

 - URL:[https://www.codewars.com/kata/52e84c460d83dd96e50000dd](https://www.codewars.com/kata/52e84c460d83dd96e50000dd)
 - Id: 52e84c460d83dd96e50000dd
 - Language: javascript
 - Completed on: 2022-06-25T21:18:50.273Z
 - Tags: Algorithms
 - Description:
For a given DNA genetic code represented by a string, count the number of times the letters A (adenine), C (cytosine), G (guanine) and T (thymine) appears and return and object. 

The input string may contain both upper and lower case characters.

For example:
```javascript

var genCode = 'aCCggT';

getCountedNucleotides(genCode); // return {A: 1, C: 2, G: 2, T: 1}
```
Also, should a nucleotide type not be present within the string, it should still be present in the object returned with it's value as 0. For example:

```javascript

var genCode = 'ACG';

getCountedNucleotides(genCode); // return {A: 1, C: 1, G: 1, T: 0}
```

