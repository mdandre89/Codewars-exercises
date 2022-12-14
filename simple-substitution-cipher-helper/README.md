# Simple Substitution Cipher Helper

 - URL:[https://www.codewars.com/kata/52eb114b2d55f0e69800078d](https://www.codewars.com/kata/52eb114b2d55f0e69800078d)
 - Id: 52eb114b2d55f0e69800078d
 - Language: python
 - Completed on: 2017-09-13T16:13:24.605Z
 - Tags: Ciphers,Cryptography,Security,Basic Language Features,Language Features,Object-oriented Programming,Strings,Algorithms
 - Description:
A simple substitution cipher replaces one character from an alphabet with a character from an alternate alphabet, where each character's position in an alphabet is mapped to the alternate alphabet for encoding or decoding.

E.g.
```javascript
var abc1 = "abcdefghijklmnopqrstuvwxyz";
var abc2 = "etaoinshrdlucmfwypvbgkjqxz";
   
var sub = new SubstitutionCipher(abc1, abc2);
sub.encode("abc") // => "eta"
sub.encode("xyz") // => "qxz"
sub.encode("aeiou") // => "eirfg"
   
sub.decode("eta") // => "abc"
sub.decode("qxz") // => "xyz"
sub.decode("eirfg") // => "aeiou"
```
```python
map1 = "abcdefghijklmnopqrstuvwxyz";
map2 = "etaoinshrdlucmfwypvbgkjqxz";
   
cipher = Cipher(map1, map2);
cipher.encode("abc") # => "eta"
cipher.encode("xyz") # => "qxz"
cipher.encode("aeiou") # => "eirfg"
   
cipher.decode("eta") # => "abc"
cipher.decode("qxz") # => "xyz"
cipher.decode("eirfg") # => "aeiou"
```
```rust
let map1 = "abcdefghijklmnopqrstuvwxyz";
let map2 = "etaoinshrdlucmfwypvbgkjqxz";
   
let cipher = Cipher::new(map1, map2);
cipher.encode("abc") // => "eta"
cipher.encode("xyz") // => "qxz"
cipher.encode("aeiou") // => "eirfg"
   
cipher.decode("eta") // => "abc"
cipher.decode("qxz") // => "xyz"
cipher.decode("eirfg") // => "aeiou"
```

If a character provided is not in the opposing alphabet, simply leave it as be.
