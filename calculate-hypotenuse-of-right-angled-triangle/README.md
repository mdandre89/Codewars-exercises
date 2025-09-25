# Calculate Hypotenuse of Right-angled Triangle

 - URL:[https://www.codewars.com/kata/525a3d6b85a9a47fcf00055a](https://www.codewars.com/kata/525a3d6b85a9a47fcf00055a)
 - Id: 525a3d6b85a9a47fcf00055a
 - Language: javascript
 - Completed on: 2017-08-18T16:06:36.293Z
 - Tags: Mathematics,Algorithms
 - Description:
To solve this Kata, complete the function, calculateHypotenuse(a,b), which will return the length of the hyptenuse for a right angled triangle with the other two sides having a length equal to the inputs.  More details:

- The returned value should be a number rounded to three decimal places
- An error (`ArgumentException` in C#) should be thrown if an invalid input is provided (inputs should both be numbers that are above zero)

```javascript
calculateHypotenuse(1,1); // returns 1.414
calculateHypotenuse(3,4); // returns 5
calculateHypotenuse(-2,1); // throws error
calculateHypotenuse("one", "two"); // throws error
```

```coffeescript
calculateHypotenuse(1,1); # returns 1.414
calculateHypotenuse(3,4); # returns 5.000
calculateHypotenuse(-2,1); # throws error
calculateHypotenuse("one", "two"); # throws error
```

```ruby
calculateHypotenuse(1,1) # returns 1.414
calculateHypotenuse(3,4) # returns 5
calculateHypotenuse(-2,1) # raises exception
calculateHypotenuse("one", "two") # raises exception
```

```csharp
Kata.CalculateHypotenuse(1,1)           // returns 1.414
Kata.CalculateHypotenuse(3,4)           // returns 5
Kata.CalculateHypotenuse(-2,1)          // throws ArgumentException
Kata.CalculateHypotenuse(2, Double.NaN) // throws ArgumentException
```

For more information on the hypotenuse, visit: http://en.wikipedia.org/wiki/Hypotenuse
