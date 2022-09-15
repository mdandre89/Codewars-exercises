# The Greatest Warrior

 - URL:[https://www.codewars.com/kata/5941c545f5c394fef900000c](https://www.codewars.com/kata/5941c545f5c394fef900000c)
 - Id: 5941c545f5c394fef900000c
 - Language: python
 - Completed on: 2022-06-26T18:27:20.564Z
 - Tags: Algorithms
 - Description:
![alt text](https://2.bp.blogspot.com/-DNNiOXduuvQ/Vh-FR-qbKXI/AAAAAAAAEOA/HT0IzJ36zW4/s1600/voz.jpg)

Create a class called `Warrior` which calculates and keeps track of their level and skills, and ranks them as the warrior they've proven to be.

<b><span style="color:#00BFFF">Business Rules:</span></b>

- A warrior starts at level <span style="color:#e4d00a">1</span> and can progress all the way to <span style="color:#e4d00a">100</span>.
- A warrior starts at rank `"Pushover"` and can progress all the way to `"Greatest"`.
- The only acceptable range of rank values is `"Pushover", "Novice", "Fighter", "Warrior", "Veteran", "Sage", "Elite", "Conqueror", "Champion", "Master", "Greatest"`.
- Warriors will compete in battles. Battles will always accept an enemy level to match against your own.
- With each battle successfully finished, your warrior's experience is updated based on the enemy's level.
- The experience earned from the battle is relative to what the warrior's current level is compared to the level of the enemy.
- A warrior's experience starts from <span style="color:#e4d00a">100</span>. Each time the warrior's experience increases by another <span style="color:#e4d00a">100</span>, the warrior's level rises to the next level.
- A warrior's experience is <span style="color:#e4d00a">cumulative</span>, and does not reset with each rise of level. The only exception is when the warrior reaches level <span style="color:#e4d00a">100</span>, with which the experience stops at <span style="color:#e4d00a">10000</span>
- At every <span style="color:#e4d00a">10</span> levels, your warrior will reach a new rank tier. (ex. levels <span style="color:#e4d00a">1-9</span> falls within `"Pushover"` tier, levels <span style="color:#e4d00a">80-89</span> fall within `"Champion"` tier, etc.)
- A warrior cannot progress beyond level <span style="color:#e4d00a">100</span> and rank `"Greatest"`.


<b><span style="color:#00BFFF">Battle Progress Rules & Calculations:</span></b>

- If an enemy level does not fall in the range of 1 to 100, the battle cannot happen and should return `"Invalid level"`.
- Completing a battle against an enemy with the same level as your warrior will be worth <span style="color:#e4d00a">10</span> experience points.
- Completing a battle against an enemy who is one level lower than your warrior will be worth <span style="color:#e4d00a">5</span> experience points.
- Completing a battle against an enemy who is two levels lower or more than your warrior will give <span style="color:#e4d00a">0</span> experience points.
- Completing a battle against an enemy who is one level higher or more than your warrior will accelarate your experience gaining. The greater the difference between levels, the more experinece your warrior will gain. The formula is `20 * diff * diff` where `diff` equals the difference in levels between the enemy and your warrior.
- However, if your warrior is at least one rank lower than your enemy, and at least 5 levels lower, your warrior cannot fight against an enemy that strong and must instead return `"You've been defeated"`.
- Every successful battle will also return one of three responses: `"Easy fight", "A good fight", "An intense fight"`. Return `"Easy fight"` if your warrior is 2 or more levels higher than your enemy's level. Return `"A good fight"` if your warrior is either 1 level higher or equal to your enemy's level. Return `"An intense fight"` if your warrior's level is lower than the enemy's level.

<b><span style="color:#00BFFF">Logic Examples:</span></b>

- If a warrior level <span style="color:#e4d00a">1</span> fights an enemy level <span style="color:#e4d00a">1</span>, they will receive <span style="color:#e4d00a">10</span> experience points.
- If a warrior level <span style="color:#e4d00a">1</span> fights an enemy level <span style="color:#e4d00a">3</span>, they will receive <span style="color:#e4d00a">80</span> experience points.
- If a warrior level <span style="color:#e4d00a">5</span> fights an enemy level <span style="color:#e4d00a">4</span>, they will receive <span style="color:#e4d00a">5</span> experience points.
- If a warrior level <span style="color:#e4d00a">3</span> fights an enemy level <span style="color:#e4d00a">9</span>, they will receive <span style="color:#e4d00a">720</span> experience points, resulting in the warrior rising up by at least <span style="color:#e4d00a">7</span> levels.
- If a warrior level <span style="color:#e4d00a">8</span> fights an enemy level <span style="color:#e4d00a">13</span>, they will receive <span style="color:#e4d00a">0</span> experience points and return `"You've been defeated"`. (Remember, difference in rank & enemy level being <span style="color:#e4d00a">5</span> levels higher or more must be established for this.)
- If a warrior level <span style="color:#e4d00a">6</span> fights an enemy level <span style="color:#e4d00a">2</span>, they will receive <span style="color:#e4d00a">0</span> experience points.

<b><span style="color:#00BFFF"> Training Rules & Calculations:</span></b>
- In addition to earning experience point from battles, warriors can also gain experience points from training.
- Training will accept an array of three elements (except in java where you'll get 3 separated arguments): the description, the experience points your warrior earns, and the minimum level requirement.
- If the warrior's level meets the minimum level requirement, the warrior will receive the experience points from it and store the description of the training. It should end up returning that description as well.
- If the warrior's level does not meet the minimum level requirement, the warrior doesn not receive the experience points and description and instead returns `"Not strong enough"`, without any archiving of the result.

<b><span style="color:#00BFFF"> Code Examples:</span></b>
```javascript
var bruce_lee = new Warrior();
bruce_lee.level();        // => 1
bruce_lee.experience();   // => 100
bruce_lee.rank();         // => "Pushover"
bruce_lee.achievements(); // => []
bruce_lee.training(["Defeated Chuck Norris", 9000, 1]); // => "Defeated Chuck Norris"
bruce_lee.experience();   // => 9100
bruce_lee.level();        // => 91
bruce_lee.rank();         // => "Master"
bruce_lee.battle(90);     // => "A good fight"
bruce_lee.experience();   // => 9105
bruce_lee.achievements(); // => ["Defeated Chuck Norris"]
```
```ruby
bruce_lee = Warrior.new
bruce_lee.level         # => 1
bruce_lee.experience    # => 100
bruce_lee.rank          # => "Pushover"
bruce_lee.achievements  # => []
bruce_lee.training(["Defeated Chuck Norris", 9000, 1]) # => "Defeated Chuck Norris"
bruce_lee.experience    # => 9100
bruce_lee.level         # => 91
bruce_lee.rank          # => "Master"
bruce_lee.battle(90)    # => "A good fight"
bruce_lee.experience    # => 9105
bruce_lee.achievements  # => ["Defeated Chuck Norris"]
```
```python
bruce_lee = Warrior()
bruce_lee.level         # => 1
bruce_lee.experience    # => 100
bruce_lee.rank          # => "Pushover"
bruce_lee.achievements  # => []
bruce_lee.training(["Defeated Chuck Norris", 9000, 1]) # => "Defeated Chuck Norris"
bruce_lee.experience    # => 9100
bruce_lee.level         # => 91
bruce_lee.rank          # => "Master"
bruce_lee.battle(90)    # => "A good fight"
bruce_lee.experience    # => 9105
bruce_lee.achievements  # => ["Defeated Chuck Norris"]
```
```java
// Note: all numeric values are integers.

Warrior bruce_lee = new Warrior();
bruce_lee.level();        // => 1
bruce_lee.experience();   // => 100
bruce_lee.rank();         // => "Pushover"
bruce_lee.achievements(); // => []  (as List<String>)
bruce_lee.training("Defeated Chuck Norris", 9000, 1); // => "Defeated Chuck Norris"
bruce_lee.experience();   // => 9100
bruce_lee.level();        // => 91
bruce_lee.rank();         // => "Master"
bruce_lee.battle(90);     // => "A good fight"
bruce_lee.experience();   // => 9105
bruce_lee.achievements(); // => ["Defeated Chuck Norris"]  (as List<String>)
```
