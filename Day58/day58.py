import numpy as np
import pandas as pd

# ------------ Exercise 1 -----------
values = [100, 50, 0]
probabilities = [0.20, 0.30, 0.50]

expected_value = sum(v * p for v, p in zip(values, probabilities))

print(expected_value)

# When the game is played many times, the expected value
# represents the average outcome over the long run.

# ------------ Exercise 2 -----------
data = pd.read_csv(r"C:\Users\asara\Desktop\Datascience_per\python_learning-journey\Day52\titanic.csv")
survived = len(data[data["Survived"] == 1])
p_survived = survived / len(data["Survived"])
print(p_survived)

survived_female = len(data[(data["Survived"] == 1) & (data["Sex"] == "female")])
p_survived_female = survived_female / len(data[data["Sex"] == "female"])
print(p_survived_female)

survived_male = len(data[(data["Survived"] == 1) & (data["Sex"] == "male")])
p_survived_male = survived_male / len(data[data["Sex"] == "male"])

print(p_survived_male)
# ------------ Exercise 3 ------------
results = []

for pclass in [1, 2, 3]:
    group = data[data["Pclass"] == pclass]
    probability = group["Survived"].mean()

    results.append({
        "Pclass": pclass,
        "Survival_Probability": probability
    })

survival_by_class = pd.DataFrame(results)

print(survival_by_class)

# ----------- Exercise 4 ----------
p_a = 0.4
p_b = 0.5
prob_a_and_b = p_a * p_b
prob_a_or_b = p_a + p_b - (prob_a_and_b)
print(prob_a_and_b)
print(prob_a_or_b)