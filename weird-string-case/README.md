# WeIrD StRiNg CaSe

 - URL:[https://www.codewars.com/kata/52b757663a95b11b3d00062d](https://www.codewars.com/kata/52b757663a95b11b3d00062d)
 - Id: 52b757663a95b11b3d00062d
 - Language: javascript
 - Completed on: 2017-09-11T10:34:49.557Z
 - Tags: Strings,Algorithms
 - Description:
Write a function `toWeirdCase` (`weirdcase` in Ruby) that accepts a string, and returns the same string with all even indexed characters in each word upper cased, and all odd indexed characters in each word lower cased. The indexing just explained is zero based, so the zero-ith index is even, therefore that character should be upper cased and you need to start over for each word.

The passed in string will only consist of alphabetical characters and spaces(`' '`). Spaces will only be present if there are multiple words. Words will be separated by a single space(`' '`).

### Examples:
```javascript
toWeirdCase( "String" );//=> returns "StRiNg"
toWeirdCase( "Weird string case" );//=> returns "WeIrD StRiNg CaSe"
```
```coffeescript
toWeirdCase( "String" );//=> returns "StRiNg"
toWeirdCase( "Weird string case" );//=> returns "WeIrD StRiNg CaSe"
```
```python
to_weird_case('String'); # => returns 'StRiNg'
to_weird_case('Weird string case') # => returns 'WeIrD StRiNg CaSe'
```
```haskell
toWeirdCase "String"            `shouldBe` "StRiNg"
toWeirdCase "Weird string case" `shouldBe` "WeIrD StRiNg CaSe"
```
```ruby
weirdcase( "String" )#=> returns "StRiNg"
weirdcase( "Weird string case" );#=> returns "WeIrD StRiNg CaSe"
```
```php
toWeirdCase("String"); // => returns "StRiNg"
toWeirdCase("Weird string case"); // => returns "WeIrD StRiNg CaSe"
```
```go
toWeirdCase("String") // => returns "StRiNg"
toWeirdCase("Weird string case") // => returns "WeIrD StRiNg CaSe"
```
