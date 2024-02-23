# How far can you pedal a bike???

 - URL:[https://www.codewars.com/kata/5a0f593a1bae7bd7ca000159](https://www.codewars.com/kata/5a0f593a1bae7bd7ca000159)
 - Id: 5a0f593a1bae7bd7ca000159
 - Language: javascript
 - Completed on: 2022-06-09T21:00:36.706Z
 - Tags: Puzzles,Fundamentals,Algorithms,Games
 - Description:
# Explanation

You are a velodrome cycling coach and devising new drills for your team to assess the distance they can cover in a set amount of time. Being a coach you're a bit of a control freak so you are dictating the gear that they have to ride in, as well as how fast they turn the pedals.

You task is to work out how far in kilometers a cyclist can travel in a certain period of time (time), a given gear (gear) and an enforced speed at which they have to turn the pedals (cadence).

## Time
Provided in minutes and will always be a positive integer less than or equal to 300.

## Cadence
The number of full pedal revolultions per minute and will always be a positive integer between 50 and 120 inclusive (reflecting a normal cycling cadence in the real world).

## Gears
Gears are expressed by the number of teeth on the front chainring and the number of gears on the rear cog. The gears argument will be provided as a string with the number of front teeth and number of rear teeth (in that order) separated by an "x" character. E.g. A 53 tooth chainring on the front and an 11 tooth cog on the back would be expresssed as "53x11". To reflect modern road bike gears, the front chainring will always be either 39 tooth or 53 tooth, and the rear will always be any positive integer between 11 and 25 teeth inclusive.

We can can caclulate the forward motion of a bicycle with the system 'metres of development', which measures the distance travelled in meters with each turn of the crank. Metres of development is calculated with the formula:

![alt text](http://res.cloudinary.com/jamesriall/image/upload/v1511023861/gear-inches_q0vmqk.png "Meters of development")

The drive wheel circumference of the bikes being used is 2.11115 meters.

## Output
The product of the function should be a string of the following format:

"You cycled 55.745 kilometers!"

The kilometers cycled should always be provided to three decimal places.

Bon chance!

![alt text](http://cycling-passion.com/wp-content/uploads/2014/09/Eddy-Merckx-Hour-Record-Mexico-City-1972.jpg "Eddy Merckx")
