# Pyramid Array

 - URL:[https://www.codewars.com/kata/515f51d438015969f7000013](https://www.codewars.com/kata/515f51d438015969f7000013)
 - Id: 515f51d438015969f7000013
 - Language: python
 - Completed on: 2022-06-25T10:51:42.342Z
 - Tags: Algorithms
 - Description:
Write a function that when given a number >= 0, returns an Array of ascending length subarrays.

```
pyramid(0) => [ ]
pyramid(1) => [ [1] ]
pyramid(2) => [ [1], [1, 1] ]
pyramid(3) => [ [1], [1, 1], [1, 1, 1] ]
```

**Note:** the subarrays should be filled with `1`s

```if:c
Subarrays should not overlap; this will be tested.
Dont forget to de-allocate memory in `free_pyramid()`
```
