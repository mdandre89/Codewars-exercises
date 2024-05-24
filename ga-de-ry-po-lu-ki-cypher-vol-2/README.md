# GA-DE-RY-PO-LU-KI cypher vol 2

 - URL:[https://www.codewars.com/kata/592b7b16281da94068000107](https://www.codewars.com/kata/592b7b16281da94068000107)
 - Id: 592b7b16281da94068000107
 - Language: python
 - Completed on: 2017-11-27T14:26:46.326Z
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

Other keys often used by Scouts:

```
PO-LI-TY-KA-RE-NU
KA-CE-MI-NU-TO-WY
KO-NI-EC-MA-TU-RY
ZA-RE-WY-BU-HO-KI
BA-WO-LE-TY-KI-JU
RE-GU-LA-MI-NO-WY
```

<h2>Task</h2>

Your task is to help scouts to encrypt and decrypt thier messages.
Write the `Encode` and `Decode` functions. 

<h2>Input/Output</h2>

The function should have two parameters. <br/>
The `message` input string consists of lowercase and uperrcase characters and whitespace character.<br/>
The `key` input string consists of only lowercase characters.
<br/>The substitution has to be case-sensitive. 

<h2>Example</h2>

```csharp
 Encode("ABCD", "agedyropulik");             // => GBCE 
 Encode("Ala has a cat", "gaderypoluki");    // => Gug hgs g cgt 
 Decode("Dkucr pu yhr ykbir","politykarenu") // => Dance on the table
 Decode("Hmdr nge brres","regulaminowy")  // => Hide our beers
 ```
```javascript
 encode("ABCD", "agedyropulik");             // => GBCE 
 encode("Ala has a cat", "gaderypoluki");    // => Gug hgs g cgt 
 decode("Dkucr pu yhr ykbir","politykarenu") // => Dance on the table
 decode("Hmdr nge brres","regulaminowy")  // => Hide our beers
 ```
```ruby
 encode("ABCD", "agedyropulik");             // => GBCE 
 encode("Ala has a cat", "gaderypoluki");    // => Gug hgs g cgt 
 decode("Dkucr pu yhr ykbir","politykarenu") // => Dance on the table
 decode("Hmdr nge brres","regulaminowy")  // => Hide our beers
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
