# Surrounding Primes for a value

 - URL:[https://www.codewars.com/kata/560b8d7106ede725dd0000e2](https://www.codewars.com/kata/560b8d7106ede725dd0000e2)
 - Id: 560b8d7106ede725dd0000e2
 - Language: python
 - Completed on: 2017-10-11T13:36:54.043Z
 - Tags: Fundamentals,Mathematics
 - Description:
We need a function ```prime_bef_aft()``` that gives the largest prime below a certain given value ```n```, 

```befPrime or bef_prime``` (depending on the language), 

and the smallest prime larger than this value, 

```aftPrime/aft_prime``` (depending on the language).

The result should be output in a list like the following:

```python
prime_bef_aft(n) == [befPrime, aftPrime]
```
```ruby
prime_bef_aft(n) == [bef_prime, aft_prime]
```
```javascript
primeBefAft == [befPrime, aftPrime]
```
```coffeescript
primeBefAft == [befPrime, aftPrime]
```
```java
primeBefAft == {befPrime, aftPrime}
```
```csharp
PrimeBefAft == {befPrime, aftPrime}
```
```haskell
PrimeBefAft == (befPrime, aftPrime)
```
```clojure
prime-bef-aft == [befPrime, aftPrime]
```

If n is a prime number it will give two primes, n will not be included in the result.

Let's see some cases:
```python
prime_bef_aft(100) == [97, 101]

prime_bef_aft(97) == [89, 101]

prime_bef_aft(101) == [97, 103]
```
```ruby
prime_bef_aft(100) == [97, 101]

prime_bef_aft(97) == [89, 101]

prime_bef_aft(101) == [97, 103]
```
```javascript
primeBefAft(100) == [97, 101]

primeBefAft(97) == [89, 101]

primeBefAft(101) == [97, 103]
```
```coffeescript
primeBefAft(100) == [97, 101]

primeBefAft(97) == [89, 101]

primeBefAft(101) == [97, 103]
```
```java
primeBefAft(100) --> {97, 101}

primeBefAft(97) --> {89, 101}

primeBefAft(101) --> {97, 103}
```
```csharp
PrimeBefAft(100) --> {97, 101}

PrimeBefAft(97) --> {89, 101}

PrimeBefAft(101) --> {97, 103}
```
```haskell
primeBefAft(100) --> (97, 101)

primeBefAft(97) --> (89, 101)

primeBefAft(101) --> (97, 103)
```
```clojure
(prime-bef-aft 100) == [97, 101]

(prime-bef-aft 97) == [89, 101]

(prime-bef-aft 101) == [97, 103]
```
Range for the random tests: 
```1000 <= n <= 200000```

(The extreme and special case n = 2 will not be considered for the tests. Thanks Blind4Basics)

Happy coding!!

