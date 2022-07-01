# World Bits War

 - URL:[https://www.codewars.com/kata/58865bfb41e04464240000b0](https://www.codewars.com/kata/58865bfb41e04464240000b0)
 - Id: 58865bfb41e04464240000b0
 - Language: python
 - Completed on: 2018-02-13T14:35:09.874Z
 - Tags: Bits,Binary,Arrays,Fundamentals
 - Description:
Variation of <a href="https://www.codewars.com/kata/bits-battle/" target="_blank">this nice kata</a>, the war has expanded and become dirtier and meaner; both even and odd numbers will fight with their pointy `1`s.
And negative integers are coming into play as well, with, ça va sans dire, a negative contribution (think of them as spies or saboteurs).

A number's strength is determined by the number of set bits (`1`s) in its binary representation. Negative integers work against their own side so their strength is negative.
For example `-5` = `-101` has strength `-2` and `+5` = `+101` has strength `+2`.

The side with the largest cumulated strength wins.

Again, three possible outcomes: `odds win`, `evens win` and `tie`.

Examples:

```javascript
bitsWar([1,5,12]) => "odds win" //1+101 vs 1100, 3 vs 2
bitsWar([7,-3,20]) => "evens win" //111-11 vs 10100, 3-2 vs 2
bitsWar([7,-3,-2,6]) => "tie" //111-11 vs -1+110, 3-2 vs -1+2
```
```python
bits_war([1,5,12]) => "odds win" #1+101 vs 1100, 3 vs 2
bits_war([7,-3,20]) => "evens win" #111-11 vs 10100, 3-2 vs 2
bits_war([7,-3,-2,6]) => "tie" #111-11 vs -1+110, 3-2 vs -1+2
```
```ruby
bits_war([1,5,12]) => "odds win" #1+101 vs 1100, 3 vs 2
bits_war([7,-3,20]) => "evens win" #111-11 vs 10100, 3-2 vs 2
bits_war([7,-3,-2,6]) => "tie" #111-11 vs -1+110, 3-2 vs -1+2
```
```crystal
bits_war([1,5,12]) => "odds win" #1+101 vs 1100, 3 vs 2
bits_war([7,-3,20]) => "evens win" #111-11 vs 10100, 3-2 vs 2
bits_war([7,-3,-2,6]) => "tie" #111-11 vs -1+110, 3-2 vs -1+2
```
```php
bitsWar([1,5,12]) => "odds win" //1+101 vs 1100, 3 vs 2
bitsWar([7,-3,20]) => "evens win" //111-11 vs 10100, 3-2 vs 2
bitsWar([7,-3,-2,6]) => "tie" //111-11 vs -1+110, 3-2 vs -1+2
```
```java
bitsWar(new int[]{1,5,12}).equals("odds win") == true   // 1+101 vs 1100, 3 vs 2
bitsWar(new int[]{7,-3,20}).equals("evens win") == true // 111-11 vs 10100, 3-2 vs 2
bitsWar(new int[]{7,-3,-2,6}).equals("tie") == true     // 111-11 vs -1+110, 3-2 vs -1+2
```
