# Simple Sentences

 - URL:[https://www.codewars.com/kata/5297bf69649be865e6000922](https://www.codewars.com/kata/5297bf69649be865e6000922)
 - Id: 5297bf69649be865e6000922
 - Language: python
 - Completed on: 2020-12-11T12:42:58.039Z
 - Tags: Strings,Regular Expressions,Fundamentals
 - Description:
Implement a function, so it will produce a sentence out of the given parts.

Array of parts could contain:<br>
- words;<br>
- commas in the middle;<br>
- multiple periods at the end.<br>

Sentence making rules:<br>
- there must always be a space between words;<br>
- there must not be a space between a comma and word on the left;<br>
- there must always be one and only one period at the end of a sentence.<br>

**Example:**
```javascript
makeSentence(['hello', ',', 'my', 'dear']) // returns 'hello, my dear.'
```
```coffeescript
makeSentence ['hello', ',', 'my', 'dear'] # returns 'hello, my dear.'
```
```ruby
make_sentence ['hello', ',', 'my', 'dear'] # returns 'hello, my dear.'
```
