# Time-like string format

 - URL:[https://www.codewars.com/kata/51e000d070fe4414000003f0](https://www.codewars.com/kata/51e000d070fe4414000003f0)
 - Id: 51e000d070fe4414000003f0
 - Language: javascript
 - Completed on: 2017-04-04T12:08:22.752Z
 - Tags: Strings,Formatting,Fundamentals
 - Description:
Build up a method that takes an integer and formats it to a 'time - like' format.
```if:csharp
The method must raise an `ArgumentException` if its hour length is less than 3 digits and greater than 4.
```
```if-not:csharp
The method must raise an exception if its hour length is less than 3 digits and greater than 4. 
```

### Example:

```coffeescript
solution(800) # should return '8:00'
solution(1000) # should return '10:00'
solution(1451) # should return '14:51'
solution(3351) # should return '33:51'
solution(10000) # should raise an exception
```
```javascript
solution(800); // should return '8:00'
solution(1000); // should return '10:00'
solution(1451); // should return '14:51'
solution(3351); // should return '33:51'
solution(10000); // should raise an exception
```
```csharp
Kata.Solution(800); // should return '8:00'
Kata.Solution(1000); // should return '10:00'
Kata.Solution(1451); // should return '14:51'
Kata.Solution(3351); // should return '33:51'
Kata.Solution(10000); // should raise an exception
```
