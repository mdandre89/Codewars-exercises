# denumerate string

 - URL:[https://www.codewars.com/kata/57197be09906af7c830016de](https://www.codewars.com/kata/57197be09906af7c830016de)
 - Id: 57197be09906af7c830016de
 - Language: python
 - Completed on: 2017-11-22T12:06:10.575Z
 - Tags: Strings,Sorting,Fundamentals
 - Description:
You have to rebuild a string from an enumerated list.
For this task, you have to check if input is correct beforehand.

* Input must be a list of tuples
* Each tuple has two elements.
* Second element is an alphanumeric character.
* First element is the index of this character into the reconstructed string.
* Indexes start at 0 and have to match with output indexing: no gap is allowed.
* Finally tuples aren't necessarily ordered by index.

If any condition is invalid, the function should return `False`.

Input example: 
```python 
[(4,'y'),(1,'o'),(3,'t'),(0,'m'),(2,'n')]
```
Returns

```python
'monty'
```


