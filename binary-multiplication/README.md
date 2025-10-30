# Binary multiplication.

 - URL:[https://www.codewars.com/kata/596a81352240711f3b00006e](https://www.codewars.com/kata/596a81352240711f3b00006e)
 - Id: 596a81352240711f3b00006e
 - Language: python
 - Completed on: 2018-01-25T11:33:54.248Z
 - Tags: Mathematics,Puzzles,Algorithms
 - Description:
You will be given two numbers `m,n`. The numbers could span from `0` to `10000`. We can get their product by using binary reduction as show in the table below.
<p>Example (to understand the table please read the description below it) </p>
<table>
  <colgroup>
    <col span="2">
  </colgroup>
  <tr>
    <th>real value of m(r)</th>
    <th>m</th>
    <th>n</th>
    <th>(r*n)</th>
  </tr>
  <tr>
    <td>0</td>
    <td>100</td>
    <td>15</td>
    <td>0</td>
  </tr>
    <tr>
    <td>0</td>
    <td>50</td>
    <td>30</td>
    <td>0</td>
  </tr>
    <tr>
    <td>1</td>
    <td>25</td>
    <td>60</td>
    <td>60</td>
  </tr>  
  <tr>
    <td>0</td>
    <td>12</td>
    <td>120</td>
    <td>0</td>
  </tr>
    <tr>
    <td>0</td>
    <td>6</td>
    <td>240</td>
    <td>0</td>
  </tr>
    <tr>
    <td>1</td>
    <td>3</td>
    <td>480</td>
    <td>480</td>
  </tr>
    <tr>
    <td>1</td>
    <td>1</td>
    <td>960</td>
    <td>960</td>
  </tr>
</table>

Above, we are given two numbers `100` and `15`. we keep reducing the bigger number by dividing it by `2` and hold the integer part of the division till it is no more divisible by `2`. Then we assign the real values to these reduced parts of `m`. Any reduced number `[1,m]` has real value of `0` if it is even, and it will have real value of `1` if it is odd. On the other hand the smaller number in this case `n` keeps on doubling itself the same amount of times `m` reduces itself. The idea of this method is to change multiplication of two big number to a sequence of multiplication by `0` or `1` and perform addition to get the final product. You can see that from the last column `(r*n)` above.</br> 
if we sum the last column we get `0+60+0+0+480+960=1500=100*15`
Now your task for this kata will be to get those non-zero number in the last column in an array and return it sorted in descending order.so for the above example the return will be `[960,480,60]`.

_Beware: _`m,n`_ are not necessarily ordered._
