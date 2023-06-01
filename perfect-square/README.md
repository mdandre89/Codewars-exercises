# Perfect Square.

 - URL:[https://www.codewars.com/kata/584e93a70f60247eb8000132](https://www.codewars.com/kata/584e93a70f60247eb8000132)
 - Id: 584e93a70f60247eb8000132
 - Language: javascript
 - Completed on: 2018-02-22T10:57:58.673Z
 - Tags: Regular Expressions,Fundamentals
 - Description:
<style>

  .firstRow {
    vertical-align:-60px;
  }

</style>

<h4 style="color:brown">Task</h4>

Write function which validates an input string. If the string is a perfect square return true,false otherwise.

<h4 style="color:brown">What is perfect square?</h4>
* We assume that character '.' (dot) is a perfect square (1x1)
* Perfect squares can only contain '.' (dot) and optionally '\n' (line feed) characters.<br>
* Perfect squares must have same width and height -> cpt.Obvious<br>
* Squares of random sizes will be tested!

<h4 style="color:brown">Function input:</h4>

```javascript
perfectSquare = "...\n...\n...";    

// This represents the following Perfect Square:

`...
 ...
 ...`
                               
notPerfect = "..,\n..\n...";

// This is not a Perfect Square:

`..,
 ..
 ...`

```

