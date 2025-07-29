# Collatz

 - URL:[https://www.codewars.com/kata/5286b2e162056fd0cb000c20](https://www.codewars.com/kata/5286b2e162056fd0cb000c20)
 - Id: 5286b2e162056fd0cb000c20
 - Language: javascript
 - Completed on: 2017-09-01T08:25:12.897Z
 - Tags: Number Theory,Mathematics,Algorithms
 - Description:
## Preface

A collatz sequence, starting with a positive integer<i>n</i>, is found by repeatedly applying the following function to <i>n</i> until <i>n</i> == 1 :

`$f(n) =
\begin{cases}
n/2,   \text{  if $n$ is even} \\
3n+1,  \text{  if $n$ is odd}
\end{cases}$`
----

A more detailed description of the collatz conjecture may be found [on Wikipedia](http://en.wikipedia.org/wiki/Collatz_conjecture).

## The Problem

Create a function `collatz` that returns a collatz sequence string starting with the positive integer argument passed into the function, in the following form:

"X<sub>0</sub>->X<sub>1</sub>->...->X<sub>N</sub>"

Where X<sub>i</sub> is each iteration of the sequence and N is the length of the sequence.

## Sample Input

```c
collatz(4); // should return "4->2->1"
collatz(3); // should return "3->10->5->16->8->4->2->1"
```
```javascript
collatz(4); // should return "4->2->1"
collatz(3); // should return "3->10->5->16->8->4->2->1"
```
```csharp
Kata.Collatz(4); // should return "4->2->1"
Kata.Collatz(3); // should return "3->10->5->16->8->4->2->1"
```
```ruby
collatz(4) # should return "4->2->1"
collatz(3) # should return "3->10->5->16->8->4->2->1"
```
```python
collatz(4) # should return "4->2->1"
collatz(3) # should return "3->10->5->16->8->4->2->1"
```
```haskell
collatz 2 `shouldBe` "2->1"
collatz 3 `shouldBe` "3->10->5->16->8->4->2->1"
collatz 4 `shouldBe` "4->2->1"
```
```elixir
Collatz.collatz(2) # should return "2->1"
Collatz.collatz(3) # should return "3->10->5->16->8->4->2->1"
Collatz.collatz(4) # should return "4->2->1"
```
```java
Collatz.collatz(2) // should return "2->1"
Collatz.collatz(3) // should return "3->10->5->16->8->4->2->1"
Collatz.collatz(4) // should return "4->2->1"
```

Don't worry about invalid input. Arguments passed into the function are guaranteed to be valid integers >= 1.

