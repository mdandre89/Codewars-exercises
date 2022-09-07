# The old switcheroo

 - URL:[https://www.codewars.com/kata/55d410c492e6ed767000004f](https://www.codewars.com/kata/55d410c492e6ed767000004f)
 - Id: 55d410c492e6ed767000004f
 - Language: javascript
 - Completed on: 2017-05-03T17:15:28.283Z
 - Tags: Strings,Regular Expressions,Fundamentals
 - Description:
Write a function 

```javascript
vowel2index(str)
```
```coffeescript
vowel2index(str)
```
```python
vowel_2_index
```
```ruby
vowel_2_index
```
```csharp
Vowel2Index(string s)
  ```
```java
vowel2Index(String s)
```
```julia
vowel2index(str::String)::String
```

that takes in a string and replaces all the vowels [a,e,i,o,u] with their respective positions within that string. <br/>
E.g: <br/>

```javascript
vowel2index('this is my string') == 'th3s 6s my str15ng'
vowel2index('Codewars is the best site in the world') == 'C2d4w6rs 10s th15 b18st s23t25 27n th32 w35rld'
vowel2index('') == ''
```
```python
vowel_2_index('this is my string') == 'th3s 6s my str15ng'
vowel_2_index('Codewars is the best site in the world') == 'C2d4w6rs 10s th15 b18st s23t25 27n th32 w35rld'
vowel_2_index('') == ''
```
```ruby
vowel_2_index('this is my string') == 'th3s 6s my str15ng'
vowel_2_index('Codewars is the best site in the world') == 'C2d4w6rs 10s th15 b18st s23t25 27n th32 w35rld'
vowel_2_index('') == ''
```
```coffeescript
vowel2index 'this is my string' == 'th3s 6s my str15ng'
vowel2index 'Codewars is the best site in the world' == 'C2d4w6rs 10s th15 b18st s23t25 27n th32 w35rld'
vowel2index '' == ''
```
```csharp
Kata.Vowel2Index("this is my string") == "th3s 6s my str15ng"
Kata.Vowel2Index("Codewars is the best site in the world") == "C2d4w6rs 10s th15 b18st s23t25 27n th32 w35rld"
```
```java
Kata.Vowel2Index("this is my string") == "th3s 6s my str15ng"
Kata.Vowel2Index("Codewars is the best site in the world") == "C2d4w6rs 10s th15 b18st s23t25 27n th32 w35rld"
```
```haskell
vowel2Index "this is my string"  == "th3s 6s my str15ng"
vowel2Index "Codewars is the best site in the world"  == "C2d4w6rs 10s th15 b18st s23t25 27n th32 w35rld"
```
```julia
vowel2index("this is my string") == "th3s 6s my str15ng"
vowel2index("Codewars is the best site in the world") == "C2d4w6rs 10s th15 b18st s23t25 27n th32 w35rld"
```
<b> Your function should be case insensitive to the vowels.

