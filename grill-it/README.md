# Grill it!

 - URL:[https://www.codewars.com/kata/595b3f0ad26b2d817400002a](https://www.codewars.com/kata/595b3f0ad26b2d817400002a)
 - Id: 595b3f0ad26b2d817400002a
 - Language: javascript
 - Completed on: 2017-07-06T16:49:21.005Z
 - Tags: Strings,Binary,Fundamentals
 - Description:
# Introduction 

A grille cipher was a technique for encrypting a plaintext by writing it onto a sheet of paper through a pierced sheet (of paper or cardboard or similar). The earliest known description is due to the polymath Girolamo Cardano in 1550. His proposal was for a rectangular stencil allowing single letters, syllables, or words to be written, then later read, through its various apertures. The written fragments of the plaintext could be further disguised by filling the gaps between the fragments with anodyne words or letters. This variant is also an example of steganography, as are many of the grille ciphers. 
<a href="https://en.wikipedia.org/wiki/Grille_(cryptography)">Wikipedia Link</a> 

![Tangiers1](https://upload.wikimedia.org/wikipedia/commons/8/8a/Tangiers1.png)
![Tangiers2](https://upload.wikimedia.org/wikipedia/commons/b/b9/Tangiers2.png)

# Task

Write a function that accepts two inputs: `message` and `code` and returns hidden message decrypted from `message` using the `code`.   
The `code` is a nonnegative integer and it decrypts in binary the `message`. 


```csharp
Grille("abcdef", 5)  => "df"

message : abcdef
code    : 000101
----------------
result  : df

```
```javascript
grille("abcdef", 5)  => "df"

message : abcdef
code    : 000101
----------------
result  : df

```
```java
grille("abcdef", 5)  => "df"

message : abcdef
code    : 000101
----------------
result  : df

```




