# Binary multiple of 3

 - URL:[https://www.codewars.com/kata/54de279df565808f8b00126a](https://www.codewars.com/kata/54de279df565808f8b00126a)
 - Id: 54de279df565808f8b00126a
 - Language: python
 - Completed on: 2017-11-07T12:17:20.100Z
 - Tags: Regular Expressions,Algorithms,Puzzles,Number Theory,Mathematics
 - Description:
In this kata, your task is to create a regular expression capable of evaluating binary strings (strings with only `1`s and `0`s) and determining whether the given string represents a number divisible by 3.

Take into account that:

* An empty string *might* be evaluated to true (it's not going to be tested, so you don't need to worry about it - unless you want)
* The input should consist only of binary digits - no spaces, other digits, alphanumeric characters, etc.
* There might be leading `0`s.

```if-not:julia
### Examples (Javascript)
* `multipleof3Regex.test('000')` should be `true`
* `multipleof3Regex.test('001')` should be `false`
* `multipleof3Regex.test('011')` should be `true`
* `multipleof3Regex.test('110')` should be `true`
* `multipleof3Regex.test(' abc ')` should be `false`
```
```if:julia
### Examples
* `occursin(multipleof3regex, '000')` should be `true`
* `occursin(multipleof3regex, '001')` should be `false`
* `occursin(multipleof3regex, '011')` should be `true`
* `occursin(multipleof3regex, '110')` should be `true`
* `occursin(multipleof3regex, ' abc ')` should be `false`
```

You can check more in the example test cases

### Note
There's a way to develop an automata (FSM) that evaluates if strings representing numbers in a given base are divisible by a given number. You might want to check an example of an automata for doing this same particular task [here](http://math.stackexchange.com/questions/140283/why-does-this-fsm-accept-binary-numbers-divisible-by-three).

If you want to understand better the inner principles behind it, you might want to study how to get the modulo of an arbitrarily large number taking one digit at a time.
