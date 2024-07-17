# Find heavy ball - level: master

 - URL:[https://www.codewars.com/kata/544034f426bc6adda200000e](https://www.codewars.com/kata/544034f426bc6adda200000e)
 - Id: 544034f426bc6adda200000e
 - Language: python
 - Completed on: 2017-10-13T11:13:14.949Z
 - Tags: Puzzles,Logic,Riddles
 - Description:
There are 8 balls numbered from 0 to 7. 
Seven of them have the same weight. One is heavier. Your task is to find its number.

Your function `findBall` will receive single argument - `scales` object. The `scales` object contains an internally stored array of 8 elements (indexes 0-7), each having the same value except one, which is greater. It also has a public method named `getWeight(left, right)` which takes two arrays of indexes and returns -1, 0, or 1 based on the accumulation of the values found at the indexes passed are heavier, equal, or lighter.

`getWeight` returns:

`-1` if **left** pan is heavier

`1` if **right** pan is heavier

`0` if both pans weight the same

Examples of `scales.getWeight()` usage:

`scales.getWeight([3], [7])` returns `-1` if ball 3 is heavier than ball 7, `1` if ball 7 is heavier, or `0` i these balls have the same weight.

`scales.getWeight([3, 4], [5, 2])` returns `-1` if weight of balls 3 and 4 is heavier than weight of balls 5 and 2 etc.

So where's the catch, you may ask. Well - the scales is very old. You can use it only **TWICE** before the scale breaks.

``` if:python,ruby,crystal
**Note** - Use `scales.get_weight()` in the Python, Crystal and Ruby versions.
```
``` if:ocaml
**Note** - Use `scales#get_weight` in the OCaml version.
```

Too hard ? Try lower levels:

* [novice](http://www.codewars.com/kata/544047f0cf362503e000036e)
* [conqueror](http://www.codewars.com/kata/54404a06cf36258b08000364)

Still too easy ? Try this kata - [ubermaster](http://www.codewars.com/kata/find-heavy-ball-level-ubermaster) (made by by [bellmyer](http://www.codewars.com/users/bellmyer))
