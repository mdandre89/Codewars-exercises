# Least Larger

 - URL:[https://www.codewars.com/kata/5f8341f6d030dc002a69d7e4](https://www.codewars.com/kata/5f8341f6d030dc002a69d7e4)
 - Id: 5f8341f6d030dc002a69d7e4
 - Language: python
 - Completed on: 2022-06-20T18:56:08.810Z
 - Tags: Algorithms
 - Description:
### Task

Given an array of numbers and an index, return either the index of the smallest number that is larger than the element at the given index, or `-1` if there is no such index ( or, where applicable, `Nothing` or a similarly empty value ).

### Notes

Multiple correct answers may be possible. In this case, return any one of them.  
The given index will be inside the given array.  
The given array will, therefore, never be empty.  

### Example

```javascript
leastLarger( [4, 1, 3, 5, 6], 0 )  =>  3
leastLarger( [4, 1, 3, 5, 6], 4 )  => -1
```
```haskell
leastLarger [4, 1, 3, 5, 6] 0  ->  Just 3
leastLarger [4, 1, 3, 5, 6] 4  -> Nothing
```
```c
least_larger({4, 1, 3, 5, 6}, 5, 0) ==  3;
least_larger({4, 1, 3, 5, 6}, 5, 4) == -1;
```
```python
least_larger( [4, 1, 3, 5, 6], 0 )  ->  3
least_larger( [4, 1, 3, 5, 6], 4 )  -> -1
```
```prolog
least_larger( [4, 1, 3, 5, 6], 0, 3 ).
least_larger( [4, 1, 3, 5, 6], 4, -1 ).
```
```ruby
least_larger( [4, 1, 3, 5, 6], 0 )  =  3
least_larger( [4, 1, 3, 5, 6], 4 )  = -1
```
```go
leastLarger( [] int {4, 1, 3, 5, 6}, 0 )  =  3
leastLarger( [] int {4, 1, 3, 5, 6}, 4 )  = -1
```
```java
leastLarger( new int [] {4, 1, 3, 5, 6}, 0 )  =  3
leastLarger( new int [] {4, 1, 3, 5, 6}, 4 )  = -1
```
```csharp
leastLarger( new int [] {4, 1, 3, 5, 6}, 0 )  =  3
leastLarger( new int [] {4, 1, 3, 5, 6}, 4 )  = -1
```
```cobol
      LeastLarger( [4, 1, 3, 5, 6], 1 )  = 4
      LeastLarger( [4, 1, 3, 5, 6], 5 )  = 0
```
```cpp
leastLarger( vector<int> {4, 1, 3, 5, 6}, 0 )  =  3
leastLarger( vector<int> {4, 1, 3, 5, 6}, 4 )  = -1
```
```lambdacalc
least-larger : List Number -> Number -> Option Number
least-larger < 4 1 3 5 6 > 0  .  Some 3
least-larger < 4 1 3 5 6 > 4  .  None

# use numEncoding Scott
# provide the following for input / output:
nil ~ [] : List a
cons ~ (:) : a -> List a -> List a
option ~ maybe : z -> (a -> z) -> Option a -> z
```
```factor
{ 4 1 3 5 6 } 0 ?least-larger !  3
{ 4 1 3 5 6 } 4 ?least-larger !  f
```
```julia
leastlarger([4, 1, 3, 5, 6], 1) -->  4
leastlarger([4, 1, 3, 5, 6], 5) -->  nothing
```
```rust
least_larger(&[4, 1, 3, 5, 6], 0)  // returns Some(3)
least_larger(&[4, 1, 3, 5, 6], 4)  // returns None
```
```go
LeastLarger([]int{4, 1, 3, 5, 6}, 0)  // returns 3
LeastLarger([]int{4, 1, 3, 5, 6}, 4)  // returns -1
```
