# Exclamation marks series #17: Put the exclamation marks and question marks on the balance - are they balanced?

 - URL:[https://www.codewars.com/kata/57fb44a12b53146fe1000136](https://www.codewars.com/kata/57fb44a12b53146fe1000136)
 - Id: 57fb44a12b53146fe1000136
 - Language: javascript
 - Completed on: 2017-08-30T17:10:40.872Z
 - Tags: Fundamentals
 - Description:
Each exclamation mark's weight is 2; each question mark's weight is 3. Putting two strings `left` and `right` on the balance - are they balanced?
 
If the left side is more heavy, return `"Left"`; if the right side is more heavy, return `"Right"`; if they are balanced, return `"Balance"`.

## Examples

```python
"!!", "??"     -->  "Right"
"!??", "?!!"   -->  "Left"
"!?!!", "?!?"  -->  "Left"
"!!???!????", "??!!?!!!!!!!"  -->  "Balance"
```
```haskell
-- For Haskell use the Comparison type defined in Preloaded code
-- data Comparison = Left | Right | Balance deriving (Show, Eq, Enum, Bounded)

balance :: String -> String -> Comparison

balance "!!" "??" == Right
balance "!??" "?!!" == Left
balance "!?!!" "?!?" == Left
balance "!!???!????" "??!!?!!!!!!!" == Balance
```
