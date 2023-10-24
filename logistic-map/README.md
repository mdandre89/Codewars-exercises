# Logistic Map

 - URL:[https://www.codewars.com/kata/5779624bae28070489000146](https://www.codewars.com/kata/5779624bae28070489000146)
 - Id: 5779624bae28070489000146
 - Language: python
 - Completed on: 2018-02-13T16:04:03.902Z
 - Tags: Graph Theory,Graphs,Data Structures,Matrix,Arrays,Lists,Algorithms
 - Description:
Our AAA company is in need of some software to help with logistics: you will be given the width and height of a map, a list of x coordinates and a list of y coordinates of the supply points, starting to count from the top left corner of the map as 0.

Your goal is to return a two dimensional array/list with every item having the value of the distance of the square itself from the closest supply point expressed as a simple integer.

Quick examples:

```python
logistic_map(3,3,[0],[0])
#returns
#[[0,1,2],
# [1,2,3],
# [2,3,4]]
logistic_map(5,2,[0,4],[0,0])
#returns
#[[0,1,2,1,0],
# [1,2,3,2,1]]
```
```ruby
logistic_map(3,3,[0],[0])
#returns
#[[0,1,2],
# [1,2,3],
# [2,3,4]]
logistic_map(5,2,[0,4],[0,0])
#returns
#[[0,1,2,1,0],
# [1,2,3,2,1]]
```
```javascript
logisticMap(3,3,[0],[0])
//returns
//[[0,1,2],
// [1,2,3],
// [2,3,4]]
logisticMap(5,2,[0,4],[0,0])
//returns
//[[0,1,2,1,0],
// [1,2,3,2,1]]
```
```csharp
LogisticMap(3,3,{0},{0})
//returns
//{{0,1,2},
// {1,2,3},
// {2,3,4}}
LogisticMap(5,2,{0,4},{0,0})
//returns
//{{0,1,2,1,0},
// {1,2,3,2,1}}
```
```dart
logisticMap(3,3,[0],[0])
//returns
//[[0,1,2],
// [1,2,3],
// [2,3,4]]
logisticMap(5,2,[0,4],[0,0])
//returns
//[[0,1,2,1,0],
// [1,2,3,2,1]]
```

Remember that our company is operating with trucks, not drones, so you can simply use <a href="https://en.wikipedia.org/wiki/Taxicab_geometry">Manhattan distance</a>. If supply points are present, they are going to be within the boundaries of the map; if no supply point is present on the map, just return `None`/`nil`/`null` in every cell.

```python
logistic_map(2,2,[],[])
#returns
#[[None,None],
# [None,None]]
```
```ruby
logistic_map(2,2,[],[])
#returns
#[[None,None],
# [None,None]]
```
```javascript
logisticMap(2,2,[],[])
//returns
//[[None,None],
// [None,None]]
```
```csharp
LogisticMap(2,2,{},{})
//returns
//{{-1,-1},
// {-1,-1}}
```
```dart
logisticMap(2,2,[],[])
//returns
//[[null,null],
// [null,null]]
```

**Note:** this one is taken (and a bit complicated) from a problem a real world AAA company [whose name I won't tell here] used in their interview. It was done by a friend of mine. It is nothing that difficult and I assume it is their own version of the FizzBuzz problem, but consider candidates were given about 30 mins to solve it.
