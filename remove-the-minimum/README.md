# Remove the minimum

 - URL:[https://www.codewars.com/kata/563cf89eb4747c5fb100001b](https://www.codewars.com/kata/563cf89eb4747c5fb100001b)
 - Id: 563cf89eb4747c5fb100001b
 - Language: python
 - Completed on: 2017-03-07T19:50:36.301Z
 - Tags: Lists,Data Structures,Arrays,Fundamentals
 - Description:
# The museum of incredible dull things

The museum of incredible dull things wants to get rid of some exhibitions. Miriam, the interior architect, comes up with a plan to remove the most boring exhibitions. She gives them a rating, and then removes the one with the lowest rating.

However, just as she finished rating all exhibitions, she's off to an important fair, so she asks you to write a program that tells her the ratings of the items after one removed the lowest one. Fair enough.

# Task

Given an array of integers, remove the smallest value. <span style="color:red">**Do not mutate the original array/list**</span>. If there are multiple elements with the same value, remove the one with a lower index. If you get an empty array/list, return an empty array/list.

Don't change the order of the elements that are left.

### Examples

```
* Input: [1,2,3,4,5], output= [2,3,4,5]
* Input: [5,3,2,1,4], output = [5,3,2,4]
* Input: [2,2,1,2,1], output = [2,2,2,1]
```

