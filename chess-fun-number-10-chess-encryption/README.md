# Chess Fun #10: Chess Encryption

 - URL:[https://www.codewars.com/kata/58a3f0662f949eba5c00004f](https://www.codewars.com/kata/58a3f0662f949eba5c00004f)
 - Id: 58a3f0662f949eba5c00004f
 - Language: python
 - Completed on: 2017-10-17T11:51:22.107Z
 - Tags: Puzzles
 - Description:
## Task
 The prisoners from previous challenges love playing chess so they make extra plan C in communcation , it goes as follows.

 They distribute the 26 letters on the standard 8 x 8 chess board as shown below :

<div>
  
<img src="http://i.imgur.com/Sbdzpaa.jpg">
<img src="http://i.imgur.com/zO5VwkV.png">
</div>

 
 Then they assign every letter to its location on the board as described below:
 <br>
 <br>
 <div style="background-color: white"><img src="http://upload.wikimedia.org/wikipedia/commons/thumb/b/b6/SCD_algebraic_notation.svg/242px-SCD_algebraic_notation.svg.png"></div>
<br>

 So character `v` would correspond to a1 and `u` would be b1, etc..

 NOTE: during the encryption words are separated by space

## Example

 For: `msg = "hi"`, the result should be: `"e5e4"`
 
 For: `msg = "play again"`, the result should be: `"g1f2d3c2 d3e6d3e4h2"`

## Input/Output


 - `[input]` string `msg`

  message input.

 - `[output]` a string

  encrypted message.
