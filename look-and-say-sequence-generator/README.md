# Look and say sequence generator

 - URL:[https://www.codewars.com/kata/592421cb7312c23a990000cf](https://www.codewars.com/kata/592421cb7312c23a990000cf)
 - Id: 592421cb7312c23a990000cf
 - Language: python
 - Completed on: 2017-11-20T14:55:56.083Z
 - Tags: Strings,Regular Expressions,Fundamentals
 - Description:
The look and say sequence is a sequence in which each number is the result of a "look and say" operation on the previous element.

Considering for example the classical version startin with `"1"`: `["1", "11", "21, "1211", "111221", ...]`. You can see that the second element describes the first as `"1(times number)1"`, the third is `"2(times number)1"` describing the second, the fourth is `"1(times number)2(and)1(times number)1"` and so on.

Your goal is to create a function which takes a starting string (not necessarily the classical `"1"`, much less a single character start) and return the nth element of the series.

## Examples

```javascript
lookAndSaySequence("1", 1)   === "1"
lookAndSaySequence("1", 3)   === "21"
lookAndSaySequence("1", 5)   === "111221"
lookAndSaySequence("22", 10) === "22"
lookAndSaySequence("14", 2)  === "1114"
```
```python
look_and_say_sequence("1", 1)   == "1"
look_and_say_sequence("1", 3)   == "21"
look_and_say_sequence("1", 5)   == "111221"
look_and_say_sequence("22", 10) == "22"
look_and_say_sequence("14", 2)  == "1114"
```
```ruby
look_and_say_sequence("1", 1)   == "1"
look_and_say_sequence("1", 3)   == "21"
look_and_say_sequence("1", 5)   == "111221"
look_and_say_sequence("22", 10) == "22"
look_and_say_sequence("14", 2)  == "1114"
```
```crystal
look_and_say_sequence("1" ,1)   == "1"
look_and_say_sequence("1", 3)   == "21"
look_and_say_sequence("1", 5)   == "111221"
look_and_say_sequence("22", 10) == "22"
look_and_say_sequence("14", 2)  == "1114"
```
```csharp
LookAndSaySequence("1" ,1)   == "1"
LookAndSaySequence("1", 3)   == "21"
LookAndSaySequence("1", 5)   == "111221"
LookAndSaySequence("22", 10) == "22"
LookAndSaySequence("14", 2)  == "1114"
```
```c
LookAndSaySequence("1" ,1)   == "1"
LookAndSaySequence("1", 3)   == "21"
LookAndSaySequence("1", 5)   == "111221"
LookAndSaySequence("22", 10) == "22"
LookAndSaySequence("14", 2)  == "1114"
```
Trivia: `"22"` is the only element that can keep the series constant.
