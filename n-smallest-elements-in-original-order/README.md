# N smallest elements in original order

 - URL:[https://www.codewars.com/kata/5aec1ed7de4c7f3517000079](https://www.codewars.com/kata/5aec1ed7de4c7f3517000079)
 - Id: 5aec1ed7de4c7f3517000079
 - Language: python
 - Completed on: 2022-06-25T18:50:56.898Z
 - Tags: Arrays,Lists,Data Structures,Algorithms
 - Description:
Your task is to write a function that does just what the title suggests (so, fair warning, be aware that you are not getting out of it just throwing a lame bas sorting method there) with an array/list/vector of integers and the expected number `n` of smallest elements to return.

Also:

* the number of elements to be returned cannot be higher than the array/list/vector length;
* elements can be duplicated;
* in case of duplicates, just return them according to the original order (see third example for more clarity).

Same examples and more in the test cases:

```javascript
firstNSmallest([1,2,3,4,5],3) === [1,2,3] //well, not technically ===, but you get what I mean
firstNSmallest([5,4,3,2,1],3) === [3,2,1]
firstNSmallest([1,2,3,4,1],3) === [1,2,1]
firstNSmallest([1,2,3,-4,0],3) === [1,-4,0]
firstNSmallest([1,2,3,4,5],0) === []
```
```cpp
firstNSmallest({1,2,3,4,5},3) == {1,2,3}
firstNSmallest({5,4,3,2,1},3) == {3,2,1}
firstNSmallest({1,2,3,4,1},3) == {1,2,1}
firstNSmallest({1,2,3,-4,0},3) == {1,-4,0}
firstNSmallest({1,2,3,4,5},0) == {}
```
```python
first_n_smallest([1,2,3,4,5],3) == [1,2,3]
first_n_smallest([5,4,3,2,1],3) == [3,2,1]
first_n_smallest([1,2,3,4,1],3) == [1,2,1]
first_n_smallest([1,2,3,-4,0],3) == [1,-4,0]
first_n_smallest([1,2,3,4,5],0) == []
```
```ruby
first_n_smallest([1,2,3,4,5],3) == [1,2,3]
first_n_smallest([5,4,3,2,1],3) == [3,2,1]
first_n_smallest([1,2,3,4,1],3) == [1,2,1]
first_n_smallest([1,2,3,-4,0],3) == [1,-4,0]
first_n_smallest([1,2,3,4,5],0) == []
```
```crystal
first_n_smallest([1,2,3,4,5],3) == [1,2,3]
first_n_smallest([5,4,3,2,1],3) == [3,2,1]
first_n_smallest([1,2,3,4,1],3) == [1,2,1]
first_n_smallest([1,2,3,-4,0],3) == [1,-4,0]
first_n_smallest([1,2,3,4,5],0) == []
```
```c
first_n_smallest((int[]){1,2,3,4,5},5,3) == {1,2,3}
first_n_smallest((int[]){5,4,3,2,1},5,3) == {3,2,1}
first_n_smallest((int[]){1,2,3,4,1},5,3) == {1,2,1}
first_n_smallest((int[]){1,2,3,-4,0},5,3) == {1,-4,0}
first_n_smallest((int[]){1,2,3,4,5},5,0) == {}
```
```nasm
first_n_smallest((int[]){1,2,3,4,5},5,3) == {1,2,3}
first_n_smallest((int[]){5,4,3,2,1},5,3) == {3,2,1}
first_n_smallest((int[]){1,2,3,4,1},5,3) == {1,2,1}
first_n_smallest((int[]){1,2,3,-4,0},5,3) == {1,-4,0}
first_n_smallest((int[]){1,2,3,4,5},5,0) == {}
```

```haskell
firstNSmallest [1,2,3,4,5]   3 `shouldBe`  [1,2,3]
firstNSmallest [5,4,3,2,1]   3 `shouldBe`  [3,2,1]
firstNSmallest [1,2,3,1,2]   3 `shouldBe`  [1,2,1]
firstNSmallest [1,2,3,-4,0]  3 `shouldBe`  [1,-4,0]
firstNSmallest [1,2,3,4,5]   0 `shouldBe`  []
```
```csharp
FirstNSmallest(new []{1,2,3,4,5},3) == new []{1,2,3}
FirstNSmallest(new []{5,4,3,2,1},3) == new []{3,2,1}
FirstNSmallest(new []{1,2,3,4,1},3) == new []{1,2,1}
FirstNSmallest(new []{1,2,3,-4,0},3) == new []{1,-4,0}
FirstNSmallest(new []{1,2,3,4,5},0) == new int[0]
```
```rust
assert_eq!(first_n_smallest(&[1,2,3,4,5], 3), [1,2,3]);
assert_eq!(first_n_smallest(&[5,4,3,2,1], 3), [3,2,1]);
assert_eq!(first_n_smallest(&[1,2,3,4,1], 3), [1,2,1]);
assert_eq!(first_n_smallest(&[1,2,3,-4,0], 3), [1,-4,0]);
assert_eq!(first_n_smallest(&[1,2,3,4,5], 0), []);
```

[Performance version by FArekkusu](https://www.codewars.com/kata/5aeed69804a92621a7000077) also available.
