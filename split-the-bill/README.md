# Split The Bill

 - URL:[https://www.codewars.com/kata/5641275f07335295f10000d0](https://www.codewars.com/kata/5641275f07335295f10000d0)
 - Id: 5641275f07335295f10000d0
 - Language: javascript
 - Completed on: 2017-08-24T13:54:10.598Z
 - Tags: Fundamentals,Object-oriented Programming,Data Structures
 - Description:
It's tricky keeping track of who is owed what when spending money in a group. Write a function to balance the books.

* The function should take one parameter: an object/dict with two or more name-value pairs which represent the members of the group and the amount spent by each.
* The function should return an object/dict with the same names, showing how much money the members should pay or receive.

**Further points:**

* The values should be positive numbers if the person should receive money from the group, negative numbers if they owe money to the group.
* If value is a decimal, round to two decimal places.
 
Translations and comments (and upvotes!) welcome.

### Example

3 friends go out together: A spends £20, B spends £15, and C spends £10. The function should return an object/dict showing that A should receive £5, B should receive £0, and C should pay £5.

```javascript
var group = {
    A: 20, 
    B: 15, 
    C: 10
}

splitTheBill(group) // returns {A: 5, B: 0, C: -5}
```    
```python
group = {
    'A': 20, 
    'B': 15, 
    'C': 10
}

split_the_bill(group) # returns {'A': 5, 'B': 0, 'C': -5}
```        
```ruby
group = {
    'A'=>20, 
    'B'=>15, 
    'C'=>10
}

split_the_bill(group) # returns {'A'=>5, 'B'=>0, 'C'=>-5}
```    
```elixir
group = %{
  :A => 20,
  :B => 15,
  :C => 10
}

split_the_bill(group) # returns %{:A => 5, :B => 0, :C => -5}
```
