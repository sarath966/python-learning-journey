import numpy as np

# ---- Exercise 1 ----

np.random.seed(42)

n_control = 1000
n_treatment = 1000

control = np.random.binomial(1, 0.10, n_control)
treatment = np.random.binomial(1, 0.12, n_treatment)

control_rate = control.mean()
treatment_rate = treatment.mean()

print("Control conversion rate:", control_rate)
print("Treatment conversion rate:", treatment_rate)

# ---- Exercise 2 ----
absolute_difference = treatment_rate - control_rate
relative_lift = absolute_difference / control_rate

print("Absolute difference:", absolute_difference)
print("Relative lift:", relative_lift)
print("Relative lift (%):", relative_lift * 100)

# ---- Exercise 3 ----

# Scenario:
# A company launches a new recommendation algorithm and wants to know
# whether it increases click-through rate.

# H0: Treatment click-through rate <= Control click-through rate
# H1: Treatment click-through rate > Control click-through rate
# Test direction: One-sided

# ---- Exercise 4 ----
from statsmodels.stats.proportion import proportions_ztest

successes = np.array([
    control.sum(),
    treatment.sum()
])

samples = np.array([
    len(control),
    len(treatment)
])

z_stat, p_value = proportions_ztest(
    successes,
    samples,
    alternative="two-sided"
)

print("Z-statistic:", z_stat)
print("P-value:", p_value)

alpha = 0.05

if p_value <= alpha:
    print("Reject H0")
else:
    print("Fail to reject H0")

# ---- Exercise 5 ----
z_stat_one, p_value_one = proportions_ztest(
    successes,
    samples,
    alternative="smaller"
)

print("One-sided z-statistic:", z_stat_one)
print("One-sided p-value:", p_value_one)

if p_value_one <= alpha:
    print("Evidence that treatment conversion rate is higher than control")
else:
    print("Insufficient evidence that treatment conversion rate is higher than control")

# The one-sided test focuses specifically on whether treatment
# performs better than control.

# ---- Exercise 6 ----
from statsmodels.stats.proportion import confint_proportions_2indep

ci_low, ci_high = confint_proportions_2indep(
    count1=control.sum(),
    nobs1=len(control),
    count2=treatment.sum(),
    nobs2=len(treatment),
    method="wald"
)

print("95% CI for difference:", ci_low, ci_high)

# ---- Exercise 7 ----

sample_sizes = [100, 500, 1000, 5000, 10000]

for n in sample_sizes:

    control_test = np.random.binomial(1, 0.10, n)
    treatment_test = np.random.binomial(1, 0.12, n)

    successes_test = np.array([
        control_test.sum(),
        treatment_test.sum()
    ])

    samples_test = np.array([
        len(control_test),
        len(treatment_test)
    ])

    z_stat_test, p_value_test = proportions_ztest(
        successes_test,
        samples_test,
        alternative="two-sided"
    )

    if p_value_test <= alpha:
        decision = "Reject H0"
    else:
        decision = "Fail to reject H0"

    print("\nSample size:", n)
    print("Control rate:", control_test.mean())
    print("Treatment rate:", treatment_test.mean())
    print("Difference:", treatment_test.mean() - control_test.mean())
    print("P-value:", p_value_test)
    print("Decision:", decision)
# As sample size increases, estimates generally become more precise
# and the test has greater ability to detect a real difference.
# Therefore, statistical power generally increases with sample size.

# ---- Exercise 8 ----

# Results from six metrics:
#
# Conversion rate:      p = 0.42
# Revenue per user:     p = 0.31
# Average order value:  p = 0.008
# Click-through rate:   p = 0.03
# Session duration:     p = 0.51
# Bounce rate:          p = 0.04

# Statistically significant at alpha = 0.05:
# Average order value
# Click-through rate
# Bounce rate
#
# Testing many metrics increases the chance of obtaining a statistically
# significant result simply by chance.
#
# Therefore, the primary metric should be defined before the experiment.
#
# Multiple testing procedures such as Bonferroni correction can help
# control the overall false-positive rate.

# ---- Exercise 9 ----

def analyze_ab_test(control, treatment, alpha=0.05):

    control_rate = np.mean(control)
    treatment_rate = np.mean(treatment)

    absolute_difference = treatment_rate - control_rate
    relative_lift = absolute_difference / control_rate

    successes = np.array([
        control.sum(),
        treatment.sum()
    ])

    samples = np.array([
        len(control),
        len(treatment)
    ])

    z_statistic, p_value = proportions_ztest(
        successes,
        samples,
        alternative="two-sided"
    )

    if p_value <= alpha:
        decision = "Reject H0"
    else:
        decision = "Fail to reject H0"

    return {
        "control_rate": control_rate,
        "treatment_rate": treatment_rate,
        "absolute_difference": absolute_difference,
        "relative_lift": relative_lift,
        "z_statistic": z_statistic,
        "p_value": p_value,
        "decision": decision
    }


result = analyze_ab_test(control, treatment)

print("\nExercise 9")
for key, value in result.items():
    print(f"{key}: {value}")

# ---- Mini Challenge ----

np.random.seed(2026)

n_control = 50000
n_treatment = 50000

control = np.random.binomial(1, 0.082, n_control)
treatment = np.random.binomial(1, 0.087, n_treatment)

control_rate = control.mean()
treatment_rate = treatment.mean()

absolute_difference = treatment_rate - control_rate
relative_lift = absolute_difference / control_rate

successes = np.array([
    control.sum(),
    treatment.sum()
])

samples = np.array([
    len(control),
    len(treatment)
])

z_stat, p_value = proportions_ztest(
    successes,
    samples,
    alternative="two-sided"
)

ci_low, ci_high = confint_proportions_2indep(
    count1=control.sum(),
    nobs1=len(control),
    count2=treatment.sum(),
    nobs2=len(treatment),
    method="wald"
)

alpha = 0.05

if p_value <= alpha:
    decision = "Reject H0"
else:
    decision = "Fail to reject H0"

additional_conversions = (
    treatment_rate - control_rate
) * n_treatment

additional_profit = additional_conversions * 800

print("\nMini Challenge")
print("Control conversion rate:", control_rate)
print("Treatment conversion rate:", treatment_rate)
print("Absolute difference:", absolute_difference)
print("Relative lift:", relative_lift)
print("Relative lift (%):", relative_lift * 100)
print("Z-statistic:", z_stat)
print("P-value:", p_value)
print("95% CI:", ci_low, ci_high)
print("Decision:", decision)
print("Estimated additional conversions:", additional_conversions)
print("Estimated additional profit: ₹", additional_profit)

# Business interpretation:
# The treatment should be evaluated using statistical evidence,
# effect size, uncertainty, and expected financial impact together.