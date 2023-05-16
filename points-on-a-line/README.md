# Points On A Line

 - URL:[https://www.codewars.com/kata/53b7bc844db8fde50800020a](https://www.codewars.com/kata/53b7bc844db8fde50800020a)
 - Id: 53b7bc844db8fde50800020a
 - Language: python
 - Completed on: 2017-10-13T11:57:10.550Z
 - Tags: Arrays,Geometry,Mathematics,Fundamentals
 - Description:
Given some points (cartesian coordinates), return true if all of them lie on a line.  Treat both an empty set and a single point as a line.

```javascript
onLine([[1,2], [7, 4], [22, 9]]);                 // returns true
onLine([[1,2], [-3, -14], [22, 9]]);              // returns false
```
```haskell
onLine [(1,2), (7, 4), (22, 9)]    `shouldBe` True
onLine [(1,2), (-3, -14), (22, 9)] `shouldBe` False
```
```ruby
on_line([[1,2], [7, 4], [22, 9]])    => returns true
on_line([[1,2], [-3, -14], [22, 9]]) => returns false
```
```python
on_line(((1,2), (7,4), (22,9)) == True
on_line(((1,2), (-3,-14), (22,9))) == False
```
