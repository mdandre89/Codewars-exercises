# To square(root) or not to square(root)

 - URL:[https://www.codewars.com/kata/57f6ad55cca6e045d2000627](https://www.codewars.com/kata/57f6ad55cca6e045d2000627)
 - Id: 57f6ad55cca6e045d2000627
 - Language: javascript
 - Completed on: 2017-02-13T16:37:19.945Z
 - Tags: Basic Language Features,Language Features,Mathematics,Arrays,Algorithms
 - Description:
Write a method, that will get an integer array as parameter and will process every number from this array.

Return a new array with processing every number of the input-array like this:

If the number has an integer square root, take this, otherwise square the number.

#### Example

```
[4,3,9,7,2,1] -> [2,9,3,49,4,1]
```

#### Notes

The input array will always contain only positive numbers, and will never be empty or null.

~~~if:lambdacalc
#### Encodings

purity: `LetRec`  
numEncoding: `Scott`  
export constructors `Nil, Cons` and deconstructor `foldr` for your `List` encoding  
~~~
