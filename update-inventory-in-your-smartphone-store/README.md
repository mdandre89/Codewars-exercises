# Update inventory  in your smartphone store

 - URL:[https://www.codewars.com/kata/57a31ce7cf1fa5a1e1000227](https://www.codewars.com/kata/57a31ce7cf1fa5a1e1000227)
 - Id: 57a31ce7cf1fa5a1e1000227
 - Language: python
 - Completed on: 2022-06-25T09:29:52.109Z
 - Tags: Algorithms,Data Structures,Arrays,Optimization
 - Description:
You will be given an array which lists the current inventory of stock in your store and another array which lists the new inventory being delivered to your store today.

Your task is to write a function that returns the updated list of your current inventory **in alphabetical order**.

## Example

```javascript
currentStock = [[25, 'HTC'], [1000, 'Nokia'], [50, 'Samsung'], [33, 'Sony'], [10, 'Apple']]
newStock = [[5, 'LG'], [10, 'Sony'], [4, 'Samsung'], [5, 'Apple']]

updateInventory(currentStock, newStock)  ==>
[[15, 'Apple'], [25, 'HTC'], [5, 'LG'], [1000, 'Nokia'], [54, 'Samsung'], [43, 'Sony']]
```
```python
cur_stock = [(25, 'HTC'), (1000, 'Nokia'), (50, 'Samsung'), (33, 'Sony'), (10, 'Apple')]
new_stock = [(5, 'LG'), (10, 'Sony'), (4, 'Samsung'), (5, 'Apple')]

update_inventory(cur_stock, new_stock)  ==>
[(15, 'Apple'), (25, 'HTC'), (5, 'LG'), (1000, 'Nokia'), (54, 'Samsung'), (43, 'Sony')]
```
```ruby
cur_stock = [[25, 'HTC'], [1000, 'Nokia'], [50, 'Samsung'], [33, 'Sony'], [10, 'Apple']]
new_stock = [[5, 'LG'], [10, 'Sony'], [4, 'Samsung'], [5, 'Apple']]

update_inventory(cur_stock, new_stock)  ==>
[[15, 'Apple'], [25, 'HTC'], [5, 'LG'], [1000, 'Nokia'], [54, 'Samsung'], [43, 'Sony']]
```

___

*Kata inspired by the FreeCodeCamp's 'Inventory Update' algorithm.*


