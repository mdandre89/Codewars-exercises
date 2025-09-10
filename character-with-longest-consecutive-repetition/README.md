# Character with longest consecutive repetition

 - URL:[https://www.codewars.com/kata/586d6cefbcc21eed7a001155](https://www.codewars.com/kata/586d6cefbcc21eed7a001155)
 - Id: 586d6cefbcc21eed7a001155
 - Language: python
 - Completed on: 2017-10-09T17:03:02.070Z
 - Tags: Strings,Fundamentals,Algorithms
 - Description:
For a given string `s` find the character `c` (or `C`) with longest consecutive repetition and return:

```c
c
(assign l to pointer)
```
```lua
{ character = c, length = l }
```
```go
type Result struct {
	C rune // character
	L int  // count
}
```
```python
(c, l)
```
```haskell
Just (Char, Int)
```
```csharp
Tuple<char?, int>(c, l)
```
```shell
# in Shell a String of comma-separated values
c,l
```
```javascript
[c, l]
```
```ruby
[c, l]
```
```groovy
[c, l]
```
```coffeescript
[c, l]
```
```java
Object[]{c, l};
```
```typescript
[c, l]: [string, number]
```
```scala
(c, l)
```
```nim
(c, l)
```
```kotlin
Pair(c, l)
```
```vb
Tuple(Of Char?, Integer>(c, l)
```
```elixir
{c, l}
```
```rust
Some((c, l))
```
```perl
[c, l]
```


where `l` (or `L`) is the length of the repetition. If there are two or more characters with the same `l` return the first in order of appearance.

For empty string return:

```c
'\0'
(assign 0 to pointer)
```
```lua
{character = "", length = 0 }
```
```go
Result{}
```
```python
('', 0)
```
```haskell
Nothing
```
```csharp
Tuple<char?, int>(null, 0)
```
```shell
,0
```
```javascript
["", 0]
```
```groovy
["", 0]
```
```ruby
["", 0]
```
```coffeescript
["", 0]
```
```java
Object[]{"", 0}
```
```typescript
["", 0]
```
```scala
("", 0)
```
```nim
('\0', 0)
```
```kotlin
Pair(null, 0)
```
```vb
Tuple(Of Char?, Integer)(Nothing, 0)
```
```elixir
{"", 0}
```
```rust
None
```
```swift
["": 0]
```
```perl
["", 0]
```

In **JavaScript**: If you use `Array.sort` in your solution, you might experience issues with the random tests as `Array.sort` is not stable in the Node.js version used by CodeWars. This is not a kata issue.

Happy coding! :)
