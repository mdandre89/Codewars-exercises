# Chess piece values

 - URL:[https://www.codewars.com/kata/5832514f64a4cecd1c000013](https://www.codewars.com/kata/5832514f64a4cecd1c000013)
 - Id: 5832514f64a4cecd1c000013
 - Language: python
 - Completed on: 2022-06-27T17:52:33.332Z
 - Tags: Arrays,Fundamentals
 - Description:
<h2>Task:</h2>
<p>Complete the function <code>piecesValue</code>/<code>pieces_value</code> that accepts two arguments, an 8x8 array (arr),representing a chess board and a string (s). Depending on the value of the string <code>s</code>  (which can be either <code>"white"</code> or <code>"black"</code>) calculate the value of the pieces on the table for the corresponding player(white or black). <br> Empty fields will be marked as a space <code>" "</code> while the fields with pieces look like this:</p>

```javascript
"w-king"   //meaning white king
"b-bishop" //a black bishop
"w-pawn"   //white pawn
```

...and so on. Preloaded for you there is an object called `hash` (`values` in python):

```javascript
const hash = Object.freeze({
  queen: 9, rook: 5, bishop: 3, knight: 3, pawn: 1
});
```
```python
values = {
    'queen': 9,
    'rook': 5,
    'bishop': 3,
    'knight': 3,
    'pawn': 1,
}
```

<p>Having the estimated value of each piece. This is a rough estimation and the real piece value depends on other factors in game as well ,such as the game being a closed or open one, which can favor either knights or bishops. (If you are interested more about that here: <a href="https://www.chess.com/chessopedia/view/open-closed">open vs closed game</a>.) But for our purposes we will use the mentioned values. <br>
<b>Note:</b> the value of a king cannot be estimated because without it the game would be over, so <strong>DO NOT</strong> take into consideration the value of the king.You will not be tested for invalid input.<br>
</p>
<strong>Example case:</strong>

```javascript
piecesValue([[' ',' ',' ',' ',' ',' ',' ',' '],
             [' ',' ','b-queen',' ',' ',' ',' ','w-queen'],
             [' ','b-king',' ',' ','w-rook',' ',' ',' '],
             [' ',' ',' ',' ',' ',' ',' ',' '],
             [' ',' ',' ',' ',' ',' ',' ',' '],
             ['w-king',' ',' ',' ',' ',' ',' ',' '],
             [' ',' ',' ',' ',' ',' ',' ',' '],
             [' ',' ',' ',' ',' ',' ',' ',' ']], 
             'white');
//should be 14 since white has a queen and a rook 
//while the same table would return 9 for 'black'

piecesValue([[' ',' ',' ',' ',' ',' ',' ',' '],
             [' ',' ','b-queen',' ',' ',' ',' ','w-queen'],
             [' ','b-king',' ','b-pawn','w-rook',' ',' ',' '],
             [' ',' ',' ',' ','w-pawn',' ',' ',' '],
             [' ',' ',' ',' ',' ','w-bishop',' ',' '],
             ['w-king',' ',' ',' ',' ',' ',' ',' '],
             [' ',' ',' ','b-pawn',' ',' ',' ',' '],
             [' ',' ',' ',' ',' ',' ',' ',' ']],
             'white');
//should return 18 for 'white' (queen, rook, pawn, bishop)
//and 11 in case s is 'black'(queen, pawn, pawn)
```

## Happy coding warrior!
