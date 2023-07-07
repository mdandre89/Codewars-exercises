# Northwest and Southeast corners 

 - URL:[https://www.codewars.com/kata/58ed139326f519019a000053](https://www.codewars.com/kata/58ed139326f519019a000053)
 - Id: 58ed139326f519019a000053
 - Language: python
 - Completed on: 2017-11-16T11:40:48.794Z
 - Tags: Mathematics,Fundamentals
 - Description:
Everyday we go to different places to get our things done. Those places can be represented by specific location points `[ [<lat>, <long>], ... ]` on a map. I will be giving you an array of arrays that contain coordinates of the different places I had been on a particular day. Your task will be to find `peripheries (outermost edges)` of the bounding box that contains all the points. The response should only contain `Northwest and Southeast` points as follows: `{ "nw": [<lat>, <long>], "se": [ <lat>, <long>] }`. You are adviced to draw the points on a 2D plan to visualize:

```
                         N
                         ^
    p(nw)  ______________|________________
          |              |                |
          |              | all other      |   
          |              |  points        |
          |              |                |
     ----------------------------------------> E          
          |              |                |
          |  all other   |                |
          |  points      |                |
          |______________|________________|
                         |                  p(se)
```
