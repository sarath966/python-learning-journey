import numpy as np
import matplotlib.pyplot as plt

# ------ Exericse 1 ------
population = np.random.normal(loc=50, scale=10, size=1000)
sample = np.random.choice(population, size=50, replace=False)
sample_mean = np.mean(sample)
sample_std = np.std(sample, ddof=1)
standard_error = sample_std / np.sqrt(len(sample))

print("Sample mean:", sample_mean)
print("Sample standard deviation:", sample_std)
print("Standard error:", standard_error)

# -------- Exercise 2 -------
margin_of_error = 1.96 * standard_error

lower = sample_mean - margin_of_error
upper = sample_mean + margin_of_error

print("95% CI:", lower, upper)

# -------- Exercise 3 -------
# A 95% confidence interval gives a range of plausible values
# produced by a confidence-interval procedure for estimating the population mean.
# Across many repeated samples, about 95% of intervals constructed this way
# would contain the true population mean.

# ------- Exercise 4 -------
sample_sizes = [10, 30, 50, 100, 300]

for size in sample_sizes:
    sample = np.random.choice(population, size=size, replace=False)

    sample_std = np.std(sample, ddof=1)
    standard_error = sample_std / np.sqrt(size)
    margin_of_error = 1.96 * standard_error

    print(
        "Sample size:", size,
        "SE:", standard_error,
        "Margin of error:", margin_of_error
    )
# As sample size increases, the standard error and margin of error generally decrease,
# so the estimate of the population mean becomes more precise.

# ------- Exercise 5 -------
def confidence_interval(sample):
    mean = np.mean(sample)
    std = np.std(sample, ddof=1)
    se = std / np.sqrt(len(sample))
    margin = 1.96 * se

    lower = mean - margin
    upper = mean + margin

    return lower, upper

sample = np.random.choice(population, size=50, replace=False)

lower, upper = confidence_interval(sample)

print("Lower:", lower)
print("Upper:", upper)

# ------ Exercise 6 ------
population = np.random.normal(loc=50, scale=10, size=100)
population_mean = np.mean(population)

inside = 0

for i in range(100):
    sample = np.random.choice(population, size=50, replace=False)

    lower, upper = confidence_interval(sample)

    if lower <= population_mean <= upper:
        inside += 1

print("Intervals containing population mean:", inside)

# ------- Exercise 7 ------
sample_means = []
lower_bounds = []
upper_bounds = []
population = np.random.normal(loc=50, scale=10, size=1000)
for i in range(20):
    sample = np.random.choice(population, size=50, replace=False)
    sample_mean = np.mean(sample)
    sample_means.append(sample_mean)
    lower, upper = confidence_interval(sample)
    lower_bounds.append(lower)
    upper_bounds.append(upper)

plt.errorbar(
    range(len(sample_means)),
    sample_means,
    yerr=[
        np.array(sample_means) - np.array(lower_bounds),
        np.array(upper_bounds) - np.array(sample_means)
    ],
    fmt="o"
)

plt.axhline(population_mean, linestyle="--")
plt.xlabel("Sample")
plt.ylabel("Estimated Mean")
plt.title("95% Confidence Intervals")
plt.show()