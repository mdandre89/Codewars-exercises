# The Enigma Machine - Part 1: The Plugboard

 - URL:[https://www.codewars.com/kata/5523b97ac8f5025c45000900](https://www.codewars.com/kata/5523b97ac8f5025c45000900)
 - Id: 5523b97ac8f5025c45000900
 - Language: python
 - Completed on: 2017-08-11T15:35:57.744Z
 - Tags: Fundamentals,Algorithms
 - Description:
In this series of Kata, we will be implementing a software version of the [Enigma Machine](http://en.wikipedia.org/wiki/Enigma_machine).

The Enigma Machine was a message enciphering/deciphering machine used during the Second World War for disguising the content of military communications.  [Alan Turing](http://en.wikipedia.org/wiki/Alan_Turing) - the father of computing - formulated and developed concepts that are the basis of all computers in use today, he did this in response to the vital need to break those military communications.  Turing and his colleagues at [Bletchley Park](http://en.wikipedia.org/wiki/Bletchley_Park) are generally recognised as being responsible for shortening WWII by two years and saving an estimated 22 Million lives.

The Enigma Machine consisted of a number of parts: Keyboard for input, rotors and plugboard for enciphering, and lampboard for output.

We will simulate input and output with strings, and build the rotors, plugboard and mechanism that used them in software.  As we progress the code will become more complex, so you are advised to attempt them in order.

Step 1: The [plugboard](http://en.wikipedia.org/wiki/Enigma_machine#Plugboard)

In this Kata, you must implement the plugboard.  

### Physical Description
The plugboard crosswired the 26 letters of the latin alphabet togther, so that an input into one letter could generate output as another letter.  If a wire was not present, then the input letter was unchanged.  Each plugboard came with a maximum of 10 wires, so at least six letters were not cross-wired.

For example:

* If a wire connects `A` to `B`, then an `A` input will generate a `B` output and a `B` input will generate an `A` output.

* If no wire connects to `C`, then only a `C` input will generate a `C` output.

### Note
In the actual usage of the original Enigma Machine, punctuation was encoded as words transmitted in the stream, in our code, anything that is not in the range A-Z will be returned unchanged.

### Kata
The `Plugboard` class you will implement, will:

1. Take a list of wire pairs at construction in the form of a string, with a default behaviour of no wires configured.  E.g. `"ABCD"` would wire `A` <-> `B` and `C` <-> `D`.
2. Validate that the wire pairings are legitimate. Raise an exception if not.
3. Implement the `process` method to translate a single character input into an output.

~~~if:haskell
### Haskell remarks
Since Haskell doesn't have classes, `plugboard` is a function that either returns a `Char -> Char` function for processing, or an error message.
~~~

---

## Examples

```python
plugboard = Plugboard("ABCDEFGHIJKLMNOPQRST")
plugboard.process("A") ==> "B"
plugboard.process("B") ==> "A"
plugboard.process("X") ==> "X"
plugboard.process(".") ==> "."
```
```javascript
var plugboard = Plugboard("ABCDEFGHIJKLMNOPQRST")
plugboard.process("A") ==> "B"
plugboard.process("B") ==> "A"
plugboard.process("X") ==> "X"
plugboard.process(".") ==> "."
```
```java
Plugboard plugboard = new Plugboard("ABCDEFGHIJKLMNOPQRST");
plugboard.process("A") ==> "B"
plugboard.process("B") ==> "A"
plugboard.process("X") ==> "X"
plugboard.process(".") ==> "."
```
```haskell
let (Right process) = plugboard "ABCDEFGHIJKLMNOPQRST"
in map process "ABX." `shouldBe` "BAX."
```
```csharp
var plugboard = new Plugboard("ABCDEFGHIJKLMNOPQRST");
plugboard.process('A') ==> "B"
plugboard.process('B') ==> "A"
plugboard.process('X') ==> "X"
plugboard.process('.') ==> "."
```

