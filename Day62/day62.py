import numpy as np
from scipy.stats import ttest_1samp

np.random.seed(42)

sample = np.random.normal(
    loc=2700,
    scale=450,
    size=25
)
mu_0 = 2500
t_stat, p_value = ttest_1samp(sample, mu_0)

print("Sample mean:", np.mean(sample))
print("t-statistic:", t_stat)
print("p-value:", p_value)
alpha = 0.05

if p_value <= alpha:
    print("Reject H0")
else:
    print("Fail to reject H0")

# ---- Exercise 1 ----
np.random.seed(42)

sample = np.random.normal(
    loc=2700,
    scale=450,
    size=30
)
print(np.mean(sample))
print(sample.std(ddof=1))
print(sample.size)

# ---- Exercise 2 ----
# H0: The population mean customer spending is equal to ₹2500.
# H1: The population mean customer spending is different from ₹2500.
# Test type: Two-sided one-sample t-test

# ---- Exercise 3 ----
t_stat, p_value = ttest_1samp(sample, 2500)
print(sample.mean())
print(t_stat)
print(p_value)

# ---- Exercise 4 ----
alpha = 0.05
if p_value <= alpha:
    print("Reject H0")
else:
    print("Fail to reject H0")

# The test compares the sample mean customer spending with the company's
# claimed population mean of ₹2500.
# If p-value <= 0.05, there is sufficient evidence that the population mean
# differs from ₹2500.
# If p-value > 0.05, there is insufficient evidence to conclude that the
# population mean differs from ₹2500.

# ---- Exercise 5 ----
sample_sizes = [10, 30, 50, 100, 300]
for n in sample_sizes:
    sample = np.random.normal(
    loc=2700,
    scale=450,
    size=n)
    t_stat, p_value = ttest_1samp(sample, 2500)
    print(sample.size)
    print(sample.mean())
    print(t_stat)
    print(p_value)

    alpha = 0.05
    if p_value <= alpha:
        print("Reject H0")
    else:
        print("Fail to reject H0")
# ---- Exercise 5 interpretation ----
# As sample size increases, the standard error generally decreases,
# making the estimate of the population mean more precise.
# However, individual p-values can still vary because each sample
# is randomly generated.


# ---- Exercise 6 ----

# Scenario A: Is average customer spending different from ₹2500?
t_stat_two_sided, p_two_sided = ttest_1samp(
    sample, 2500, alternative="two-sided"
)

# Scenario B: Is average customer spending greater than ₹2500?
t_stat_greater, p_greater = ttest_1samp(
    sample, 2500, alternative="greater"
)

# Scenario C: Is average customer spending less than ₹2500?
t_stat_less, p_less = ttest_1samp(
    sample, 2500, alternative="less"
)

print("\nExercise 6")
print("Two-sided p-value:", p_two_sided)
print("Greater-than p-value:", p_greater)
print("Less-than p-value:", p_less)

# ---- Exercise 7 ----

def one_sample_t_test(sample, mu_0, alpha=0.05):

    sample_mean = np.mean(sample)
    sample_std = np.std(sample, ddof=1)
    sample_size = len(sample)

    t_stat, p_value = ttest_1samp(sample, mu_0)

    if p_value <= alpha:
        decision = "Reject H0"
    else:
        decision = "Fail to reject H0"

    return {
        "sample_mean": sample_mean,
        "sample_std": sample_std,
        "sample_size": sample_size,
        "t_statistic": t_stat,
        "p_value": p_value,
        "decision": decision
    }


result = one_sample_t_test(sample, 2500)

print("\nExercise 7")

for key, value in result.items():
    print(f"{key}: {value}")


# ---- Exercise 8 ----

# The company claims that average customer spending is ₹2500.
# The sample mean is approximately ₹2702.02.
# The one-sample t-test produced a p-value of approximately 8.55 × 10⁻¹⁴.
# At α = 0.05, we reject H0.
# This provides sufficient statistical evidence that average customer spending differs from the company's ₹2500 claim.


# ---- Exercise 9 ----

# z-test vs t-test
#
# z-test:
# - Population standard deviation (σ) is known.
# - Uses the population standard deviation.
# - Uses the standard normal distribution.
# - Does not use sample degrees of freedom.
# - Appropriate when population variability is known.
#
# t-test:
# - Population standard deviation (σ) is unknown.
# - Uses the sample standard deviation (s).
# - Uses the t-distribution.
# - One-sample t-test uses df = n - 1.
# - Commonly used with real-world sample data.


# ---- Mini Challenge ----

np.random.seed(123)

delivery_times = np.random.normal(
    loc=32,
    scale=6,
    size=40
)

delivery_mean = np.mean(delivery_times)
delivery_std = np.std(delivery_times, ddof=1)

t_delivery, p_delivery = ttest_1samp(
    delivery_times,
    30,
    alternative="two-sided"
)

alpha = 0.05

if p_delivery <= alpha:
    delivery_decision = "Reject H0"
else:
    delivery_decision = "Fail to reject H0"

print("\nMini Challenge")
print("Sample mean:", delivery_mean)
print("Sample standard deviation:", delivery_std)
print("t-statistic:", t_delivery)
print("p-value:", p_delivery)
print("Alpha:", alpha)
print("Decision:", delivery_decision)
