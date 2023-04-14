# Regular expression for binary numbers divisible by 5

 - URL:[https://www.codewars.com/kata/5647c3858d4acbbe550000ad](https://www.codewars.com/kata/5647c3858d4acbbe550000ad)
 - Id: 5647c3858d4acbbe550000ad
 - Language: python
 - Completed on: 2017-11-07T15:32:09.003Z
 - Tags: Binary,Algorithms,Regular Expressions
 - Description:
Define a regular expression which tests if a given string representing a binary number is divisible by 5.

### Examples:

```csharp
// 5 divisable by 5
Regex.IsMatch('101', DivisibleByFive) == true

// 135 divisable by 5
Regex.IsMatch('10000111', DivisibleByFive) == true

// 666 not divisable by 5
Regex.IsMatch('0000001010011010', DivisibleByFive) == false
```
```javascript
// 5 divisable by 5
divisibleByFive.test('101') === true

// 135 divisable by 5
divisibleByFive.test('10000111') === true

// 666 not divisable by 5
divisibleByFive.test('0000001010011010') === false
```
```php
// 5 is divisible by 5
preg_match($pattern, '101'); // => 1
// 135 is divisible by 5
preg_match($pattern, '10000111'); // => 1
// 666 is not divisible by 5
preg_match($pattern, '0000001010011010'); // => 0
```
```python
# 5 divisible by 5
PATTERN.match('101') == true

# 135 divisible by 5
PATTERN.match('10000111') == true

# 666 not divisible by 5
PATTERN.match('0000001010011010') == false
```
```java
// 5 divisible by 5
DivisibleByFive.pattern().matcher('101').matches() == true

// 135 divisible by 5
DivisibleByFive.pattern().matcher('10000111').matches() == true

// 666 not divisible by 5
DivisibleByFive.pattern().matcher('0000001010011010').matches() == false
```

### Note:

This can be solved by creating a Finite State Machine that evaluates if a string representing a number in binary base is divisible by given number.

The detailed explanation for dividing by 3 is
[here](http://math.stackexchange.com/questions/140283/why-does-this-fsm-accept-binary-numbers-divisible-by-three)

The FSM diagram for dividing by 5 is
[here](http://aswitalski.github.io/img/FSM-binary-divisible-by-five.png "Finite State machine - string representing a binary number divisible by 5")

