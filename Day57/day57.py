import numpy as np
import pandas as pd

# --------- Exercise 1 ----------
sample_space = [1,2,3,4,5,6]
prob_4 =  sample_space.count(4) / len(sample_space)

# Probability of rolling an even number
even_numbers = [x for x in sample_space if x % 2 == 0]
p_even = len(even_numbers) / len(sample_space)

# Probability of rolling a number greater than 4
greater_than_4 = [x for x in sample_space if x > 4]
p_greater_4 = len(greater_than_4) / len(sample_space)

# Probability of rolling an odd number
odd_numbers = [x for x in sample_space if x % 2 != 0]
p_odd = len(odd_numbers) / len(sample_space)

print("Sample space:", sample_space)
print("P(4):", prob_4)
print("P(Even):", p_even)
print("P(>4):", p_greater_4)
print("P(Odd):", p_odd)

# ---------- Exercise 2 ----------
rolls = np.random.randint(1,7, size=10000)
count_6= len([x for x in rolls if x == 6])
p_6 = count_6 / len(rolls)
print(p_6)

count_even = len([x for x in rolls if x % 2 == 0])

p_even = count_even / len(rolls)

print(p_even)

count_greater_4 = len([x for x in rolls if x > 4])

p_greater_4 = count_greater_4 / len(rolls)

print(p_greater_4)

# ---------- Exercise 3 ----------
data = pd.DataFrame({
    "Student": ["A","B","C","D","E","F","G","H"],
    "Studied": ["Yes","Yes","No","Yes","No","Yes","No","Yes"],
    "Passed": ["Yes","Yes","No","No","No","Yes","No","Yes"]
})

passed = data[data["Passed"] == "Yes"]
prob_passed = len(passed) / len(data["Passed"])
print(prob_passed)

studied = data[data["Studied"] == "Yes"]
prob_studied = len(studied) / len(data["Studied"])
print(prob_studied)

passed_and_studied = studied[studied["Passed"] == "Yes"]

prob_passed_given_studied = len(passed_and_studied) / len(studied)

print(prob_passed_given_studied)

# ---------- Exercise 4 ----------

p_passed = (data["Passed"] == "Yes").mean()

studied = data[data["Studied"] == "Yes"]
passed_and_studied = studied[studied["Passed"] == "Yes"]

p_passed_given_studied = len(passed_and_studied) / len(studied)

print("P(Passed):", p_passed)
print("P(Passed | Studied):", p_passed_given_studied)

"""
P(Passed) is the probability that a randomly selected student passed,
considering all students.
P(Passed | Studied) is the probability of passing among only the students
who studied. The two probabilities can be different.
"""

# ---------- Exercise 5 ----------

p_passed = (data["Passed"] == "Yes").mean()

studied = data[data["Studied"] == "Yes"]
passed_and_studied = studied[studied["Passed"] == "Yes"]

p_passed_given_studied = len(passed_and_studied) / len(studied)

print("P(Passed):", p_passed)
print("P(Passed | Studied):", p_passed_given_studied)

if np.isclose(p_passed, p_passed_given_studied):
    print("The events appear independent in this dataset.")
else:
    print("The events appear dependent in this dataset.")

