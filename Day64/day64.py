import numpy as np
from scipy.stats import ttest_rel

# ---- Exercise 1 ----
np.random.seed(42)

before = np.random.normal(loc=70, scale=8, size=40)
after = before + np.random.normal(loc=4, scale=5, size=40)

print(before.mean())
print(after.mean())
print(before.std(ddof=1))
print(after.std(ddof=1))

# ---- Exercise 2 ----
# H0: The population mean productivity before and after training is equal.
# H1: The population mean productivity before and after training is different.
# Test type: Two-sided paired t-test

# ---- Exercise 3 ----
t_stat, p_value = ttest_rel(before, after)
print(t_stat)
print(p_value)
alpha = 0.05
if p_value < alpha:
    print("Reject H0")
else:
    print("Fail to reject H0")

# ---- Exercise 4 ----
differences = after - before
print(differences.mean())
print(differences.std())
print(differences.max())
print(differences.min())

# ---- Exercise 5 ----
for i in range(5):
    print(before[i], after[i], differences[i])

# ---- Exercise 6 ----
# H0: The population mean productivity after training is equal to before training.
# H1: The population mean productivity after training is greater than before training.

t_stat_greater, p_value_greater = ttest_rel(
    before,
    after,
    alternative="less"
)

print("\nExercise 6")
print("t-statistic:", t_stat_greater)
print("p-value:", p_value_greater)

if p_value_greater <= 0.05:
    print("Reject H0")
    print("Sufficient evidence that training increased productivity")
else:
    print("Fail to reject H0")
    print("Insufficient evidence that training increased productivity")

# ---- Exercise 7 ----
t_two_sided, p_two_sided = ttest_rel(before, after)

t_one_sided, p_one_sided = ttest_rel(
    before,
    after,
    alternative="less"
)

print("\nExercise 7")
print("Two-sided p-value:", p_two_sided)
print("One-sided p-value:", p_one_sided)

# The two-sided test considers evidence for a difference in either
# direction, while the one-sided test considers evidence in one
# specified direction only.

# ---- Exercise 8 ----

# Scenario A:
# 50 customers use Website A and another 50 different customers use Website B.
# Test: Independent two-sample t-test
# Reason: The observations come from different, independent customers.

# Scenario B:
# The same 50 customers use the old website and then the redesigned website.
# Test: Paired t-test
# Reason: Each customer's old and new measurements are naturally matched.

# Scenario C:
# The same patients have blood pressure measured before and after treatment.
# Test: Paired t-test
# Reason: Each patient's before and after measurements are paired.

# Scenario D:
# Two unrelated groups of employees are compared.
# Test: Independent two-sample t-test
# Reason: The observations belong to separate independent groups.

# ---- Exercise 9 ----
def paired_t_test(before, after, alpha=0.05):
    mean_before = np.mean(before)
    mean_after = np.mean(after)
    mean_difference = np.mean(after - before)

    t_stat, p_value = ttest_rel(before, after)

    if p_value <= alpha:
        decision = "Reject H0"
    else:
        decision = "Fail to reject H0"

    return {
        "mean_before": mean_before,
        "mean_after": mean_after,
        "mean_difference": mean_difference,
        "t_statistic": t_stat,
        "p_value": p_value,
        "decision": decision
    }

result = paired_t_test(before, after)

print("\nExercise 9")
for key, value in result.items():
    print(f"{key}: {value}")