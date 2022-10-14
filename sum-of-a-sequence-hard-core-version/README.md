# Sum of a Sequence [Hard-Core Version]

 - URL:[https://www.codewars.com/kata/587a88a208236efe8500008b](https://www.codewars.com/kata/587a88a208236efe8500008b)
 - Id: 587a88a208236efe8500008b
 - Language: python
 - Completed on: 2017-02-13T15:54:35.612Z
 - Tags: Algorithms,Optimization
 - Description:
As the title suggests, this is the hard-core version of <a href="https://www.codewars.com/kata/sum-of-a-sequence/" target="_blank"> another neat kata</a>.

The task is simple to explain: simply sum all the numbers from the first parameter being the beginning to the second parameter being the upper limit (possibly included), going in steps expressed by the third parameter:

```javascript
sequenceSum(2,2,2) === 2
sequenceSum(2,6,2) === 12 // 2 + 4 + 6
sequenceSum(1,5,1) === 15 // 1 + 2 + 3 + 4 + 5
sequenceSum(1,5,3) === 5 // 1 + 4
```
```python
sequence_sum(2, 2, 2) # 2
sequence_sum(2, 6, 2) # 12 (= 2 + 4 + 6)
sequence_sum(1, 5, 1) # (= 1 + 2 + 3 + 4 + 5)
sequence_sum(1, 5, 3) # 5 (= 1 + 4)
```
```ruby
sequence_sum(2, 2, 2) # 2
sequence_sum(2, 6, 2) # 12 (= 2 + 4 + 6)
sequence_sum(1, 5, 1) # (= 1 + 2 + 3 + 4 + 5)
sequence_sum(1, 5, 3) # 5 (= 1 + 4)
```
```crystal
sequence_sum(2, 2, 2) # 2
sequence_sum(2, 6, 2) # 12 (= 2 + 4 + 6)
sequence_sum(1, 5, 1) # (= 1 + 2 + 3 + 4 + 5)
sequence_sum(1, 5, 3) # 5 (= 1 + 4)
```
```csharp
SequenceSum(2, 2, 2) # 2
SequenceSum(2, 6, 2) # 12 (= 2 + 4 + 6)
SequenceSum(1, 5, 1) # (= 1 + 2 + 3 + 4 + 5)
SequenceSum(1, 3, 5) # 1
```

If it is an impossible sequence (with the beginning being larger the end and a positive step or the other way around), just return `0`. See the provided test cases for further examples :)

**Note:** differing from the other base kata, much larger ranges are going to be tested, so you should hope to get your algo optimized and to avoid brute-forcing your way through the solution.
