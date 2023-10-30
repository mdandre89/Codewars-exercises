# Linked Lists - Move Node

 - URL:[https://www.codewars.com/kata/55da347204760ba494000038](https://www.codewars.com/kata/55da347204760ba494000038)
 - Id: 55da347204760ba494000038
 - Language: python
 - Completed on: 2022-06-25T13:09:32.202Z
 - Tags: Linked Lists,Data Structures,Fundamentals
 - Description:
Linked Lists - Move Node

Write a MoveNode() function which takes the node from the front of the source list and moves it to the front of the destintation list. You should throw an error when the source list is empty. For simplicity, we use a Context object to store and return the state of the two linked lists. A Context object containing the two mutated lists should be returned by moveNode.

MoveNode() is a handy utility function to have for later problems. 

### JavaScript
```javascript
var source = 1 -> 2 -> 3 -> null
var dest = 4 -> 5 -> 6 -> null
moveNode(source, dest).source === 2 -> 3 -> null
moveNode(source, dest).dest === 1 -> 4 -> 5 -> 6 -> null
```
### Python
```python
source = 1 -> 2 -> 3 -> None
dest = 4 -> 5 -> 6 -> None
move_node(source, dest).source == 2 -> 3 -> None
move_node(source, dest).dest == 1 -> 4 -> 5 -> 6 -> None
```

### Ruby
```ruby
source = 1 -> 2 -> 3 -> nil
dest = 4 -> 5 -> 6 -> nil
move_node(source, dest).source == 2 -> 3 -> nil
move_node(source, dest).dest == 1 -> 4 -> 5 -> 6 -> nil
```

The push() and buildOneTwoThree() functions need not be redefined.

There is another kata called <a href="http://www.codewars.com/kata/linked-lists-move-node-in-place">Linked Lists - Move Node In-place</a> that is related but more difficult.

Related Kata in order of expected completion (increasing difficulty):<br>
 <a href="http://www.codewars.com/kata/linked-lists-push-and-buildonetwothree">Linked Lists - Push & BuildOneTwoThree</a><br>
 <a href="http://www.codewars.com/kata/linked-lists-length-and-count">Linked Lists - Length & Count</a><br>
 <a href="http://www.codewars.com/kata/linked-lists-get-nth-node">Linked Lists - Get Nth Node</a><br>
<a href="http://www.codewars.com/kata/linked-lists-insert-nth-node">Linked Lists - Insert Nth Node</a><br>
<a href="http://www.codewars.com/kata/linked-lists-sorted-insert">Linked Lists - Sorted Insert</a><br>
<a href="http://www.codewars.com/kata/linked-lists-insert-sort">Linked Lists - Insert Sort</a><br>
<a href="http://www.codewars.com/kata/linked-lists-append">Linked Lists - Append</a><br>
<a href="http://www.codewars.com/kata/linked-lists-remove-duplicates">Linked Lists - Remove Duplicates</a><br>
<a href="http://www.codewars.com/kata/linked-lists-move-node">Linked Lists - Move Node</a><br>
<a href="http://www.codewars.com/kata/linked-lists-move-node-in-place">Linked Lists - Move Node In-place</a><br>
<a href="http://www.codewars.com/kata/linked-lists-alternating-split">Linked Lists - Alternating Split</a><br>
<a href="http://www.codewars.com/kata/linked-lists-front-back-split">Linked Lists - Front Back Split</a><br>
<a href="http://www.codewars.com/kata/linked-lists-shuffle-merge">Linked Lists - Shuffle Merge</a><br>
<a href="http://www.codewars.com/kata/linked-lists-sorted-merge">Linked Lists - Sorted Merge</a><br>
<a href="http://www.codewars.com/kata/linked-lists-merge-sort">Linked Lists - Merge Sort</a><br>
<a href="http://www.codewars.com/kata/linked-lists-sorted-intersect">Linked Lists - Sorted Intersect</a><br>
<a href="http://www.codewars.com/kata/linked-lists-iterative-reverse">Linked Lists - Iterative Reverse</a><br>
<a href="http://www.codewars.com/kata/linked-lists-recursive-reverse">Linked Lists - Recursive Reverse</a><br>

Inspired by Stanford Professor Nick Parlante's excellent [Linked List teachings.](http://cslibrary.stanford.edu/103/LinkedListBasics.pdf)
