# Find the capitals

 - URL:[https://www.codewars.com/kata/539ee3b6757843632d00026b](https://www.codewars.com/kata/539ee3b6757843632d00026b)
 - Id: 539ee3b6757843632d00026b
 - Language: python
 - Completed on: 2017-03-10T15:24:26.743Z
 - Tags: Strings,Arrays,Fundamentals
 - Description:
# Instructions 

Write a function that takes a single string (`word`) as argument. The function must return an ordered list containing the indexes of all capital letters in the string.

# Example

```javascript
Test.assertSimilar( capitals('CodEWaRs'), [0,3,4,6] );
```
```ruby
Test.assert_equals( capitals('CodEWaRs'), [0,3,4,6] );
```
```haskell
capitals ""         `shouldBe` []
capitals "CodEWaRs" `shouldBe` [0,3,4,6]
capitals "aAbB"     `shouldBe` [1,3]
capitals "4ysdf4"   `shouldBe` []
capitals "ABCDEF"   `shouldBe` [0..5]
```
```csharp
Assert.AreEqual(Kata.Capitals("CodEWaRs"), new int[]{0,3,4,6});
```
