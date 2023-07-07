# Normalizing Out of Range Array Indexes

 - URL:[https://www.codewars.com/kata/5285bf61f8fc1b181700024c](https://www.codewars.com/kata/5285bf61f8fc1b181700024c)
 - Id: 5285bf61f8fc1b181700024c
 - Language: javascript
 - Completed on: 2017-09-04T11:09:05.378Z
 - Tags: Arrays,Algorithms
 - Description:
Implement a function that normalizes out of range sequence indexes (converts them to 'in range' indexes) by making them repeatedly 'loop' around the array. The function should then return the value at that index. Indexes that are not out of range should be handled normally and indexes to empty sequences should return undefined/None depending on the language.

For positive numbers that are out of range, they loop around starting at the beginning, so 

```javascript
normIndex(arr, arr.length);     //Returns first element
normIndex(arr, arr.length + 1); //Returns second element
normIndex(arr, arr.length + 2); //Returns third element
//And so on...
normIndex(arr, arr.length * 2); //Returns first element
```

```csharp
Kata.NormIndex(arr, arr.Length);     //Returns first element
Kata.NormIndex(arr, arr.Length + 1); //Returns second element
Kata.NormIndex(arr, arr.Length + 2); //Returns third element
//And so on...
Kata.NormIndex(arr, arr.Length * 2); //Returns first element
```

```python
norm_index_test(seq, len(seq))     # Returns first element
norm_index_test(seq, len(seq) + 1) # Returns second element
norm_index_test(seq, len(seq) + 2) # Returns third element
# And so on...
norm_index_test(seq, len(seq) * 2) # Returns first element
```


For negative numbers, they loop starting from the end, so

```javascript
normIndex(arr, -1);    //Returns last element
normIndex(arr, -2);    //Returns second to last element
normIndex(arr, -3);    //Returns third to last element
//And so on...
normIndex(arr, -arr.length); //Returns first element
```

```csharp
Kata.NormIndex(arr, -1);    //Returns last element
Kata.NormIndex(arr, -2);    //Returns second to last element
Kata.NormIndex(arr, -3);    //Returns third to last element
//And so on...
Kata.NormIndex(arr, -arr.Length); //Returns first element
```

```python norm_index_test(seq, len(seq))
norm_index_test(seq, -1)        # Returns last element
norm_index_test(seq, -2)        # Returns second to last element
norm_index_test(seq, -3)        # Returns third to last element
# And so on...
norm_index_test(seq, -len(seq)) # Returns first element
```

