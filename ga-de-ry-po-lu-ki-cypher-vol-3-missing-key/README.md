# GA-DE-RY-PO-LU-KI cypher vol 3 - Missing key

 - URL:[https://www.codewars.com/kata/592bdf59912f2209710000e9](https://www.codewars.com/kata/592bdf59912f2209710000e9)
 - Id: 592bdf59912f2209710000e9
 - Language: python
 - Completed on: 2018-02-02T14:55:25.314Z
 - Tags: Fundamentals
 - Description:
<h2> Introduction </h2>

The GADERYPOLUKI is a simple substitution cypher used in scouting to encrypt messages. The encryption is based on short, easy to remember key. The key is written as paired letters, which are in the cipher simple replacement.

The most frequently used key is "GA-DE-RY-PO-LU-KI".

```
 g => a
 a => g
 d => e
 e => d
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

Our scouts had party yestarday and they had too much milk and cookies. As the result all of them forgot the key. Your task is to help scouts to find the key that they used for encryption. Fortunately they have some messages that are already encoded. 


<h2>Input</h2>

The function accepts has two arrays. <br/>
The `messages` string array consists of lowercase characters and whitespace characters. The strings on the `messages` array are scout's messages before encrytption. <br/>
The `secrets` string array consists of lowercase characters and whitespace characters.
The strings on the `messages` array are scout's messages after encrytption. 

<h2>Output</h2>

Return string should consists of lowercase characters only. The pairs of substitution should be ordered by the first letter of substitution. The letters in each pair should be in alphabethic order. <br>

```
ga => incorret output (error: g is after a )
ag => correct output  
deag => incorrect output  (error: de is after ag)
agde => correct output  
```

<h2>Example</h2>


```csharp
string[] messages = { "dance on the table", "hide my beers", "scouts rocks" };
string[] secretes = { "egncd pn thd tgbud" ,"hked mr bddys" ,"scplts ypcis" };
FindTheKey(messages, secretes);   //=> agdeikluopry
 ```
```javascript
 var messages = [ "dance on the table", "hide my beers", "scouts rocks" ];
 var secrets =  [ "egncd pn thd tgbud" ,"hked mr bddys" ,"scplts ypcis" ];
 findTheKey(messages, secrets);   //=> agdeikluopry
 ```
```ruby
 messages = [ "dance on the table", "hide my beers", "scouts rocks" ];
 secrets =  [ "egncd pn thd tgbud" ,"hked mr bddys" ,"scplts ypcis" ];
 findTheKey(messages, secrets);   //=> agdeikluopry
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

