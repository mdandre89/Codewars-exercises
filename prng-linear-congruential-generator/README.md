# PRNG: Linear Congruential Generator

 - URL:[https://www.codewars.com/kata/594979a364becbc1ab00003a](https://www.codewars.com/kata/594979a364becbc1ab00003a)
 - Id: 594979a364becbc1ab00003a
 - Language: javascript
 - Completed on: 2017-09-09T12:42:04.127Z
 - Tags: Algorithms
 - Description:
The [Linear Congruential Generator (LCG)](https://en.wikipedia.org/wiki/Linear_congruential_generator) is one of the oldest pseudo random number generator functions.

The algorithm is as follows:

## X<sub>n+1</sub>=(aX<sub>n</sub> + c) mod m
where:
* `a`/`A` is the multiplier (we'll be using `2`)
* `c`/`C` is the increment (we'll be using `3`)
* `m`/`M` is the modulus (we'll be using `10`)

X<sub>0</sub> is the seed.


# Your task

Define a method `random`/`Random` in the class `LCG` that provides the next random number based on a seed. You never return the initial seed value.

Similar to [random](https://docs.python.org/3/library/random.html#random.random) return the result as a floating point number in the range `[0.0, 1.0)`


# Example

```python
# initialize the generator with seed = 5
LCG(5)

# first random number (seed = 5)
LCG.random() = 0.3      # (2 * 5 + 3) mod 10 = 3 --> return 0.3

# next random number (seed = 3)
LCG.random() = 0.9      # (2 * 3 + 3) mod 10 = 9 --> return 0.9

# next random number (seed = 9)
LCG.random() = 0.1

# next random number (seed = 1)
LCG.random() = 0.5
```
```ruby
# initialize the generator with seed = 5
LCG(5)

# first random number (seed = 5)
LCG.random() = 0.3      # (2 * 5 + 3) mod 10 = 3 --> return 0.3

# next random number (seed = 3)
LCG.random() = 0.9      # (2 * 3 + 3) mod 10 = 9 --> return 0.9

# next random number (seed = 9)
LCG.random() = 0.1

# next random number (seed = 1)
LCG.random() = 0.5
```
```crystal
# initialize the generator with seed = 5
LCG(5)

# first random number (seed = 5)
LCG.random() = 0.3      # (2 * 5 + 3) mod 10 = 3 --> return 0.3

# next random number (seed = 3)
LCG.random() = 0.9      # (2 * 3 + 3) mod 10 = 9 --> return 0.9

# next random number (seed = 9)
LCG.random() = 0.1

# next random number (seed = 1)
LCG.random() = 0.5
```
```javascript
// initialize the generator with seed = 5
LCG(5)

// first random number (seed = 5)
LCG.random() = 0.3      # (2 * 5 + 3) mod 10 = 3 --> return 0.3

// next random number (seed = 3)
LCG.random() = 0.9      # (2 * 3 + 3) mod 10 = 9 --> return 0.9

// next random number (seed = 9)
LCG.random() = 0.1

// next random number (seed = 1)
LCG.random() = 0.5
```
```csharp
LCG myLCG = new LCG(5); // Initialize the generator with a seed of 5
myLCG.Random(); // => 0.3 ((2 * 5 + 3) mod 10 = 3)
myLCG.Random(); // => 0.9 ((2 * 3 + 3) mod 10 = 9)
myLCG.Random(); // => 0.1 ((2 * 9 + 3) mod 10 = 1)
myLCG.Random(); // => 0.5 ((2 * 1 + 3) mod 10 = 5)
```

