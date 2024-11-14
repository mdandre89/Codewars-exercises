# Do you speak retsec?

 - URL:[https://www.codewars.com/kata/5516ab668915478845000780](https://www.codewars.com/kata/5516ab668915478845000780)
 - Id: 5516ab668915478845000780
 - Language: javascript
 - Completed on: 2017-03-22T17:18:29.526Z
 - Tags: Fundamentals
 - Description:
# Do you speak retsec?
You and your friends want to play undercover agents. In order to exchange your *secret* messages, you've come up with the following system: you take the word, cut it in half, and place the first half behind the latter. If the word has an uneven number of characters, you leave the middle at its previous place:

![retsec examples](http://i.imgur.com/Ozy6p09.png)

That way, you'll be able to exchange your messages in private.

# Task
You're given a single word. Your task is to swap the halves. If the word has an uneven length, leave the character in the middle at that position and swap the chunks around it.

## Examples
```javascript
reverseByCenter("secret")  == "retsec" // no center character
reverseByCenter("agent")   == "nteag"  // center character is "e"
```
```ruby
reverse_by_center("secret")  == "retsec" # no center character
reverse_by_center("agent")   == "nteag"  # center character is "e"
```
```python
reverse_by_center("secret")  == "retsec" # no center character
reverse_by_center("agent")   == "nteag"  # center character is "e"
```
```haskell
reverseByCenter "secret" `shouldBe` "retsec" -- no center character
reverseByCenter "agent"  `shouldBe` "nteag"  -- center character 'e'
```

## Remarks
Don't use this to actually exchange messages in private.
