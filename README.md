# Calculating easy percentiles

Now that you know how to plot the cumulative probability distribution lets get back to this business of trying to find the x values for a given value of y in a sentence like this one:

_y % of the data points are less than or equal to x._ 

We can proceed by recognising that if the data array `x` is sorted into ascending order it is easy to work out what fraction of data points are less than or equal to the ith element of the sorted array.  If there are `N` data points in the array we can thus calculate the percentage, `p`, of data points that are less than the `k`th element in the sorted array using:

![](https://render.githubusercontent.com/render/math?math=P=\frac{100k}{N-1})

__To complete this exercise you need to complete the function called `dataFraction` in the block on the left__.  `dataFraction` takes two variables in the input:

1. `data` is an np array containing a data set.  
2. `ind` is an integer, k, that indicates which element of the sorted data array you are interested in.

Your program should `return` the percentage of elements in data that are less than or equal to the index `ind` of `data` after this array has been sorted.

Think carefully before starting this exercise as it is simpler than it might at first appear.  __Notice that you do not need to sort data in order to complete this exercise and you also do not need to use any if statements.__
