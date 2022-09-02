# The Three Amigos

 - URL:[https://www.codewars.com/kata/59922d2ab14298db2b00003a](https://www.codewars.com/kata/59922d2ab14298db2b00003a)
 - Id: 59922d2ab14298db2b00003a
 - Language: python
 - Completed on: 2018-02-22T10:10:56.763Z
 - Tags: Algorithms
 - Description:
# Kata Task

Given a list of random integers, return the <span style='color:red'>Three Amigos</span>.

These are 3 numbers that live next to each other in the list, and who have the **most** in common with each other by these rules:
* lowest statistical <a href="https://en.wikipedia.org/wiki/Range_(statistics)">range</a>
* same <a href="https://en.wikipedia.org/wiki/Parity_(mathematics)">parity</a>

# Notes

* The list will contain at least 3 numbers
* If there is more than one answer then return the first one found (reading the list left to right)
* If there is no answer (e.g. no 3 adjacent numbers with same parity) then return an empty list.

# Examples

* ex1
 * Input = ```[1, 2, 34, 2, 1, 5, 3, 5, 7, 234, 2, 1]```
 * Result = ```[5,3,5]```
 

* ex2
 * Input = ```[2, 4, 6, 8, 10, 2, 2, 2, 1, 1, 1, 5, 3]```
 * Result = ```[2,2,2]```
 

* ex3
 * Input = ```[2, 4, 5, 3, 6, 3, 1, 56, 7, 6, 3, 12]```
 * Result = ```[]```

