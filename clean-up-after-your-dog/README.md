# Clean up after your dog

 - URL:[https://www.codewars.com/kata/57faa6ff9610ce181b000028](https://www.codewars.com/kata/57faa6ff9610ce181b000028)
 - Id: 57faa6ff9610ce181b000028
 - Language: python
 - Completed on: 2017-08-13T19:33:05.949Z
 - Tags: Fundamentals,Strings,Arrays,Mathematics
 - Description:
You have stumbled across the divine pleasure that is owning a dog and a garden. Now time to pick up all the cr@p! :D

Given a 2D array to represent your garden, you must find and collect all of the dog cr@p - represented by '@'.

You will also be given the number of bags you have access to (bags), and the capactity of a bag (cap). If there are no bags then you can't pick anything up, so you can ignore cap.

You need to find out if you have enough capacity to collect all the cr@p and make your garden clean again. 

If you do, return 'Clean', else return 'Cr@p'.

Watch out though - if your dog is out there ('D'), he gets very touchy about being watched. If he is there you need to return 'Dog!!'.

For example:

x=<br>
[[\_,\_,\_,\_,\_,\_]<br>
 [\_,\_,\_,\_,@,\_]<br>
 [@,\_,\_,\_,\_,\_]]

bags = 2, cap = 2

return  --> 'Clean'
