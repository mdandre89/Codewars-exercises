# Caesar Cipher

 - URL:[https://www.codewars.com/kata/54b594b6fab5e97c28000f3f](https://www.codewars.com/kata/54b594b6fab5e97c28000f3f)
 - Id: 54b594b6fab5e97c28000f3f
 - Language: python
 - Completed on: 2017-10-11T09:37:06.239Z
 - Tags: Algorithms,Encryption,Cryptography,Logic,Security,Ciphers,Strings,Data Types,Functions,Control Flow,Basic Language Features,Fundamentals
 - Description:
In cryptography, a Caesar cipher is one of the simplest and most widely known encryption techniques. It is a type of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet. For example, with a left shift of 3, D would be replaced by A, E would become B, and so on. The method is named after Julius Caesar, who used it in his private correspondence.

Your task is to write a function that takes exactly 2 arguments (_string, shiftkey_) and encrypts the given string. Any other character than isn't a letter should stay unchanged.

__Assumption__: shiftkey is integer from [-25, 25] interval.

For example:<br>
- caesar("Abcd", 2) should return "Cdef"<br>
- caesar("message", -1) should return "ldrrzfd"<br>
- caesar("ZZ Top", 3) should return "CC Wrs"<br>
and so on ...<br>
