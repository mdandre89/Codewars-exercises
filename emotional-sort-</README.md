# Emotional Sort ( ︶︿︶)

 - URL:[https://www.codewars.com/kata/5a86073fb17101e453000258](https://www.codewars.com/kata/5a86073fb17101e453000258)
 - Id: 5a86073fb17101e453000258
 - Language: python
 - Completed on: 2018-02-22T10:22:44.154Z
 - Tags: Arrays,Fundamentals
 - Description:
## Emotional Sort ( ︶︿︶)

You'll have a function called "**sortEmotions**" that will return an array of **emotions** sorted. It has two parameters, the first parameter called "**arr**" will expect an array of **emotions** where an **emotion** will be one of the following:

- **:D** -> Super Happy
- **:)** -> Happy
- **:|** -> Normal
- **:(** -> Sad
- **T\_T** -> Super Sad

Example of the array:``[ 'T_T', ':D', ':|', ':)', ':(' ]``

And the second parameter is called "**order**", if this parameter is **true** then the order of the emotions will be descending (from **Super Happy** to **Super Sad**) if it's **false** then it will be ascending (from **Super Sad** to **Super Happy**)

Example if **order** is true with the above array: ``[ ':D', ':)', ':|', ':(', 'T_T' ]``

- Super Happy -> Happy -> Normal -> Sad -> Super Sad

If **order** is false: ``[ 'T_T', ':(', ':|', ':)', ':D' ]``

- Super Sad -> Sad -> Normal -> Happy -> Super Happy

Example:
```
arr = [':D', ':|', ':)', ':(', ':D']
sortEmotions(arr, true) // [ ':D', ':D', ':)', ':|', ':(' ]
sortEmotions(arr, false) // [ ':(', ':|', ':)', ':D', ':D' ]

```

**More in test cases!**

Notes:
- The array could be empty, in that case return the same empty array ¯\\\_( ツ )\_/¯
- All **emotions** will be valid

## Enjoy! (づ｡◕‿‿◕｡)づ
