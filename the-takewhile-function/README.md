# The takeWhile Function

 - URL:[https://www.codewars.com/kata/54f9173aa58bce9031001548](https://www.codewars.com/kata/54f9173aa58bce9031001548)
 - Id: 54f9173aa58bce9031001548
 - Language: python
 - Completed on: 2022-06-11T12:53:23.972Z
 - Tags: Functional Programming,Arrays,Algorithms
 - Description:
Here's another staple for the functional programmer. You have a sequence of values and some predicate for those values. You want to get the longest prefix of elements such that the predicate is true for each element. We'll call this the takeWhile function. It accepts two arguments. The first is the sequence of values, and the second is the predicate function. The function does not change the value of the original sequence. 

```javascript
function isEven(num) {
  return num % 2 === 0;
}
var seq = [2,4,6,8,1,2,5,4,3,2];

takeWhile(seq, isEven) // -> [2,4,6,8]
```
```csharp
Func<int,bool> isEven = (num) => num % 2 == 0;
var seq = new int[] { 2,4,6,8,1,2,5,4,3,2 };

Kata.TakeWhile(seq, isEven); // -> [2,4,6,8]
```
```cpp
std::function<bool (int)> isEven = [](int value)
{
    return abs(value) % 2 == 0;
};

std::vector<int> seq = { 2, 4, 6, 8, 1, 2, 5, 4, 3, 2 };

takeWhile(seq, pred); // -> { 2, 4, 6, 8 }
```
```python
is_even = lambda x: not x % 2
seq = [2, 4, 6, 8, 1, 2, 5, 4, 3, 2]
take_while(seq, is_even) # -> [2, 4, 6, 8]
```
```lambdacalc
take-while [2,4,6,8,1,2,5,4,3,2] even  -->  [2,4,6,8]
```

Your task is to implement the takeWhile function. 

If you've got a [span function](http://www.codewars.com/kata/the-span-function) lying around, this is a one-liner! Also, if you liked this problem, you'll surely love [the dropWhile function](http://www.codewars.com/kata/the-dropwhile-function).

~~~if:lambdacalc
### Encodings

purity: `LetRec`  
numEncoding: `BinaryScott`  
export constructors `nil, cons` and deconstructor `foldl` for your `List` encoding  
export constructors `False, True` for your `Boolean` encoding  
~~~
