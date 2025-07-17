# Complex numbers

 - URL:[https://www.codewars.com/kata/551e8c8e24b7a4eddd000441](https://www.codewars.com/kata/551e8c8e24b7a4eddd000441)
 - Id: 551e8c8e24b7a4eddd000441
 - Language: javascript
 - Completed on: 2022-06-10T00:59:24.232Z
 - Tags: Mathematics,Algorithms
 - Description:
# Introduction

Complex numbers allow us to move from one dimensional to two dimensional maths by introducing an imaginary part tagged on to every real number:

http://en.wikipedia.org/wiki/Complex_number

In this kata you will create a class `Complex` to represent a complex number and handle simple arithmetic.

# Details

An instance can be constructed by passing in the real and imaginary parts:

`var z = new Complex(real, imag)`

Or an instance can be constructed by passing in just the real part (if there is no imaginary part):

`var z = new Complex(real);`

The instance, z, then exposes the following members:

- `z.real` = the real part of the number
- `z.imag` = the imaginary part of the number
- `z.modulus()` = returns the magnitude of the number
  - A real number: `sqrt(z.real^2 + z.imag^2)`
- `z.add(c)`= returns a new complex number representing the result of adding another complex number
  - Real part: `z.real + c.real`
  - Imaginary part: `z.imag + c.imag`
- `z.add(real)`= returns a new complex number representing the result of add the given real number
  - Real part: `z.real + real`
  - Imaginary part: `z.imag` (i.e. unchanged)
- `z.multiply(c)`= returns a new complex number representing the result of multiplying by another complex number
  - Real part: `z.real * c.real - z.imag * c.imag`
  - Imaginary part: `z.real * c.imag + z.imag * c.real`
- `z.multiply(real)`= returns a new complex number representing the result of multiplying by a real number
  - Real part: `z.real * real`
  - Imaginary part: `z.imag * real`

