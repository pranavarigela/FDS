import pandas as pd
from statistics import mean, median, mode, stdev

data = [45, 50, 55, 60, 65, 70, 75, 80, 85, 90]

mean_val = mean(data)
median_val = median(data)
mode_val = mode(data)
std_dev = stdev(data)

print("Sample Data:", data)
print("Mean:", mean_val)
print("Median:", median_val)
print("Mode:", mode_val)
print("Standard Deviation:", std_dev)