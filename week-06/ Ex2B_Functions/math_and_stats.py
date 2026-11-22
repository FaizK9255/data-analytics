import random
import math
import statistics

vals_1_100 = range(1,101)
vals_sample = random.sample(vals_1_100, 75)
vals_choices = random.choices(vals_1_100, k = 200)
radius = random.randint(3,10)
pi = math.pi

# Experimenting with a subset of integers 1-100:
sample_sum = sum(vals_sample)
sample_average = statistics.mean(vals_sample)
sample_median = statistics.median(vals_sample)

print("Experimenting with a subset of integers 1-100:")
print('-' * 30)
print(f"Sum of 75 sample values from 1 to 100: {sample_sum}")
print(f"Average of 75 sample values: {sample_average}")
print(f"Median of 75 sample values: {sample_median}")

# Experimenting with a superset of 200 values, integers 1-100
choices_average = statistics.mean(vals_choices)
choices_median = statistics.median(vals_choices)
choices_mode = statistics.mode(vals_choices)
choices_stdev = statistics.stdev(vals_choices)
choices_variance = statistics.variance(vals_choices)

print("\n Experimenting with a superset of 200 values, integers 1-100:")
print('-' * 30)
print(f"Average of 200 values: {choices_average}")
print(f"Median of 200 values: {choices_median}")
print(f"Mode of 200 values: {choices_mode}")
print(f"Standard deviation of 200 values: {choices_stdev}")
print(f"Variance of 200 values: {choices_variance}")

# Modeling a random circle:
area = pi * radius ** 2
area_round_up = math.ceil(area)
area_round_down = math.floor(area)

print("\n Modeling a random circle:")
print('-' * 30)
print(f"Radius = {radius}, area = {area_round_up} (rounded up to the nearest integer)")
print(f"Radius = {radius}, area = {area_round_down} (rounded down to the nearest integer)")