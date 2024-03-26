# High score table

 - URL:[https://www.codewars.com/kata/5962bbea6878a381ed000036](https://www.codewars.com/kata/5962bbea6878a381ed000036)
 - Id: 5962bbea6878a381ed000036
 - Language: python
 - Completed on: 2017-11-20T12:16:30.438Z
 - Tags: Algorithms,Sorting,Arrays,Object-oriented Programming
 - Description:
You just got done writing a function that calculates the player's final score for your new game, "Flight of the <a href = 'https://upload.wikimedia.org/wikipedia/commons/thumb/7/71/Cacatua_moluccensis_excited.jpg/1280px-Cacatua_moluccensis_excited.jpg'>cockatoo</a>".

Now all you need is a high score table that can be updated with the player's final scores. With such a feature, the player will be motivated to try to beat his previous scores, and hopefully, never stop playing your game.

The high score table will start out empty. A limit to the size of the table will be specified upon creation of the table.

<strong>Here's an example of the expected behavior of the high score table :</strong>

```python
highScoreTable = HighScoreTable(3)
highScoreTable.scores == [] # evaluates to True
highScoreTable.update(10)
highScoreTable.scores == [10]
highScoreTable.update(8)
highScoreTable.update(12)
highScoreTable.update(5)
highScoreTable.update(10)
highScoreTable.scores == [12, 10, 10]
highScoreTable.reset()
highScoreTable.scores == []
# And so on...
```
```coffeescript
highScoreTable = new HighScoreTable 3
highScoreTable.scores # => []
highScoreTable.update 10
highScoreTable.scores # => [10]
highScoreTable.update 8
highScoreTable.update 12
highScoreTable.update 5
highScoreTable.update 10
highScoreTable.scores # => [12, 10, 10]
highScoreTable.reset()
highScoreTable.scores # => []
# And so on...
```
