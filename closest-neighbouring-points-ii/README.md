# Closest Neighbouring Points II

 - URL:[https://www.codewars.com/kata/55e47815d7055e1a97000128](https://www.codewars.com/kata/55e47815d7055e1a97000128)
 - Id: 55e47815d7055e1a97000128
 - Language: python
 - Completed on: 2017-10-09T08:43:44.020Z
 - Tags: Fundamentals,Algorithms,Mathematics
 - Description:
We need a function, closest_points3D() that may give an accurate result to find the closest pair or pairs of points that are contained in cube volumes of size l. The function will receive a list of variable number of points in a list (each point represented with cartesian coordinates(x, y, z)). All the values of x, y and z, will be positive integers. The function closest_points3D(), should display the results in the following way:

[(1), (2), (3)]

(1) - Number of points received
(2) - Pair or pairs of closest points in a sorted list of tuples(each tuple having the 3D coordinates (x, y, z) of the encountered closest points)
(3) - The distance of this pair or these pairs of found closes points, that is the minimal distance between every possible pair of the given of points. This value will be expessed as a float with at most, 5 decimal digits (rounded result).

Let's see some cases.
```python
l(size of the cube) = 10
listPointsI = [(9, 8, 5), (4, 2, 3), (10, 7, 4), (0, 9, 7), (3, 2, 6), (5, 8, 4), (1, 9, 6), (4, 5, 6), (5, 10, 10), (8, 8, 2)]
closest_points3D(listPointsI) -----> [10, [[(0, 9, 7), (1, 9, 6)]], 1.41421]

l = 20
listPointsII = [(19, 0, 1), (15, 17, 19), (19, 17, 0), (14, 5, 3), (18, 11, 7),\
 (12, 15, 19), (19, 7, 6), (12, 13, 3), (1, 2, 17), (10, 19, 20), (1, 4, 16),\
 (3, 17, 10), (18, 17, 15), (6, 3, 2), (17, 8, 3), (4, 14, 17), (7, 0, 3),\
 (3, 17, 18), (9, 4, 18), (16, 15, 13)]
closest_points3D(listPointsII) ------> [20, [[(1, 2, 17), (1, 4, 16)]], 2.23607]
```
(Your code should be able to process lists of points up to 1000 length in the allowed runtime for testing)
(You don't have to deal with the size of the cube (l) in your function, each set of points have been prepared for you with different values of l.)
Happy coding!!


