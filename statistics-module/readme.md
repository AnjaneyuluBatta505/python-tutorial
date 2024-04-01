# Python - Statistics module

* It provides functions for calculating mathematical statistics of numeric (Real-valued) data.

## Averages and measures of central location

| Function                 | Description                                                      | Example                                         |
| ------------------------ | ---------------------------------------------------------------- | ----------------------------------------------- |
| *mean(data)*           | Arithmetic mean (i.e "average") of data.                         | **`statistics.mean([-1.5, 2, 4, 3])`**  |
| *fmean(data)*          | Convert data to floats and compute the arithmetic mean.          | `statistics.fmean([-1.5, 2, 4, 3])`           |
| *geometric_mean(data)* | Convert data to floats and compute the geometric mean.           | `statistics.geometric_mean([54, 24, 36])`     |
| *harmonic_mean(data)*  | Return the harmonic mean of data.                                | `statistics.harmonic_mean([24, 36])`          |
| *median(data)*         | Return the median (middle value) of numeric data.                | `statistics.median([1, 3, 5, 7])`             |
| *median_low(data)*     | Return the low median of numeric data.                           | `statistics.median_low([1, 3, 5, 7])`         |
| *median_high(data)*    | Return the high median of data.                                  | `statistics.median_high([1, 3, 5, 7])`        |
| *median_grouped(data)* | Return the 50th percentile (median) of grouped continuous data.  | `statistics.median_grouped([52, 52, 53, 54])` |
| *mode(data)*           | Single mode (i.e most common value) of discrete or nominal data. | `statistics.mode([52, 52, 53, 54])`           |
| *multimode(data)*      | List of modes (most common values) of discrete or nominal data.  | `statistics.multimode([52, 52, 53, 54])`      |
| *quantiles(data)*      | Divide data into intervals with equal probability.               | `statistics.quantiles([3,4,5,7,9,11,13])`     |

## Measures of spread

| Function            | Description                            | Example                                                                  |
| ------------------- | -------------------------------------- | ------------------------------------------------------------------------ |
| *pstdev(data)*    | Population standard deviation of data. | `statistics.pstdev([1.5, 2.5, 2.5, 2.75, 3.25, 4.75])`                 |
| *pvariance(data)* | Return the population variance of data | `statistics.pvariance([0.0, 0.25, 0.25, 1.25, 1.5, 1.75, 2.75, 3.25])` |
| *stdev(data)*     | Sample standard deviation of data.     | `statistics.stdev([1.5, 2.5, 2.5, 2.75, 3.25, 4.75])`                  |
| *variance(data)*  | Return the sample variance of data.    | `statistics.variance([2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5])`        |

## Statistics for relations between two inputs

| Function                            | Description                                       | Example                                                |
| ----------------------------------- | ------------------------------------------------- | ------------------------------------------------------ |
| *covariance(data1, data1)*        | Sample covariance for two variables.              | `statistics.covariance([1,2,3,4],[1,2,4,5])`         |
| *correlation(data1, data1)*       | Pearson and Spearman’s correlation coefficients. | `statistics.correlation([1,2,3,4],[1,2,4,5])`        |
| *linear_regression(data1, data1)* | Slope and intercept for simple linear regression. | `statistics.linear_regression([1,2,3,4], [1,2,4,5])` |

### References:

* [https://docs.python.org/3/library/statistics.html](https://docs.python.org/3/library/statistics.html)


.
