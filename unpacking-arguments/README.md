# Unpacking Arguments

 - URL:[https://www.codewars.com/kata/540de1f0716ab384b4000828](https://www.codewars.com/kata/540de1f0716ab384b4000828)
 - Id: 540de1f0716ab384b4000828
 - Language: python
 - Completed on: 2022-06-14T14:18:46.702Z
 - Tags: Functional Programming,Fundamentals
 - Description:
You must create a function, `spread`, that takes a function and a list of arguments to be applied to that function. You must make this function return the result of calling the given function/lambda with the given arguments.

eg:
```javascript
spread(someFunction, [1, true, "Foo", "bar"] ) 
// is the same as...
someFunction(1, true, "Foo", "bar")
```
```clojure
(spread someFunction [1 true "Foo" "bar"] ) 
; is the same as...
(someFunction 1 true "Foo" "bar")
```
```coffeescript
spread someFunction, [1, true, "Foo", "bar"] 
# is the same as...
someFunction 1, true, "Foo", "bar" 
```
```python
spread(someFunction, [1, true, "Foo", "bar"] ) 
# is the same as...
someFunction(1, true, "Foo", "bar")
```
```ruby
spread someFunction, [1, true, "Foo", "bar"] 
# is the same as...
someFunction.(1, true, "Foo", "bar")
```
