# Excel's COUNTIF, SUMIF and AVERAGEIF functions

 - URL:[https://www.codewars.com/kata/56055244356dc5c45c00001e](https://www.codewars.com/kata/56055244356dc5c45c00001e)
 - Id: 56055244356dc5c45c00001e
 - Language: python
 - Completed on: 2017-03-19T15:14:50.297Z
 - Tags: Algorithms
 - Description:
##The Brief
Microsoft Excel provides a number of useful functions for counting, summing, and averaging values if they meet a certain criteria. Your task is to write three functions that work similarly to Excel's COUNTIF, SUMIF and AVERAGEIF functions.

##Specifications
Each function will take the same two arguments:

* A list object containing `values` to be counted, summed, or averaged.
* A `criteria` in either an integer, float, or string
    * Integer or float indicates equality
    * Strings can indicate >, >=, <, <= or <> (use the Excel-style "Not equal to" operator) to a number (ex. ">=3"). In the `count_if` function, a string without an operater indicates equality to this string.
    
The tests will all include properly formatted inputs. The test cases all avoid rounding issues associated with floats.

##Examples
 ```python
count_if([1,3,5,7,9], 3)
1

count_if(["John","Steve","John"], "John")
2

sum_if([2,4,6,-1,3,1.5],">0")
16.5

average_if([99,95.5,0,83],"<>0")
92.5
```

##Excel Function Documentation:
* [COUNTIF](https://support.office.com/en-us/article/COUNTIF-function-e0de10c6-f885-4e71-abb4-1f464816df34)
* [SUMIF](https://support.office.com/en-us/article/SUMIF-function-169b8c99-c05c-4483-a712-1697a653039b)
* [AVERAGEIF](https://support.office.com/en-us/article/AVERAGEIF-function-faec8e2e-0dec-4308-af69-f5576d8ac642)
