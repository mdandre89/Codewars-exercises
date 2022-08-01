# Valid Binary Christmas Tree

 - URL:[https://www.codewars.com/kata/52aebd2423b44356b8000578](https://www.codewars.com/kata/52aebd2423b44356b8000578)
 - Id: 52aebd2423b44356b8000578
 - Language: javascript
 - Completed on: 2022-06-12T17:32:05.151Z
 - Tags: Trees,Data Structures,Validation,Algorithms
 - Description:
### Happy Holidays fellow Code Warriors!
Santa just finished taking a data structures course, and thought it would be a great idea to build a Binary Christmas Tree! All of Santa's helpers created a Binary Christmas Tree, but not all of them meet his requirements. Can you write some code to validate the Binary Christmas Trees?

### Valid Binary Christmas Tree
Write a function `isValidTree` that accepts a Binary Tree, and returns true if it meets Santa's requirements, false otherwise. Since the tree is a binary tree, each node can have 0, 1, or 2 children. The `left` and `right` properties can be used to access the current nodes left and right children. All nodes have an `ornament` property, which is the name of the ornament, and a `color` property, which  represents the color of the `ornament`.

### Santa's Binary Christmas Tree Requirements
A valid Binary Christmas Tree will meet the following requirements:
<ul>
<li>Root node has a 'star' ornament</li>
<li>Nodes with zero children (excluding the root node) have a 'blue' colored ornament</li>
<li>Nodes with one or two children (excluding the root node) have a 'red' colored ornament</li>
</ul>

### Examples:
```javascript
isValidTree( {
  ornament: 'star', 
  color: 'yellow'
} )// => returns true

isValidTree( {
  ornament: 'star',
  color: 'yellow',
  left: {
    ornament: 'candy cane',
    color: 'blue'
  }
} )// => returns true

isValidTree( {
  ornament: 'star',
  color: 'yellow',
  right: {
    ornament: 'stocking',
    color: 'red'
  }
} )// => returns false

```
