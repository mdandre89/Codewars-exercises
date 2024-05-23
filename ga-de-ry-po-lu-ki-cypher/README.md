# GA-DE-RY-PO-LU-KI cypher

 - URL:[https://www.codewars.com/kata/592a6ad46d6c5a62b600003f](https://www.codewars.com/kata/592a6ad46d6c5a62b600003f)
 - Id: 592a6ad46d6c5a62b600003f
 - Language: python
 - Completed on: 2017-06-17T16:26:09.425Z
 - Tags: Fundamentals
 - Description:
<h2> Introduction </h2>

The GADERYPOLUKI is a simple substitution cypher used in scouting to encrypt messages. The encryption is based on short, easy to remember key. The key is written as paired letters, which are in the cipher simple replacement.

The most frequently used key is "GA-DE-RY-PO-LU-KI".

```
 G => A
 g => a
 a => g
 A => G
 D => E
  etc.
```

The letters, which are not on the list of substitutes, stays in the encrypted text without changes.

<h2>Task</h2>

Your task is to help scouts to encrypt and decrypt thier messages.
Write the `Encode` and `Decode` functions.

<h2>Input/Output</h2>

The input string consists of lowercase and uperrcase characters and white .
The substitution has to be case-sensitive. 

<h2>Example</h2>

```csharp
 Encode("ABCD")          // => GBCE 
 Encode("Ala has a cat") // => Gug hgs g cgt 
 Encode("gaderypoluki"); // => agedyropulik
 Decode("Gug hgs g cgt") // => Ala has a cat 
 Decode("agedyropulik")  // => gaderypoluki
 Decode("GBCE")          // => ABCD
 ```
```javascript
 encode("ABCD")          // => GBCE 
 encode("Ala has a cat") // => Gug hgs g cgt 
 encode("gaderypoluki"); // => agedyropulik
 decode("Gug hgs g cgt") // => Ala has a cat 
 decode("agedyropulik")  // => gaderypoluki
 decode("GBCE")          // => ABCD
 ```
```ruby
 encode("ABCD")          // => GBCE 
 encode("Ala has a cat") // => Gug hgs g cgt 
 encode("gaderypoluki"); // => agedyropulik
 decode("Gug hgs g cgt") // => Ala has a cat 
 decode("agedyropulik")  // => gaderypoluki
 decode("GBCE")          // => ABCD
 ```

# GADERYPOLUKI collection

<table border="0" cellpadding="0" cellspacing="0">
<tr>
<td ><a href="https://www.codewars.com/kata/592a6ad46d6c5a62b600003f" target="_blank">GADERYPOLUKI cypher vol 1</a></td>
</tr>
<tr>
<td ><a href="https://www.codewars.com/kata/592b7b16281da94068000107" target="_blank">GADERYPOLUKI cypher vol 2</a></td>
</tr>
<tr>
<td ><a href="https://www.codewars.com/kata/592bdf59912f2209710000e9" target="_blank">GADERYPOLUKI cypher vol 3 - Missing Key</a></td>
</tr>
<tr>
<td ><a href="https://www.codewars.com/kata/592ceef6af58a64c7f00003c" target="_blank">GADERYPOLUKI cypher vol 4 - Missing key madness</a></td>
</tr>
</table>
      
