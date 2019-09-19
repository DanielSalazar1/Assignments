# mode values
import statistics

values = [8,  11,  9,  14,  9,  15,  18,  6,  9,  10]
mode = statistics.mode(values)
print(mode) # Answer 9

# Calculate mode values
import statistics

values = [8, 9, 10, 10, 11, 11, 11, 12, 13]
mode = statistics.mode(values)
print(mode) #Answer 11

# Standard deviation

import statistics

sample = [5, 4, 3, 2, 1]
value = statistics.stdev(sample)
print("Standard Deviation of sample is % s" % value) # answer 1.5811388300841898

# Variance

import statistics

sample = [10, 9, 8, 7, 6, 5, 4]
value = statistics.variance(sample)
print("Variance of sample is % s " % value) # Answer 4.666666666666667
