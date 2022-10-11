# Sum of Intervals

 - URL:[https://www.codewars.com/kata/52b7ed099cdc285c300001cd](https://www.codewars.com/kata/52b7ed099cdc285c300001cd)
 - Id: 52b7ed099cdc285c300001cd
 - Language: javascript
 - Completed on: 2018-02-27T12:40:28.519Z
 - Tags: Algorithms,Performance
 - Description:
Write a function called `sumIntervals`/`sum_intervals()` that accepts an array of intervals, and returns the sum of all the interval lengths. Overlapping intervals should only be counted once.

### Intervals

Intervals are represented by a pair of integers in the form of an array. The first value of the interval will always be less than the second value. Interval example: `[1, 5]` is an interval from 1 to 5. The length of this interval is 4.

### Overlapping Intervals

List containing overlapping intervals:

```
[
   [1,4],
   [7, 10],
   [3, 5]
]
```

The sum of the lengths of these intervals is 7. Since [1, 4] and [3, 5] overlap, we can treat the interval as [1, 5], which has a length of 4.

### Examples:

```javascript
sumIntervals( [
   [1,2],
   [6, 10],
   [11, 15]
] ); // => 9

sumIntervals( [
   [1,4],
   [7, 10],
   [3, 5]
] ); // => 7

sumIntervals( [
   [1,5],
   [10, 20],
   [1, 6],
   [16, 19],
   [5, 11]
] ); // => 19

```
```java
// null argument
Interval.sumIntervals(null);  // => 0

// empty intervals
Interval.sumIntervals(new int[][]{});  // => 0
Interval.sumIntervals(new int[][]{2,2}, {5,5});  // => 0

// disjoined intervals
Interval.sumIntervals(new int[][]{
  {1,2},{3,5}
});  // => (2-1) + (5-3) = 3

// overlapping intervals
Interval.sumIntervals(new int[][]{
  {1,4},{3,6},{2,8}
});  // [1,8] => 7
```
```C#
// empty intervals
Intervals.SumIntervals(new (int, int)[]{ });  // => 0
Intervals.SumIntervals(new (int, int)[]{ (2, 2), (5, 5)});  // => 0

// disjoined intervals
Intervals.SumIntervals(new (int, int)[]{
  (1, 2), (3, 5)
});  // => (2-1) + (5-3) = 3

// overlapping intervals
Intervals.SumIntervals(new (int, int)[]{
  (1, 4), (3, 6), (2, 8)
});  // (1,8) => 7
```
```cpp
sum_intervals( {
   {1,2},
   {6, 10},
   {11, 15}
} ); // => 9

sum_intervals( {
   {1,4},
   {7, 10},
   {3, 5}
} ); // => 7

sum_intervals( {
   {1,5},
   {10, 20},
   {1, 6},
   {16, 19},
   {5, 11}
} ); // => 19
```
```c
sum_intervals((const struct interval[]){
   {1,2},
   {6, 10},
   {11, 15}
}, 3); /* => 9 */

sum_intervals((const struct interval[]){
   {1,4},
   {7, 10},
   {3, 5}
}, 3); /* => 7 */

sum_intervals((const struct interval[]){
   {1,5},
   {10, 20},
   {1, 6},
   {16, 19},
   {5, 11}
}, 5); /* => 19 */
```
```nasm
v1:
    dd    1,2, \
          6,10, \
          11,15
v2:
    dd    1,4
    dd    7,10
    dd    3,5
v3:
    dd    1,5, 10,20, 1,6, 16,19, 5,11
      
    mov rdi, v1
    mov rsi, 3
    call sumintvls    ; EAX <- 9
    
    mov rdi, v2
    mov rsi, 3
    call sumintvls    ; EAX <- 7
    
    mov rdi, v3
    mov rsi, 5
    call sumintvls    ; EAX <- 19
```
```clojure
(sum-intervals [ [1 5] [10 15] [-1 3] ]) ; => 11

(sum-intervals [ [1 5] ]) ; => 4 
```
```typescript
sumOfIntervals([[1, 5], [10, 15], [-1, 3]]) // => 11

sumOfIntervals([[1, 5]]) // => 4 
```
```crystal
sum_of_intervals([{1, 5}, {10, 15}, {-1, 3}]) # => 11

sum_of_intervals([{1, 5}]) # => 4 
```
```elixir
sum_of_intervals([{1, 5}, {10, 15}, {-1, 3}]) # => 11

sum_of_intervals([{1, 5}]) # => 4 
```
```haskell
sumOfIntervals([(1, 5}, (10, 15}, (-1, 3)]) -- => 11

sumOfIntervals([(1, 5)]) -- => 4 
```
```julia
sumofintervals([(1, 5}, (10, 15}, (-1, 3)]) # => 11

sumofintervals([(1, 5)]) # => 4 
```
```dart
sumOfIntervals([[1, 5], [10, 15], [-1, 3]]) // => 11

sumOfIntervals([[1, 5]]) // => 4 
```
```racket
(sum-intervals (list (list -1 21) (list -59 -45))) ;; 36
(sum-intervals (list (list 1 5) (list 10 15) (list -1 3))) ;; 11
(sum-intervals (list (list 1 2) (list 6 10) (list 11 15))) ;; 36
```
```rust
sum_intervals(&[(1,5)]) // => 4
sum_intervals(&[(1, 5), (10, 15), (-1, 3)]) // => 11
```
~~~if:javascript
### Random Tests
- 100 tests with `1 - 10` intervals from the range `[-20, 20]`
- 100 tests with `20000 - 50000` intervals from the range `[-10^9, 10^9]`
~~~
~~~if:haskell
### Random Tests
Up to `1000` intervals from the range `[-10^9, 10^9]`.
~~~
~~~if:cobol
### Random tests
Up to 9999 intervals from the range `[-10^8, 10^8]`.
~~~
~~~if:c
### Random tests
Up to 32 intervals from the range `[-10^9, 10^9]`.
~~~
~~~if:rust
### Random tests
- 250 tests with `1-50` intervals in the range `[-100, 100]`
- 100 tests with `1000-10000` intervals in the range `[-10^5, 10^5]`
~~~
