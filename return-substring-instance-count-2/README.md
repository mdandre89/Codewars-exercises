# Return substring instance count - 2

 - URL:[https://www.codewars.com/kata/52190daefe9c702a460003dd](https://www.codewars.com/kata/52190daefe9c702a460003dd)
 - Id: 52190daefe9c702a460003dd
 - Language: python
 - Completed on: 2022-06-10T14:00:18.585Z
 - Tags: Strings,Regular Expressions,Search,Algorithms
 - Description:
Complete the solution so that it returns the number of times the search_text is found within the full_text.

```python
search_substr( full_text, search_text, allow_overlap = True )
```
```ruby
search_substr( full_text, search_text, allow_overlap = true )
```
```coffeescript
searchSubstr( fullText, searchText, allowOverlap = true )
```
```javascript
searchSubstr( fullText, searchText, allowOverlap = true )
```

so that overlapping solutions are (not) counted. If the searchText is empty, it should return `0`. Usage examples:

```python
search_substr('aa_bb_cc_dd_bb_e', 'bb') # should return 2 since bb shows up twice
search_substr('aaabbbcccc', 'bbb') # should return 1
search_substr( 'aaa', 'aa' ) # should return 2
search_substr( 'aaa', '' ) # should return 0
search_substr( 'aaa', 'aa', False ) # should return 1
```
```ruby
search_substr('aa_bb_cc_dd_bb_e', 'bb') # should return 2 since bb shows up twice
search_substr('aaabbbcccc', 'bbb') # should return 1
search_substr( 'aaa', 'aa' ) # should return 2
search_substr( 'aaa', '' ) # should return 0
search_substr( 'aaa', 'aa', false ) # should return 1
```
```coffeescript
searchSubstr('aa_bb_cc_dd_bb_e', 'bb') # should return 2 since bb shows up twice
searchSubstr('aaabbbcccc', 'bbb') # should return 1
searchSubstr( 'aaa', 'aa' ) # should return 2
searchSubstr( 'aaa', '' ) # should return 0
searchSubstr( 'aaa', 'aa', false ) # should return 1
```
```javascript
searchSubstr('aa_bb_cc_dd_bb_e', 'bb') // should return 2 since bb shows up twice
searchSubstr('aaabbbcccc', 'bbb') // should return 1
searchSubstr( 'aaa', 'aa' ) // should return 2
searchSubstr( 'aaa', '' ) // should return 0
searchSubstr( 'aaa', 'aa', false ) // should return 1
```
