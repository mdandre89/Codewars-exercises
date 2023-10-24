# List to Array

 - URL:[https://www.codewars.com/kata/557dd2a061f099504a000088](https://www.codewars.com/kata/557dd2a061f099504a000088)
 - Id: 557dd2a061f099504a000088
 - Language: python
 - Completed on: 2017-03-11T15:24:55.714Z
 - Tags: Data Structures,Arrays,Fundamentals
 - Description:
<b>Linked lists</b> are data structures composed of nested or chained objects, each containing a single value and a reference to the next object. 

Here's an example of a list:

```javascript
{value: 1, next: {value: 2, next: {value: 3, next: null}}}
```
```python
class LinkedList:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next
        
LinkedList(1, LinkedList(2, LinkedList(3)))

```
```ruby
{value: 1, next: {value: 2, next: {value: 3, next: null}}}
```

Write a function listToArray (or list\_to\_array in Python) that converts a list to an array, like this:

```
[1, 2, 3]
```

Assume all inputs are valid lists with at least one value. For the purpose of simplicity, all values will be either numbers, strings, or Booleans.
