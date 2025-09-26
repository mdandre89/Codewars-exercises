# Caesar Cipher Helper

 - URL:[https://www.codewars.com/kata/526d42b6526963598d0004db](https://www.codewars.com/kata/526d42b6526963598d0004db)
 - Id: 526d42b6526963598d0004db
 - Language: python
 - Completed on: 2017-09-12T14:56:09.391Z
 - Tags: Ciphers,Cryptography,Object-oriented Programming,Strings,Algorithms
 - Description:
Write a class that, when given a string, will return an **uppercase** string with each letter shifted forward in the alphabet by however many spots the cipher was initialized to.

For example:

```javascript
var c = new CaesarCipher(5); // creates a CipherHelper with a shift of five
c.encode('Codewars'); // returns 'HTIJBFWX'
c.decode('BFKKQJX'); // returns 'WAFFLES'
```
```coffeescript
c = new CaesarCipher(5) # creates a CipherHelper with a shift of five
c.encode('Codewars') # returns 'HTIJBFWX'
c.decode('BFKKQJX') # returns 'WAFFLES'
```
```python
c = CaesarCipher(5); # creates a CipherHelper with a shift of five
c.encode('Codewars') # returns 'HTIJBFWX'
c.decode('BFKKQJX') # returns 'WAFFLES'
```
```ruby
c = CaesarCipher.new(5); # creates a CipherHelper with a shift of five
c.encode('Codewars') # returns 'HTIJBFWX'
c.decode('BFKKQJX') # returns 'WAFFLES'
```

```php
$c = new CaesarCipher(5);
$c->encode('Codewars'); // returns 'HTIJBFWX'
$c->decode('BFKKQJX'); // returns 'WAFFLES'
```

If something in the string is not in the alphabet (e.g. punctuation, spaces), simply leave it as is.  
The shift will always be in range of `[1, 26]`.
