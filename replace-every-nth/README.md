# Replace every nth

 - URL:[https://www.codewars.com/kata/57fcaed83206fb15fd00027a](https://www.codewars.com/kata/57fcaed83206fb15fd00027a)
 - Id: 57fcaed83206fb15fd00027a
 - Language: python
 - Completed on: 2017-02-25T14:20:40.940Z
 - Tags: Basic Language Features,Language Features,Algorithms
 - Description:
## Task

Write a method, that replaces every nth char _oldValue_ with char _newValue_.

Method:
```c
replaceNth(const char* text, int n, char oldValue, char newValue)
```
```csharp
ReplaceNth(string text, int n, char oldValue, char newValue)
```
```javascript
replaceNth(text, n, oldValue, newValue)
```
```clojure
(replace-nth text n old-val new-val)
```
```coffeescript
replaceNth = (text, n, oldValue, newValue)
```
```typescript
replaceNth(text:string, n:number, oldValue:string, newValue:string):string
```
```java
replaceNth(String text, int n, char oldValue, char newValue)
```
```fsharp
let replaceNth text n oldValue newValue = 
```
```cpp
replaceNth(std::string text, int n, char oldValue, char newValue)
```
```python
replace_nth(text, int, old, new)
```
```ruby
replace_nth (text, n, old_value, new_value)
```

## Example:
```
n:         2
oldValue: 'a'
newValue: 'o'
"Vader said: No, I am your father!" -> "Vader soid: No, I am your fother!"
  1     2          3        4       -> 2nd and 4th occurence are replaced
```

Your method has to be case sensitive!

As you can see in the example: The first changed is the 2nd 'a'. So the start is always at the nth suitable char and not at the first!

If n is 0 or negative or if it is larger than the count of the oldValue, return the original text without a change. <br><br>
The text and the chars will never be null.

Have fun coding it and please don't forget to vote and rank this kata! :-) 

I have created other katas. Have a look if you like coding and challenges.

