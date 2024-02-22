# How many nines?

 - URL:[https://www.codewars.com/kata/5e18743cd3346f003228b604](https://www.codewars.com/kata/5e18743cd3346f003228b604)
 - Id: 5e18743cd3346f003228b604
 - Language: python
 - Completed on: 2022-06-04T22:57:10.513Z
 - Tags: Mathematics,Puzzles
 - Description:
Ask a mathematician: "What proportion of natural numbers contain at least one digit `9` somewhere in their decimal representation?"

You might get the answer "Almost all of them", or "100%".

Clearly though, not all whole numbers contain a `9`.

In this kata we ask the question: "How many `Integer`s in the range `[0..n]` contain at least one `9` in their decimal representation?"

In other words, write the function:

```haskell
nines :: Integer -> Integer
```
```javascript
nines :: BigInt => BigInt
```
```elixir
nines :: Integer -> Integer
```

Where, for example:

```haskell
nines 1  = 0
nines 10 = 1     -- 9
nines 90 = 10    -- 9, 19, 29, 39, 49, 59, 69, 79, 89, 90
```
```javascript
nines(1n)  = 0n
nines(10n) = 1n     // 9
nines(90n) = 10n    // 9, 19, 29, 39, 49, 59, 69, 79, 89, 90
```
```elixir
nines(1) == 0
nines(10) == 1     # 9
nines(90) == 10    # 9, 19, 29, 39, 49, 59, 69, 79, 89, 90
```

When designing your solution keep in mind that your function will be tested against some large numbers (up to `10^38`)
