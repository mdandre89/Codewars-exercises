# Linked Lists - Insert Nth Node

 - URL:[https://www.codewars.com/kata/55cacc3039607536c6000081](https://www.codewars.com/kata/55cacc3039607536c6000081)
 - Id: 55cacc3039607536c6000081
 - Language: python
 - Completed on: 2022-06-25T12:49:54.124Z
 - Tags: Linked Lists,Data Structures,Fundamentals
 - Description:
Linked Lists - Insert Nth

Implement an InsertNth() function (`insert_nth()` in PHP) which can insert a new node at any index within a list.

InsertNth() is a more general version of the Push() function that we implemented in the first kata listed below.  Given a list, an index 'n' in the range 0..length, and a data element, add a new node to the list so that it has the given index. InsertNth() should return the head of the list.

```javascript
insertNth(1 -> 2 -> 3 -> null, 0, 7) === 7 -> 1 -> 2 -> 3 -> null)
insertNth(1 -> 2 -> 3 -> null, 1, 7) === 1 -> 7 -> 2 -> 3 -> null)
insertNth(1 -> 2 -> 3 -> null, 3, 7) === 1 -> 2 -> 3 -> 7 -> null)
```

```php
insert_nth(1 -> 2 -> 3 -> NULL, 0, 7); // 7 -> 1 -> 2 -> 3 -> NULL
insert_nth(1 -> 2 -> 3 -> NULL, 1, 7); // 1 -> 7 -> 2 -> 3 -> NULL
insert_nth(1 -> 2 -> 3 -> NULL, 3, 7); // 1 -> 2 -> 3 -> 7 -> NULL
insert_nth(1 -> 2 -> 3 -> NULL, 4, 7); // throws new InvalidArgumentException
```

```csharp
Node.InsertNth(1 -> 2 -> 3 -> null, 0, 7)  => 7 -> 1 -> 2 -> 3 -> null
Node.InsertNth(1 -> 2 -> 3 -> null, 1, 7)  => 1 -> 7 -> 2 -> 3 -> null
Node.InsertNth(1 -> 2 -> 3 -> null, 3, 7)  => 1 -> 2 -> 3 -> 7 -> null
Node.InsertNth(1 -> 2 -> 3 -> null, -2, 7) // throws new ArgumentException
```

You must throw/raise an exception (`ArgumentOutOfRangeException` in C#, `InvalidArgumentException` in PHP) if the index is too large.

The push() and buildOneTwoThree() (`build_one_two_three()` in PHP) functions do not need to be redefined.  The `Node` class is also preloaded for you in PHP.

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
