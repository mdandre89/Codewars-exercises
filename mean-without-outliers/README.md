# Mean without outliers

 - URL:[https://www.codewars.com/kata/5962d557be3f8bb0ca000010](https://www.codewars.com/kata/5962d557be3f8bb0ca000010)
 - Id: 5962d557be3f8bb0ca000010
 - Language: python
 - Completed on: 2017-11-22T08:40:00.419Z
 - Tags: Recursion,Statistics,Mathematics,Algorithms
 - Description:
The mean and standard deviation of a sample of data can be thrown off if the sample contains one or many outlier(s) :

<img src = 'http://www.ukoln.ac.uk/web-focus/webwatch/reports/hei-lib-may1998/fig11.gif' href = 'http://www.ukoln.ac.uk/web-focus/webwatch/reports/hei-lib-may1998/report.html'><div></div>
(<a href = 'http://www.ukoln.ac.uk/web-focus/webwatch/reports/hei-lib-may1998/report.html'>image source</a>)

For this reason, it is usually a good idea to check for and remove outliers before computing the mean or the standard deviation of a sample. To this aim, your function will receive a list of numbers representing a <code>sample</code> of data. Your function must remove any outliers and return the mean of the <code>sample</code>, <strong>rounded</strong> to <strong>two</strong> decimal places (round only at the end).

Since there is no objective definition of "outlier" in statistics, your function will also receive a <code>cutoff</code>, in standard deviation units. So for example if the cutoff is 3, then any value that is <strong>more</strong> than 3 standard deviations above or below the mean must be removed. <em>Notice that, once outlying values are removed in a first "sweep", other less extreme values may then "become" outliers, that you'll have to remove as well!</em>

<strong>Example :</strong>
```python
sample = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 100]
cutoff = 3
clean_mean(sample, cutoff) → 5.5
```
```r
# R uses sam instead of sample to avoid conflicts with the
# base function sample()
sam <- c(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 100)
cutoff <- 3
clean_mean(sam, cutoff)
[1] 5.5
```

<strong>Formula for the <a href = 'https://en.wikipedia.org/wiki/Mean'>mean</a> :</strong>

<img src = 'https://wikimedia.org/api/rest_v1/media/math/render/svg/bd2f5fb530fc192e4db7a315777f5bbb5d462c90' style="background-color:lightgray"><div></div>
(where n is the sample size)

<strong>Formula for the <a href = 'https://en.wikipedia.org/wiki/Standard_deviation#Estimation'>standard deviation</a> :</strong>

<img src = 'https://wikimedia.org/api/rest_v1/media/math/render/svg/9a937016f00f1978197aa562c5f2d58619f90806' style="background-color:lightgray"><div></div>
(where N is the sample size, x<sub>i</sub> is observation i and x̄ is the sample mean)

<em>Note : since we are not computing the sample standard deviation for inferential purposes, the denominator is n, not n - 1.</em>
