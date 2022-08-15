# Two Joggers

 - URL:[https://www.codewars.com/kata/5274d9d3ebc3030802000165](https://www.codewars.com/kata/5274d9d3ebc3030802000165)
 - Id: 5274d9d3ebc3030802000165
 - Language: python
 - Completed on: 2017-08-22T11:17:30.367Z
 - Tags: Mathematics,Algorithms
 - Description:
Two Joggers
===

Description
---
Bob and Charles are meeting for their weekly jogging tour. They both start at the same spot called "Start" and they each run a different lap, which may (or may not) vary in length. Since they know each other for a long time already, they both run at the exact same speed.

Illustration
---
Example where Charles (dashed line) runs a shorter lap than Bob:

![Example laps](http://www.haan.lu/files/7713/8338/6140/jogging.png "Example laps")

Task
---
Your job is to complete the function **nbrOfLaps(x, y)** that, given the length of the laps for Bob and Charles, finds the number of laps that each jogger has to complete before they meet each other again, at the same time, at the start.

The function takes two arguments:

1. The length of Bob's lap (larger than 0)
2. The length of Charles' lap (larger than 0)  

<br/>The function should return an array (`Tuple<int, int>` in C#) containing exactly two numbers:

1. The first number is the number of laps that Bob has to run
2. The second number is the number of laps that Charles has to run

</br><b>Examples:</b>
```javascript
nbrOfLaps(5, 3); // returns [3, 5]
nbrOfLaps(4, 6); // returns [3, 2]
```
```coffeescript
nbrOfLaps(5, 3); # returns [3, 5]
nbrOfLaps(4, 6); # returns [3, 2]
```
```crystal
nbr_of_laps(5, 3) # returns {3, 5}
nbr_of_laps(4, 6) # returns {3, 2}
```
```julia
nbroflaps(5, 3) # returns (3, 5)
nbroflaps(4, 6) # returns (3, 2)
```
```python
nbr_of_laps(5, 3) # returns (3, 5)
nbr_of_laps(4, 6) # returns (3, 2)
```
```ruby
nbr_of_laps(5, 3) # returns [3, 5]
nbr_of_laps(4, 6) # returns [3, 2]
```
```haskell
nbrOfLaps 5 3 -- should be (3, 5)
nbrOfLaps 4 6 -- should be (3, 2)
```
```csharp
Kata.NbrOfLaps(5, 3) => new Tuple<int, int>(3, 5);
Kata.NbrOfLaps(4, 6) => new Tuple<int, int>(3, 2);
```
```c
nbr_of_laps(5, 3); // returns {3, 5}
nbr_of_laps(4, 6); // returns {3, 2}
```
