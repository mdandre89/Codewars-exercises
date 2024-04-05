# Greatest Position Distance Between Matching Array Values

 - URL:[https://www.codewars.com/kata/5442e4fc7fc447653a0000d5](https://www.codewars.com/kata/5442e4fc7fc447653a0000d5)
 - Id: 5442e4fc7fc447653a0000d5
 - Language: python
 - Completed on: 2017-11-16T12:13:03.754Z
 - Tags: Algorithms
 - Description:
The goal of this Kata is to return the greatest distance of index positions between matching number values in an array or 0 if there are no matching values.  

Example:
In an array with the values [0, 2, 1, 2, 4, 1] the greatest index distance is between the matching '1' values at index 2 and 5.  Executing greatestDistance against this array would return 3. (i.e. 5 - 2)  

Here's the previous example in test form:
```javascript
Test.assertEquals(greatestDistance([0, 2, 1, 2, 4, 1]), 3);
```
```python
test.assert_equals(greatest_distance([0, 2, 1, 2, 4, 1]), 3)
```
```csharp
Assert.AreEqual(3, GreatestDistance.Exec(new List<int> { 0, 2, 1, 2, 4, 1 }));
```

This is based on a Kata I had completed only to realize I has misread the instructions.  I enjoyed solving the problem I thought it was asking me to complete so I thought I'd add a new Kata for others to enjoy.  There are no tricks in this one, good luck!
