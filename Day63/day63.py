import numpy as np
from scipy.stats import ttest_ind

# ---- Exercise 1 ----
np.random.seed(42)

group_a = np.random.normal(
    loc=500,
    scale=50,
    size=50
)

group_b = np.random.normal(
    loc=530,
    scale=50,
    size=50
)
print(group_a.mean())
print(group_b.mean())
print(group_a.std(ddof=1))
print(group_b.std(ddof=1))
print(group_a.size)
print(group_b.size)

# ---- Exercise 2 ----
# H0: The population means of Group A and Group B are equal.
# H1: The population means of Group A and Group B are different.
# Test type: Two-sided independent two-sample t-test

# ---- Exercise 3 ----
t_stat, p_value = ttest_ind(
    group_a,
    group_b,
    equal_var=False
)
print(t_stat)
print(p_value)
alpha = 0.05
if p_value <= alpha:
    print("Reject H0")
else:
    print("Fail to reject H0")

# ---- Exercise 4 ----

# The control and treatment groups have different sample means.
# The Welch independent two-sample t-test compares these means while
# allowing the two groups to have different population variances.
# If p-value <= 0.05, we reject H0 and conclude that there is
# sufficient statistical evidence that the population means differ.
# If p-value > 0.05, we fail to reject H0 and conclude that there
# is insufficient statistical evidence that the population means differ.

mean_difference = group_b.mean() - group_a.mean()

print("Mean difference:", mean_difference)

# ---- Exercise 5 ----
t_stat_greater, p_greater = ttest_ind(
    group_a,
    group_b,
    equal_var=False,
    alternative="less"
)
print("\nExercise 5")
print("t-statistic:", t_stat_greater)
print("p-value:", p_greater)

if p_greater <= 0.05:
    print("Evidence that Group B has a higher mean than Group A")
else:
    print("Insufficient evidence that Group B has a higher mean than Group A")

# The two-sided and one-sided p-values differ because the one-sided
# test considers evidence in only one specified direction, while the
# two-sided test considers differences in both directions.

# ---- Exercise 6 ----
t_equal, p_equal = ttest_ind(
    group_a,
    group_b,
    equal_var=True
)
print(t_equal)
print(p_equal)

t_welch, p_welch = ttest_ind(
    group_a,
    group_b,
    equal_var=False
)

# ---- Exercise 7 ----
np.random.seed(100)

group_a = np.random.normal(
    loc=500,
    scale=20,
    size=50
)

group_b = np.random.normal(
    loc=530,
    scale=100,
    size=50
)
print("\nExercise 7")

print("Group A mean:", group_a.mean())
print("Group B mean:", group_b.mean())
print("Group A standard deviation:", group_a.std(ddof=1))
print("Group B standard deviation:", group_b.std(ddof=1))

t_stat, p_value = ttest_ind(
    group_a,
    group_b,
    equal_var=False
)

print("Welch t-statistic:", t_stat)
print("Welch p-value:", p_value)

if p_value <= 0.05:
    print("Reject H0")
else:
    print("Fail to reject H0")

# Welch's t-test is particularly relevant here because Group A and
# Group B have very different levels of variability.

# ---- Exercise 8 ----
np.random.seed(123)

sample_sizes = [10, 30, 50, 100, 300]

for n in sample_sizes:

    group_a = np.random.normal(
        loc=500,
        scale=50,
        size=n
    )

    group_b = np.random.normal(
        loc=515,
        scale=50,
        size=n
    )

    t_stat, p_value = ttest_ind(
        group_a,
        group_b,
        equal_var=False
    )

    print(
        n,
        np.mean(group_a),
        np.mean(group_b),
        t_stat,
        p_value
    )


# ---- Exercise 9 ----

def independent_t_test(group_a, group_b, alpha=0.05):

    mean_a = np.mean(group_a)
    mean_b = np.mean(group_b)

    std_a = np.std(group_a, ddof=1)
    std_b = np.std(group_b, ddof=1)

    difference = mean_b - mean_a

    t_stat, p_value = ttest_ind(
        group_a,
        group_b,
        equal_var=False
    )

    if p_value <= alpha:
        decision = "Reject H0"
    else:
        decision = "Fail to reject H0"

    return {
        "mean_a": mean_a,
        "mean_b": mean_b,
        "std_a": std_a,
        "std_b": std_b,
        "difference": difference,
        "t_statistic": t_stat,
        "p_value": p_value,
        "decision": decision
    }


result = independent_t_test(group_a, group_b)

print("\nExercise 9")

for key, value in result.items():
    print(f"{key}: {value}")

