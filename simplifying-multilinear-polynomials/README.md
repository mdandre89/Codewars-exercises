# Simplifying multilinear polynomials

 - URL:[https://www.codewars.com/kata/55f89832ac9a66518f000118](https://www.codewars.com/kata/55f89832ac9a66518f000118)
 - Id: 55f89832ac9a66518f000118
 - Language: python
 - Completed on: 2018-02-20T10:36:34.340Z
 - Tags: Mathematics,Strings,Regular Expressions,Parsers,Fundamentals
 - Description:
<!---
For translators: sorry if I am a noob with markdown (it's my very first time...). You are invited to make all the changes you think are needed
-->
When we attended middle school were asked to simplify mathematical expressions like "3x-yx+2xy-x" (or usually bigger), and that was easy-peasy ("2x+xy"). But tell that to your pc and we'll see! <br>

Write a function: `simplify`, that takes a string in input, representing a *multilinear non-constant polynomial in integers coefficients* (like `"3x-zx+2xy-x"`), and returns another string as output where the same expression has been simplified in the following way ( `->` means application of `simplify`):

- All possible sums and subtraction of equivalent monomials ("xy==yx") has been done, e.g.:<br> <p>`"cb+cba" -> "bc+abc"`, `"2xy-yx" -> "xy"`, `"-a+5ab+3a-c-2a" -> "-c+5ab"`
<br><br>
- All monomials appears in order of increasing number of variables, e.g.:<br> <p>`"-abc+3a+2ac" -> "3a+2ac-abc"`, `"xyz-xz" -> "-xz+xyz"`
<br><br> 
- If two monomials have the same number of variables, they appears in <a href="https://en.wikipedia.org/wiki/Lexicographical_order">lexicographic order</a>, e.g.:<br> <p>`"a+ca-ab" -> "a-ab+ac"`, `"xzy+zby" ->"byz+xyz"`
<br><br>  
- There is no leading `+` sign if the first coefficient is positive, e.g.:<br> <p>`"-y+x" -> "x-y"`, but no restrictions for `-`:  `"y-x" ->"-x+y"`

---

__N.B.__ to keep it simplest, the string in input is restricted to represent only *multilinear non-constant polynomials*, so you won't find something like `-3+yx^2'. **Multilinear** means in this context: **of degree 1 on each variable**.

**Warning**: the string in input can contain arbitrary variables represented by lowercase characters in the english alphabet.

__Good Work :)__

