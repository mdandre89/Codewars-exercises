# Calculate the area of a regular n sides polygon inside a circle of radius r

 - URL:[https://www.codewars.com/kata/5a58ca28e626c55ae000018a](https://www.codewars.com/kata/5a58ca28e626c55ae000018a)
 - Id: 5a58ca28e626c55ae000018a
 - Language: python
 - Completed on: 2018-02-03T21:36:27.032Z
 - Tags: Mathematics,Geometry,Fundamentals
 - Description:
Write the following function:

```javascript
function areaOfPolygonInsideCircle(circleRadius, numberOfSides)
```
```haskell
areaOfPolygonInsideCircle :: Double -> Int -> Double
areaOfPolygonInsideCircle circleRadius numberOfSides = undefined
```
```php
function areaOfPolygonInsideCircle($circleRadius, $numberOfSides)
```
```csharp
public static double AreaOfPolygonInsideCircle(double circleRadius, int numberOfSides)
```
```clojure
(defn area-of-polygon-inside-circle [circle-radius number-of-sides]
```
```python
def area_of_polygon_inside_circle(circle_radius, number_of_sides):
```
```elixir
def area_of_polygon_inside_circle(circle_radius, number_of_sides) do
```
```ruby
def area_of_polygon_inside_circle(circle_radius, number_of_sides)
```
```crystal
def area_of_polygon_inside_circle(circle_radius, number_of_sides)
```
```groovy
static double areaOfPolygonInsideCircle(circleRadius, numberOfSides)
```
```cpp
double areaOfPolygonInsideCircle (double circleRadius , int numberOfSides)
```
```swift
areaOfPolygonInsideCircle(_ circleRadius: Double, _ numberOfSides: Int) -> Double
```
```objc
double area_of_polygon_inside_circle(double circle_radius, int number_of_sides);
```
```c
double area_of_polygon_inside_circle(double circle_radius, int number_of_sides);
```
```dart
double areaOfPolygonInsideCircle(double circleRadius, int numberOfSides)
```
```coffeescript
areaOfPolygonInsideCircle = (circleRadius, numberOfSides)
```
```typescript
export function areaOfPolygonInsideCircle(circleRadius: number, numberOfSides: number): number
```
```java
public static double areaOfPolygonInsideCircle(double circleRadius, int numberOfSides) 
```
```coffeescript
areaOfPolygonInsideCircle = (circleRadius, numberOfSides)
```
```go
func AreaOfPolygonInsideCircle(circleRadius float64, numberOfSides int) float64
```

It should calculate the area of a regular polygon of `numberOfSides`, `number-of-sides`, or `number_of_sides` sides inside a circle of radius `circleRadius`, `circle-radius`, or `circle_radius` which passes through all the vertices of the polygon (such circle is called [**circumscribed circle** or **circumcircle**](https://en.wikipedia.org/wiki/Circumscribed_circle)). The answer should be a number rounded to 3 decimal places. 

Input :: Output Examples 

```javascript
areaOfPolygonInsideCircle(3, 3) // returns 11.691

areaOfPolygonInsideCircle(5.8, 7) // returns 92.053

areaOfPolygonInsideCircle(4, 5) // returns 38.042
```
```haskell
areaOfPolygonInsideCircle 3 3 -- returns 11.691

areaOfPolygonInsideCircle 5.8 7 -- returns 92.053

areaOfPolygonInsideCircle 4 5 -- returns 38.042
```
```dart
areaOfPolygonInsideCircle(3.0, 3) // returns 11.691

areaOfPolygonInsideCircle(5.8, 7) // returns 92.053

areaOfPolygonInsideCircle(4.0, 5) // returns 38.042
```
```php
areaOfPolygonInsideCircle(3, 3) // returns 11.691

areaOfPolygonInsideCircle(5.8, 7) // returns 92.053

areaOfPolygonInsideCircle(4, 5) // returns 38.042
```
```cpp
areaOfPolygonInsideCircle (3, 3) // returns 11.691

areaOfPolygonInsideCircle (5.8, 7) // returns 92.053

areaOfPolygonInsideCircle (4, 5) // returns 38.042
```
```groovy
areaOfPolygonInsideCircle(3, 3) // returns 11.691

areaOfPolygonInsideCircle(5.8, 7) // returns 92.053

areaOfPolygonInsideCircle(4, 5) // returns 38.042
```
```csharp
AreaOfPolygonInsideCircle(3, 3) // returns 11.691

AreaOfPolygonInsideCircle(5.8, 7) // returns 92.053

AreaOfPolygonInsideCircle(4, 5) // returns 38.042
```
```python
area_of_polygon_inside_circle(3, 3) # returns 11.691

area_of_polygon_inside_circle(5.8, 7) # returns 92.053

area_of_polygon_inside_circle(4, 5) # returns 38.042
```
```elixir
area_of_polygon_inside_circle(3, 3) # returns 11.691

area_of_polygon_inside_circle(5.8, 7) # returns 92.053

area_of_polygon_inside_circle(4, 5) # returns 38.042
```
```clojure
(area-of-polygon-inside-circle 3 3) ; returns 11.691

(area-of-polygon-inside-circle 5.8 7) ; returns 92.053

(area-of-polygon-inside-circle 4 5) ; returns 38.042
```
```objc
area_of_polygon_inside_circle(3, 3); // => 11.691

area_of_polygon_inside_circle(5.8, 7); // => 92.053

area_of_polygon_inside_circle(4, 5); // => 38.042
```
```c
area_of_polygon_inside_circle(3, 3); // => 11.691

area_of_polygon_inside_circle(5.8, 7); // => 92.053

area_of_polygon_inside_circle(4, 5); // => 38.042
```
```swift
areaOfPolygonInsideCircle(3, 3); // => 11.691

areaOfPolygonInsideCircle(5.8, 7); // => 92.053

areaOfPolygonInsideCircle(4, 5); // => 38.042
```
```ruby
area_of_polygon_inside_circle(3, 3) # returns 11.691

area_of_polygon_inside_circle(5.8, 7) # returns 92.053

area_of_polygon_inside_circle(4, 5) # returns 38.042
```
```crystal
area_of_polygon_inside_circle(3, 3) # returns 11.691

area_of_polygon_inside_circle(5.8, 7) # returns 92.053

area_of_polygon_inside_circle(4, 5) # returns 38.042
```
```coffeescript
areaOfPolygonInsideCircle(3, 3) # returns 11.691

areaOfPolygonInsideCircle(5.8, 7) # returns 92.053

areaOfPolygonInsideCircle(4, 5) # returns 38.042
```
```typescript
areaOfPolygonInsideCircle(3, 3) // returns 11.691

areaOfPolygonInsideCircle(5.8, 7) // returns 92.053

areaOfPolygonInsideCircle(4, 5) // returns 38.042
```
```java
areaOfPolygonInsideCircle(3, 3) // returns 11.691

areaOfPolygonInsideCircle(5.8, 7) // returns 92.053

areaOfPolygonInsideCircle(4, 5) // returns 38.042
```
```go
AreaOfPolygonInsideCircle(3, 3) // returns 11.691

AreaOfPolygonInsideCircle(5.8, 7) // returns 92.053

AreaOfPolygonInsideCircle(4, 5) // returns 38.042
```
