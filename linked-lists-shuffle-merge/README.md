# Linked Lists - Shuffle Merge

 - URL:[https://www.codewars.com/kata/55e5253dcd20f821c400008e](https://www.codewars.com/kata/55e5253dcd20f821c400008e)
 - Id: 55e5253dcd20f821c400008e
 - Language: python
 - Completed on: 2022-06-25T18:16:17.087Z
 - Tags: Linked Lists,Data Structures,Algorithms
 - Description:
Linked Lists - Shuffle Merge

Write a ShuffleMerge() function that takes two lists and merges their nodes together to make one list, taking nodes alternately between the two lists. So ShuffleMerge() with `1 -> 2 -> 3 -> null` and `7 -> 13 -> 1 -> null` should yield `1 -> 7 -> 2 -> 13 -> 3 -> 1 -> null`. If either list runs out, all the nodes should be taken from the other list. ShuffleMerge() should return the new list. The solution depends on being able to move nodes to the end of a list.

```javascript
var first = 3 -> 2 -> 8 -> null
var second = 5 -> 6 -> 1 -> 9 -> 11 -> null
shuffleMerge(first, second) === 3 -> 5 -> 2 -> 6 -> 8 -> 1 -> 9 -> 11 -> null
```

If one of the argument lists is null, the returned list should be the other linked list (even if it is also null). No errors need to be thrown in ShuffleMerge().

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
