# Tree leaves at same level

 - URL:[https://www.codewars.com/kata/52d43d5515be7cbc92000611](https://www.codewars.com/kata/52d43d5515be7cbc92000611)
 - Id: 52d43d5515be7cbc92000611
 - Language: javascript
 - Completed on: 2022-06-12T15:32:06.807Z
 - Tags: Trees,Data Structures,Recursion,Algorithms
 - Description:
A binary tree is a structure that has a value and two references to its child: left and right. Each of these references are themselves a binary tree or undefined to represent an empty tree.

The leaves in a binary tree are the lower level nodes for which both references (left and right) are undefined. For example, in the following tree:

```
  a
 / \
b  c
    \
    d
```

'b' and 'd' are leaves while 'a' and 'c' are not.
We define the level of a tree as the number of parent nodes a tree node has. The root of the tree, therefore, is at level 0. Root's children are at level 1, etc.

The goal of this kata is to write a function to determine if all leaves of a binary tree are at the same level.
In the tree shown before the function should return false since 'b' and 'd' are at levels 1 and 2, respectively.

In the following example, the function should return true because now the leaves are 'e' and 'd' and both are at level 2:

```
   a
  / \
 b   c
 /    \
e      d
```

In this next example:
```
    a
   / 
  b  
 /  
e 
```
the function should also return true because 'e' is the only leaf.

If the function is passed an empty tree (undefined) it should return true. Similarly, if the tree has only 1 node (the root node) the function should return true.

The Node class can be used as follows:
``` javascript
var n = Node(1,undefined,Node(2,undefined,undefined));
var nLeft = n.getLeft();
var nRight = n.getRight();
```
