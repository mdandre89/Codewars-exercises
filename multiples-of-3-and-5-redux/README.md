# Multiples of 3 and 5 redux

 - URL:[https://www.codewars.com/kata/54bb6ee72c4715684d0008f9](https://www.codewars.com/kata/54bb6ee72c4715684d0008f9)
 - Id: 54bb6ee72c4715684d0008f9
 - Language: python
 - Completed on: 2017-10-14T12:32:07.625Z
 - Tags: Algorithms,Mathematics
 - Description:
## The galactic games have begun!

It's the galactic games! Beings of all worlds come together to compete in several interesting sports, like nroogring, fredling and buzzing (the beefolks love the last one). However, there's also the traditional marathon run.

Unfortunately, there have been cheaters in the last years, and the committee decided to place sensors on the track. Committees being committees, they've come up with the following rule:

> A sensor should be placed every 3 and 5 meters from the start, e.g.
> at 3m, 5m, 6m, 9m, 10m, 12m, 15m, 18m….

Since you're responsible for the track, you need to buy those sensors. Even worse, you don't know how long the track will be! And since there might be more than a single track, and you can't be bothered to do all of this by hand, you decide to write a program instead.

## Task
Return the sum of the multiples of 3 and 5 __below__ a number. Being the _galactic_ games, the tracks can get rather large, so your solution should work for _really_ large numbers (greater than 1,000,000).

### Examples
```haskell
solution 10 `shouldBe` 23 = 3 + 5 + 6 + 9
solution 20 `shouldBe` 78 = 3 + 5 + 6 + 9 + 10 + 12 + 15 + 18
```
```javascript
solution (10) // => 23 = 3 + 5 + 6 + 9
solution (20) // => 78 = 3 + 5 + 6 + 9 + 10 + 12 + 15 + 18
```
```python
solution (10) # => 23 = 3 + 5 + 6 + 9
solution (20) # => 78 = 3 + 5 + 6 + 9 + 10 + 12 + 15 + 18
```
```ruby
solution(10) # => 23 = 3 + 5 + 6 + 9
solution(20) # => 78 = 3 + 5 + 6 + 9 + 10 + 12 + 15 + 18
```
