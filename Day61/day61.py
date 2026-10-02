import numpy as np
from scipy.stats import norm

# ---- Exercise 1 ----
population_mean_claim = 2500

# H0: The population mean spending is equal to ₹2500.
# H1: The population mean spending is different from ₹2500.
# It is a two-sided test.

# ---- Exercise 2 ----

# Scenario A:
# H1: μ > 2500
# One-sided test because we only care whether the average increases.

# Scenario B:
# H1: μ < 10
# One-sided test because we only care whether the average decreases.

# Scenario C:
# H1: μ != 30
# Two-sided test because both an increase and a decrease would be considered different.

# ---- Exercise 3 ----
np.random.seed(42)

population = np.random.normal(
    loc=50,
    scale=10,
    size=10000
)

population_mean = np.mean(population)

print("Population mean:", population_mean)

sample = np.random.choice(population, size=50, replace=False)

sample_mean = np.mean(sample)
sample_std = np.std(sample, ddof=1)

print("Sample mean:", sample_mean)
print("Sample standard deviation:", sample_std)

# The sample mean is unlikely to be exactly 50 because random samples
# naturally vary from one sample to another.
# A sample mean different from 50 does not automatically mean H0 is false;
# we need to determine whether the difference is large enough to be statistically unusual.

# ---- Exercise 4 ----
mu_0 = 50

standard_error = sample_std / np.sqrt(len(sample))

z_score = (sample_mean - mu_0) / standard_error

print("Standard error:", standard_error)
print("Z-score:", z_score)

# ---- Exercise 5 ----
p_value = 2 * (1 - norm.cdf(abs(z_score)))

print("P-value:", p_value)
alpha = 0.05
if p_value <= alpha:
    print("Reject H0")
else:
    print("Fail to reject H0")
"""
The p-value is ______.
Since the p-value is greater than α = 0.05,
we fail to reject H0.
This means the sample provides insufficient evidence
that the population mean differs from 50.
"""
# ---- Exercise 6 ----
sample_sizes = [10, 30, 50, 100, 300]
for size in sample_sizes:
    sample = np.random.choice(
        population,
        size=size,
        replace=False
    )

    sample_mean = np.mean(sample)
    sample_std = np.std(sample, ddof=1)
    standard_error = sample_std / np.sqrt(size)

    z_score = (sample_mean - mu_0) / standard_error

    p_value = 2 * (1 - norm.cdf(abs(z_score)))

    print(
        "Sample size:", size,
        "Mean:", sample_mean,
        "SE:", standard_error,
        "Z:", z_score,
        "p-value:", p_value
    )

# ---- Exercise 7 ----
def hypothesis_test(sample, mu_0, alpha=0.05):
    mean = np.mean(sample)
    std = np.std(sample, ddof=1)
    se = std / np.sqrt(len(sample))

    z = (mean - mu_0) / se

    p_value = 2 * (1 - norm.cdf(abs(z)))

    if p_value <= alpha:
        decision = "Reject H0"
    else:
        decision = "Fail to reject H0"

    return mean, se, z, p_value, decision

sample = np.random.choice(population, size=50, replace=False)

result = hypothesis_test(sample, 50)

print(result)

mean, se, z, p_value, decision = result

print("Mean:", mean)
print("SE:", se)
print("Z-score:", z)
print("P-value:", p_value)
print("Decision:", decision)