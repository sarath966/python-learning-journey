import numpy as np
from scipy.stats import ttest_ind

# ---- Exercise 1 ----
np.random.seed(42)

control = np.random.normal(
    loc=100,
    scale=15,
    size=50
)

treatment = np.random.normal(
    loc=108,
    scale=15,
    size=50
)
print(control.mean())
print(treatment.mean())
print(control.std(ddof=1))
print(treatment.std(ddof=1))

# ---- Exercise 2 ----

t_stat, p_value = ttest_ind(
    control,
    treatment,
    equal_var=False
)
alpha = 0.05
if p_value <= alpha:
    print("Reject H0")
else:
    print("Fail to reject H0")

# ---- Exercise 3 ----

mean_difference = np.mean(treatment) - np.mean(control)

pooled_std = np.sqrt(
    (
        (len(control) - 1) * np.var(control, ddof=1)
        + (len(treatment) - 1) * np.var(treatment, ddof=1)
    )
    / (len(control) + len(treatment) - 2)
)

cohens_d = mean_difference / pooled_std

print("\nExercise 3")
print("Mean difference:", mean_difference)
print("Pooled standard deviation:", pooled_std)
print("Cohen's d:", cohens_d)

if abs(cohens_d) < 0.2:
    print("Effect size: Negligible")
elif abs(cohens_d) < 0.5:
    print("Effect size: Small")
elif abs(cohens_d) < 0.8:
    print("Effect size: Medium")
else:
    print("Effect size: Large")

# ---- Exercise 4 ----

# The p-value measures the strength of evidence against the null hypothesis.
# Cohen's d measures the magnitude of the difference between the groups.
#
# A statistically significant result indicates evidence that the population
# means differ, but it does not automatically mean that the difference is
# practically important.
#
# The business importance of the treatment should therefore be evaluated
# using both statistical significance and effect size.

# ---- Exercise 5 ----
from statsmodels.stats.power import TTestIndPower

analysis = TTestIndPower()

power = analysis.solve_power(
    effect_size=0.5,
    nobs1=50,
    alpha=0.05,
    ratio=1.0,
    alternative="two-sided"
)

print("Power:", power)

# ---- Exercise 6 ----

sample_sizes = [10, 20, 30, 50, 100, 200]

print("\nExercise 6")

for n in sample_sizes:
    power = analysis.solve_power(
        effect_size=0.5,
        nobs1=n,
        alpha=0.05,
        ratio=1.0,
        alternative="two-sided"
    )

    print("n =", n, "Power =", power)

# As sample size increases, statistical power generally increases.
# Larger samples reduce uncertainty and make it easier to detect
# a true effect of a given size.

# ---- Exercise 7 ----

effect_sizes = [0.2, 0.5, 0.8, 1.0]

print("\nExercise 7")

for effect_size in effect_sizes:
    power = analysis.solve_power(
        effect_size=effect_size,
        nobs1=50,
        alpha=0.05,
        ratio=1.0,
        alternative="two-sided"
    )

    print("Effect size =", effect_size, "Power =", power)

# Larger effects are easier to detect because the signal is larger
# relative to the random variation in the data.

# ---- Exercise 8 ----

required_n = analysis.solve_power(
    effect_size=0.5,
    power=0.80,
    alpha=0.05,
    ratio=1.0,
    alternative="two-sided"
)

required_n_rounded = int(np.ceil(required_n))

print("\nExercise 8")
print("Required sample size per group:", required_n)
print("Rounded sample size per group:", required_n_rounded)

# We round upward because rounding down could produce a sample size
# that provides less than the desired 80% statistical power.

# ---- Exercise 9 ----

def calculate_power(effect_size, sample_size, alpha=0.05):
    power = analysis.solve_power(
        effect_size=effect_size,
        nobs1=sample_size,
        alpha=alpha,
        ratio=1.0,
        alternative="two-sided"
    )

    return power


print("\nExercise 9")

for d in [0.2, 0.5, 0.8]:
    power = calculate_power(d, 50)
    print("Effect size:", d)
    print("Power:", power)

# ---- Exercise 10 ----

# Scenario:
# p-value = 0.003
# Cohen's d = 0.08
#
# The p-value is below 0.05, so there is statistically significant
# evidence of a difference between the groups.
#
# However, Cohen's d = 0.08 represents a very small effect.
#
# Therefore, statistical significance alone is not enough to recommend
# launching the treatment.
#
# The company should also consider:
# - Whether the improvement is practically meaningful
# - Financial impact of the improvement
# - Cost of implementation
# - Operational complexity
# - Sample size and study power
# - Whether the result is consistent across important customer segments
#
# A statistically significant effect can still be too small to matter
# economically.