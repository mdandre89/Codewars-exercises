# Clock in Mirror

 - URL:[https://www.codewars.com/kata/56548dad6dae7b8756000037](https://www.codewars.com/kata/56548dad6dae7b8756000037)
 - Id: 56548dad6dae7b8756000037
 - Language: python
 - Completed on: 2017-05-24T16:56:17.759Z
 - Tags: Fundamentals
 - Description:
Peter can see a clock in the mirror from the place he sits in the office.
When he saw the clock shows 12:22

<svg width="200" height="200">
    <circle cx="100" cy="100" r="92" stroke="black" stroke-width="4" fill="white"/>
    <text x="135" y=" 40" fill="black">1</text>
    <text x="165" y=" 68" fill="black">2</text>
    <text x="174" y="105" fill="black">3</text>
    <text x="165" y="145" fill="black">4</text>
    <text x="135" y="175" fill="black">5</text>
    <text x=" 96" y="185" fill="black">6</text>
    <text x=" 58" y="175" fill="black">7</text>
    <text x=" 28" y="145" fill="black">8</text>
    <text x=" 15" y="105" fill="black">9</text>
    <text x=" 25" y=" 68" fill="black">10</text>
    <text x=" 55" y=" 40" fill="black">11</text>
    <text x=" 92" y=" 25" fill="black">12</text>
    <line x1="100" y1="100" x2="110" y2=" 51" stroke="black" stroke-width="5"/>
    <line x1="100" y1="100" x2="152" y2="146" stroke="black" stroke-width="5"/>
</svg>

He knows that the time is 11:38

<svg width="200" height="200">
    <circle cx="100" cy="100" r="92" stroke="black" stroke-width="4" fill="white"/>
    <text x="135" y=" 40" fill="black">1</text>
    <text x="165" y=" 68" fill="black">2</text>
    <text x="174" y="105" fill="black">3</text>
    <text x="165" y="145" fill="black">4</text>
    <text x="135" y="175" fill="black">5</text>
    <text x=" 96" y="185" fill="black">6</text>
    <text x=" 58" y="175" fill="black">7</text>
    <text x=" 28" y="145" fill="black">8</text>
    <text x=" 15" y="105" fill="black">9</text>
    <text x=" 25" y=" 68" fill="black">10</text>
    <text x=" 55" y=" 40" fill="black">11</text>
    <text x=" 92" y=" 25" fill="black">12</text>
    <line x1="100" y1="100" x2="90" y2=" 51" stroke="black" stroke-width="5"/>
    <line x1="100" y1="100" x2="48" y2="146" stroke="black" stroke-width="5"/>
</svg>

in the same manner:

05:25 --> 06:35

01:50 --> 10:10

11:58 --> 12:02

12:01 --> 11:59

Please complete the function `WhatIsTheTime(timeInMirror)`, where `timeInMirror` is the mirrored time (what Peter sees) as string.

Return the _real_ time as a string.

Consider hours to be between 1 <= hour < 13.

So there is no 00:20, instead it is 12:20.

There is no 13:20, instead it is 01:20.
