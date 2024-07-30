# extract file name

 - URL:[https://www.codewars.com/kata/597770e98b4b340e5b000071](https://www.codewars.com/kata/597770e98b4b340e5b000071)
 - Id: 597770e98b4b340e5b000071
 - Language: python
 - Completed on: 2017-10-21T11:25:43.320Z
 - Tags: Regular Expressions,Fundamentals
 - Description:
You have to extract a portion of the file name as follows:

* Assume it will start with date represented as long number
* Followed by an underscore
* You'll have then a filename with an extension
* it will always have an extra extension at the end

Inputs:
---
```
1231231223123131_FILE_NAME.EXTENSION.OTHEREXTENSION

1_This_is_an_otherExample.mpg.OTHEREXTENSIONadasdassdassds34

1231231223123131_myFile.tar.gz2
```

Outputs
---

```
FILE_NAME.EXTENSION

This_is_an_otherExample.mpg

myFile.tar
```

Acceptable characters for random tests:

`abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_-0123456789`

The recommended way to solve it is using RegEx and specifically groups.
