# Cycle a list of values

 - URL:[https://www.codewars.com/kata/5456812629ccbf311b000078](https://www.codewars.com/kata/5456812629ccbf311b000078)
 - Id: 5456812629ccbf311b000078
 - Language: javascript
 - Completed on: 2017-09-04T13:42:06.682Z
 - Tags: Algorithms
 - Description:
## Prologue

You're part of a team porting MS Paint into the browser and currently working on a new UI component that allows user to control the canvas zoom level.

According to the wireframes delivered to you in PowerPoint format the user should be able to *cycle* through specified zoom levels by clicking a button in the UI repeatedly. The reverse direction should work with shift key held.

A new function is needed to support this behavior, so you alt-tab to Visual Studio and get to work.

--- 

## Instructions

Implement a function which when given the arguments

1. Direction to which to cycle the current value
2. List of values
3. Current value

returns the value next to current value in the specified direction.

The function should pick the next value from the other side of the list in case there are no values in the given direction.

## Examples

``` haskell
cycleList R [1,2,3] 1  -- => Just 2
cycleList L [1,2,3] 1  -- => Just 3
cycleList R [1,2,3] 0  -- => Nothing
cycleList L ["foo", "bar", "xyz"] "bar"  -- => Just "foo"
```
``` javascript
cycle(1, [1,2,3], 1)   // => 2
// Given the direction 1, returns the value next to 1 on the right

cycle(-1, [1,2,3], 1)  // => 3
// Given the direction -1 and value 1, wraps around list returning the last element

cycle(1, [1,2,3], 0)   // => null
// 0 does not exist in the list, returns null

cycle(1, [1,2,2,3], 2) // => 2
// Corner case: multiple instances of given value, picks next relative to first occurrence
```
``` coffeescript
# Given the direction 1, returns the value next to 1 on the right
cycle(1, [1,2,3], 1)   # => 2

# Given the direction -1 and value 1, wraps around list returning the last element
cycle(-1, [1,2,3], 1)  # => 3

# 0 does not exist in the list, returns null
cycle(1, [1,2,3], 0)   # => null

# Corner case: multiple instances of given value, picks next relative to first occurrence
cycle(1, [1,2,2,3], 2) # => 2
```
``` python
# Given the direction 1, returns the value next to 1 on the right
cycle(1, [1,2,3], 1)   # => 2

# Given the direction -1 and value 1, wraps around list returning the last element
cycle(-1, [1,2,3], 1)  # => 3

# 0 does not exist in the list, returns null
cycle(1, [1,2,3], 0)   # => null

# Corner case: multiple instances of given value, picks next relative to first occurrence
cycle(1, [1,2,2,3], 2) # => 2
```
