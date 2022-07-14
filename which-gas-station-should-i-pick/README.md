# Which Gas Station should I pick?

 - URL:[https://www.codewars.com/kata/5877839c0594a6ead600012c](https://www.codewars.com/kata/5877839c0594a6ead600012c)
 - Id: 5877839c0594a6ead600012c
 - Language: python
 - Completed on: 2017-10-15T14:02:08.407Z
 - Tags: Mathematics,Fundamentals
 - Description:
<h2>Which Gas Station should I pick?</h2>
<br>
You have to fill up your gas and there are multiple gas stations with different prices and different distance to you. Sometimes it is cheaper to drive to a more distant gas station, because the prices are cheaper!
<br>
<br>
<ul>
<li>Your tank can contain 60l at maximum.</li>
<li>You always fill your tank full</li>
<li>Calculate the current fuel in tank with the actual price of the gas stations</li>
</ul>



<h3> Your task: </h3>

Given an object with multiple gas stations, your currentFuel as integer between 0 and 60 and the fuel consumption of your car (l/100km, float) - <code>find the cheapest gas station and return the name of the gas station!</code>
<br>
<br>
Return <code>undefined (in JS) | None (in Python)</code> if there are no gas station or your fuel is not enough to reach one!
<br>
<br>
No need to test for invalid input! <br>
Remember: You also need fuel to drive to the gas station! The way back home should also be considered :)

<h4> Example </h4>

<pre>
<code>
var obj = {
            "gas_station1": {"price": 1.5, "distance": 50},
            "gas_station2": {"price": 2.0, "distance": 75}
          };
var currentFuel = 35;
var fuelConsumption = 7.5;

costs gas_station1 = 48.75; <- is cheaper
costs gas_station2 = 72.5;

#distance: distance between you and the gasstation in km
#fuelConsumption: how much your car consumes in l/100km
#currentFuel: your current fuel in l

</code>
</pre>
