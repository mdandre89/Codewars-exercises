# The Rhinestone Cowboy  ~ Count the dollars in his boots!

 - URL:[https://www.codewars.com/kata/58a2a561f749ed763c00000b](https://www.codewars.com/kata/58a2a561f749ed763c00000b)
 - Id: 58a2a561f749ed763c00000b
 - Language: python
 - Completed on: 2017-04-08T13:18:26.011Z
 - Tags: Fundamentals
 - Description:
<h2>The Rhinestone Cowboy - Count the dollars in his boots!</h2>
```
           ,|___|,       
           |     |
           |     |
           |     |
           | ==  |        
           |[(1)]|
           /    &|        
       .-'`  ,   )****      
       |         |   **
       `~~~~~~~~~~    ^
            ^
            |
     One Dollar Bill

           ,|___|,       
           |     |
           |     |
           |[(1)]|
           | ==  |        
           |[(1)]|
           /    &|        
       .-'`  ,   )****      
       |         |   **
       `~~~~~~~~~~    ^
            ^
            |
     Two Dollar Bills
 
           ,|___|,       
           |[{1}]|  <---- not a bill   
           |     |
           |[(1)]|
           | ==  |        
           |[(1)]|
           /    &|  <---- top is above the "&"   
       .-'`  ,   )****      
       |         |   **
       `~~~~~~~~~~    ^
             ^
             |
     Two Dollar Bills

```
<h2>Task</h2>
You will receive an array of two strings with the Cowboys boots. Count the number of dollars in each boot and return a string such as: 

"This Rhinestone Cowboy has 2 dollar bills in his right boot and 1 in the left"
```
boots[0] = left boot
boots[1] = right boot
```

The bill must be of form ```[(1)]``` to be counted and only count ones no other denominations. Only count bills in the top half of the boot(boot leg) so the cowboy can pull money out without removing the boots, see diagram above.

The test boots will be well-formed and always the same size.

You will always be given two boots since a Cowboy cannot walk around barefoot!

Dedicated to one of the coolest dudes ever.... 
Glen Campbell
=> https://www.youtube.com/watch?v=8kAU3B9Pi_U
