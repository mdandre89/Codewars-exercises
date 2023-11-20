# Ka Ka Ka cypher - words only vol 1

 - URL:[https://www.codewars.com/kata/5934d648d95386bc8200010b](https://www.codewars.com/kata/5934d648d95386bc8200010b)
 - Id: 5934d648d95386bc8200010b
 - Language: python
 - Completed on: 2017-11-26T16:25:59.465Z
 - Tags: Fundamentals
 - Description:
# Introduction 

Ka ka ka cypher is a cypher used by small children in some country. When a girl wants to pass something to the other girls and there are some boys nearby, she can use Ka cypher. So only the other girls are able to understand her. <br/>
She speaks using KA, ie.: <br>
`ka thi ka s ka bo ka y ka i ka s ka u ka gly` what simply means `this boy is ugly`. <br/>


# Task 

Write a function `KaCokadekaMe` (`ka_co_ka_de_ka_me` in Python) that accepts a string word and returns encoded message using ka cypher. <br/><br/>
Our rules:<br>
- The encoded word should start from `ka`.
- The `ka` goes after vowel (a,e,i,o,u)
- When there is multiple vowels together, the `ka` goes only after the last `vowel`
- When the word is finished by a vowel, do not add the `ka` after

# Input/Output

The `word` string consists of only lowercase and uppercase characters. There is only 1 word to convert - no white spaces.

# Example

```
KaCokadekaMe("a");  //=> "kaa"
KaCokadekaMe("ka");  //=> "kaka"
KaCokadekaMe("aa"); //=> "kaaa"  
KaCokadekaMe("Abbaa"); //=> kaAkabbaa
KaCokadekaMe("maintenance"); //=> kamaikantekanakance
KaCokadekaMe("Woodie"); //=> kaWookadie
KacokadekaMe("Incomprehensibilities"); //=> kaIkancokamprekahekansikabikalikatiekas
```

# Remark

Ka cypher's country residents, please don't hate me for simplifying the way how we divide the words into "syllables" in the Kata. I don't want to make it too hard for other nations ;-P 
