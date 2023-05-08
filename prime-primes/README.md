# Prime Primes

 - URL:[https://www.codewars.com/kata/57ba58d68dcd97e98c00012b](https://www.codewars.com/kata/57ba58d68dcd97e98c00012b)
 - Id: 57ba58d68dcd97e98c00012b
 - Language: python
 - Completed on: 2017-11-27T11:49:48.834Z
 - Tags: Algorithms
 - Description:
Define a "prime prime" number to be a rational number written as one prime number over another prime number: `primeA / primeB` (e.g. `7/31`)

Given a whole number `N` / `n`, generate the number of "prime prime" rational numbers less than 1, using only prime numbers between `0` and `N` / `n`(non inclusive).

Return the count of these "prime primes", and the integer part  of their sum.

## Example

```python
N = 6

# The "prime primes" less than 1 are:
2/3, 2/5, 3/5               # count: 3

2/3 + 2/5 + 3/5 = 1.6667    # integer part: 1

Thus, the function should return 3 and 1.
```

```ruby
n = 6

# The "prime primes" less than 1 are:
2/3, 2/5, 3/5               # count: 3

2/3 + 2/5 + 3/5 = 1.6667    # integer part: 1

thus, the function should return 3 and 1.
```

```javascript
N = 6

// The "prime primes" less than 1 are:
2/3, 2/5, 3/5               // count: 3

2/3 + 2/5 + 3/5 = 1.6667    // integer part: 1

Thus, the function should return [3, 1].
```
