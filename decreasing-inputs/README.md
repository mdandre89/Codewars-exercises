# Decreasing  Inputs

 - URL:[https://www.codewars.com/kata/555de49a04b7d1c13c00000e](https://www.codewars.com/kata/555de49a04b7d1c13c00000e)
 - Id: 555de49a04b7d1c13c00000e
 - Language: python
 - Completed on: 2017-09-13T10:08:57.129Z
 - Tags: Arrays,Basic Language Features,Language Features,Fundamentals
 - Description:
This kata is all about adding numbers.

You will create a function named add. It will return the sum of all the arguments. Sounds easy, doesn't it?

Well Here's the Twist. The inputs will gradually decrease with their index as parameter to the function.


```javascript
  add(3,4,6); 
  /*
  returns ( 3 / 1 ) + ( 4 / 2 ) + ( 6 / 3 ) = 7
  */
```
```ruby
  add(3,4,6) #returns (3/1)+(4/2)+(6/3)=7
```
```python
  add(3,4,6) #returns (3/1)+(4/2)+(6/3)=7
```

Remember the function will return 0 if no arguments are passed and it must round the result if sum is a float.

Example
```javascript
  add(); //=> 0
  add(1,2,3); //=> 3
  add(1,4,-6,20); //=> 6
```
```ruby
  add() #=> 0
  add(1,2,3) #=> 3
  add(1,4,-6,20) #=> 6
```
```python
  add() #=> 0
  add(1,2,3) #=> 3
  add(1,4,-6,20) #=> 6
```

Check my another kata here!! http://www.codewars.com/kata/555b73a81a6285b6ce000047

