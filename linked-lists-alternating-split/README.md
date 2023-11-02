# Linked Lists - Alternating Split

 - URL:[https://www.codewars.com/kata/55dd5386575839a74f0000a9](https://www.codewars.com/kata/55dd5386575839a74f0000a9)
 - Id: 55dd5386575839a74f0000a9
 - Language: python
 - Completed on: 2022-06-25T13:15:23.390Z
 - Tags: Data Structures,Linked Lists,Fundamentals
 - Description:
Linked Lists - Alternating Split

Write an AlternatingSplit() function that takes one list and divides up its nodes to make two smaller lists. The sublists should be made from alternating elements in the original list. So if the original list is `a -> b -> a -> b -> a -> null` then one sublist should be `a -> a -> a -> null` and the other should be `b -> b -> null`.

###JavaScript
```javascript
var list = 1 -> 2 -> 3 -> 4 -> 5 -> null
alternatingSplit(list).first === 1 -> 3 -> 5 -> null
alternatingSplit(list).second === 2 -> 4 -> null
```
###Python
```python
list = 1 -> 2 -> 3 -> 4 -> 5 -> None
alternating_split(list).first == 1 -> 3 -> 5 -> None
alternating_split(list).second == 2 -> 4 -> None
```
###Ruby
```ruby
list = 1 -> 2 -> 3 -> 4 -> 5 -> nil
alternating_split(list).first == 1 -> 3 -> 5 -> nil
alternating_split(list).second == 2 -> 4 -> nil
```

For simplicity, we use a Context object to store and return the state of the two linked lists. A Context object containing the two mutated lists should be returned by AlternatingSplit().

If the passed in head node is null/None/nil or a single node, throw an error.

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
