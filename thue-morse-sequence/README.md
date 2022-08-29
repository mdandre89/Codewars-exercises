# Thue-Morse Sequence

 - URL:[https://www.codewars.com/kata/591aa1752afcb02fa300002a](https://www.codewars.com/kata/591aa1752afcb02fa300002a)
 - Id: 591aa1752afcb02fa300002a
 - Language: python
 - Completed on: 2017-06-18T18:26:24.388Z
 - Tags: Strings,Binary,Algorithms
 - Description:
Given a positive integer `n`, return first n dgits of Thue-Morse sequence, as a string (see examples).

Thue-Morse sequence is a binary sequence with 0 as the first element. The rest of the sequece is obtained by adding the Boolean (binary) complement of a group obtained so far.

```
For example:

0
01
0110
01101001
and so on...
```

![alt](https://upload.wikimedia.org/wikipedia/commons/f/f1/Morse-Thue_sequence.gif)


Ex.:
```javascript
thueMorse(1); //'0'
thueMorse(2); //'01'
thueMorse(5); //'01101'
thueMorse(10): //'0110100110'
```
```python
thue_morse(1);  #"0"
thue_morse(2);  #"01"
thue_morse(5);  #"01101"
thue_morse(10): #"0110100110"
```
```ruby
thue_morse(1);  #"0"
thue_morse(2);  #"01"
thue_morse(5);  #"01101"
thue_morse(10): #"0110100110"
```
```crystal
thue_morse(1);  #"0"
thue_morse(2);  #"01"
thue_morse(5);  #"01101"
thue_morse(10): #"0110100110"
```

- You don't need to test if n is valid - it will always be a positive integer.
- `n` will be between 1 and 10000

[Thue-Morse on Wikipedia](https://en.wikipedia.org/wiki/Thue%E2%80%93Morse_sequence)

[Another kata on Thue-Morse](https://www.codewars.com/kata/simple-fun-number-106-is-thue-morse) by @myjinxin2015


