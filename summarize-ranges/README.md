# Summarize ranges

 - URL:[https://www.codewars.com/kata/55fb6537544ae06ccc0000dc](https://www.codewars.com/kata/55fb6537544ae06ccc0000dc)
 - Id: 55fb6537544ae06ccc0000dc
 - Language: python
 - Completed on: 2018-02-05T12:51:19.364Z
 - Tags: Arrays,Algorithms
 - Description:
Given a sorted array of numbers, return the summary of its ranges.


## Examples
```javascript
summaryRanges([1, 2, 3, 4]) === ["1->4"]
summaryRanges([1, 1, 1, 1, 1]) === ["1"]
summaryRanges([0, 1, 2, 5, 6, 9]) === ["0->2", "5->6", "9"]
summaryRanges([0, 1, 2, 3, 3, 3, 4, 5, 6, 7]) === ["0->7"]
summaryRanges([0, 1, 2, 3, 3, 3, 4, 4, 5, 6, 7, 7, 9, 9, 10]) === ["0->7", "9->10"]
summaryRanges([-2,0, 1, 2, 3, 3, 3, 4, 4, 5, 6, 7, 7, 9, 9, 10, 12]) ===["-2", "0->7", "9->10", "12"]
```
```python
summary_ranges([1, 2, 3, 4]) == ["1->4"]
summary_ranges([1, 1, 1, 1, 1]) == ["1"]
summary_ranges([0, 1, 2, 5, 6, 9]) == ["0->2", "5->6", "9"]
summary_ranges([0, 1, 2, 3, 3, 3, 4, 5, 6, 7]) == ["0->7"]
summary_ranges([0, 1, 2, 3, 3, 3, 4, 4, 5, 6, 7, 7, 9, 9, 10]) == ["0->7", "9->10"]
summary_ranges([-2, 0, 1, 2, 3, 3, 3, 4, 4, 5, 6, 7, 7, 9, 9, 10, 12]) == ["-2", "0->7", "9->10", "12"]
```
```ruby
summary_ranges([1, 2, 3, 4]) == ["1->4"]
summary_ranges([1, 1, 1, 1, 1]) == ["1"]
summary_ranges([0, 1, 2, 5, 6, 9]) == ["0->2", "5->6", "9"]
summary_ranges([0, 1, 2, 3, 3, 3, 4, 5, 6, 7]) == ["0->7"]
summary_ranges([0, 1, 2, 3, 3, 3, 4, 4, 5, 6, 7, 7, 9, 9, 10]) == ["0->7", "9->10"]
summary_ranges([-2, 0, 1, 2, 3, 3, 3, 4, 4, 5, 6, 7, 7, 9, 9, 10, 12]) == ["-2", "0->7", "9->10", "12"]
```
