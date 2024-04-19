# [Geometry A-2]: Length of a vector

 - URL:[https://www.codewars.com/kata/554dc2b88fbafd2e95000125](https://www.codewars.com/kata/554dc2b88fbafd2e95000125)
 - Id: 554dc2b88fbafd2e95000125
 - Language: python
 - Completed on: 2022-06-25T21:38:04.303Z
 - Tags: Geometry,Mathematics,Vectors,Fundamentals
 - Description:
For a given 2D vector described by cartesian coordinates of its initial point and terminal point in the following format:

```javascript
[[x1, y1], [x2, y2]]
```
```coffeescript
[[x1, y1], [x2, y2]]
```
```ruby
[[x1, y1], [x2, y2]]
```
```python
[[x1, y1], [x2, y2]]
```
```csharp
// Argument will be passed as a Vector2

public struct Vector2
{
  public Point2 Head;
  public Point2 Tail;
  
  public Vector2(Point2 tail, Point2 head)
  {
    this.Tail = tail;
    this.Head = head;
  }
  
  public Point2 this[int i]
  {
    get
    {
      return new Point2[] {this.Tail, this.Head}[i];
    }
  }
}

public struct Point2
{
  public double X;
  public double Y;
  
  public Point2(double x, double y)
  {
    this.X = x;
    this.Y = y;
  }
  
  public double this[int i]
  {
    get
    {
      return new double[] {this.X, this.Y}[i];
    }
  }
}
```

Your function must return this vector's length represented as a floating point number.

Error must be within 1e-7.

Coordinates can be integers or floating point numbers.
