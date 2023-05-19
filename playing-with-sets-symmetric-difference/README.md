# Playing with Sets : Symmetric difference

 - URL:[https://www.codewars.com/kata/5884f4727987a2a561000147](https://www.codewars.com/kata/5884f4727987a2a561000147)
 - Id: 5884f4727987a2a561000147
 - Language: javascript
 - Completed on: 2017-08-13T19:42:53.043Z
 - Tags: Sets,Data Structures,Fundamentals
 - Description:
[Set](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set) objects are new JavaScript built-in objects defined since [ECMAScript 2015](http://www.ecma-international.org/ecma-262/6.0/#sec-set-objects.)

A **Set** lets you store unique values of any type. It comes with some useful methods like `.add`, `.clear`, `.has` . . . **BUT** some "Set operations" are missing, like . . . 

# Symmetric difference

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/4/46/Venn0110.svg/330px-Venn0110.svg.png" style="max-width:200px">

The **symmetric difference** is an extension of the [complement](https://www.codewars.com/kata/playing-with-sets-complement). Denoted `A Δ B`,  it's the set of all element of A which **are not** element of B and all element of B which **are not** element of A.

### Example:
```
{7,8,9,10} Δ {9,10,11,12} = {7,8,11,12}.
```

# Task

Create function `symDiff` getting 2 sets as arguments and returning a **new Set** as result of symmetric difference of these sets.

### Examples:
```javascript
A = new Set([1,2,3]);
B = new Set([2,3,4]);

symDiff(A,B) // -> {1,4}
```

**Note**: as I've got some problem outputting "`Δ`" in tests, I will use "`^`" instead of it.

&nbsp;

" May the Code be with you ! "
<img src="https://en.wikipedia.org/w/extensions/wikihiero/img/hiero_E20.png" align="right" title="There's more than ONE Set!">
