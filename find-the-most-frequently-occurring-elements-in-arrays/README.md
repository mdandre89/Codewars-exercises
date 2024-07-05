# Find the most frequently occurring elements in arrays

 - URL:[https://www.codewars.com/kata/578b44a47c77f5a1bd000011](https://www.codewars.com/kata/578b44a47c77f5a1bd000011)
 - Id: 578b44a47c77f5a1bd000011
 - Language: javascript
 - Completed on: 2022-06-19T12:56:46.814Z
 - Tags: Algorithms,Data Structures,Arrays,Optimization
 - Description:
<b>Input:</b> A 5-day JSON weather forecast which consist of 5 arrays. Each of the 5 arrays includes 8 numbers which represent 3-hourly temperature forecast for a given day.

<b>Output:</b> An array which includes the most frequent number (temperature) from each of the 5 arrays (days). In case there is a tie, return the value present later in a given array (day).

Example input:

var forecast_01 = {<br>
&nbsp;&nbsp; "temperature": [<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;    [15,17,19,21,21,21,20,16],<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;    [16,17,22,22,22,22,20,16],<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;    [12,17,19,20,20,20,20,18],<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;    [14,15,19,19,20,22,18,17],<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;    [15,17,24,24,24,20,20,20]<br>
&nbsp;&nbsp;  ]<br>
};

Example output:

`getMostFrequent(forecast_01)  // should return [21,22,20,19,20]`

Explanation of the example above:

The output is `[21,22,20,19,20]` because given 5 arrays, <br> 
`[15,17,19,21,21,21,20,16]` 21 is the most frequent in 1st array<br>
`[16,17,22,22,22,22,20,16]` 22 is the most frequent in 2nd array<br>
`[12,17,19,20,20,20,20,18]` 20 is the most frequent in 3rd array<br>
`[14,15,19,19,20,22,18,17]` 19 is the most frequent in 4th array<br>
`[15,17,24,24,24,20,20,20]` 24 and 20 appear 3 times each in 5th array so 20 is included in the output as the last 20 appears later than the last 24.
