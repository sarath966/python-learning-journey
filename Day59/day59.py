import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ------- Exericse 1 -------
df = pd.read_csv(r"C:\Users\asara\Desktop\Datascience_per\python_learning-journey\Day52\titanic.csv")
print(df["Age"].describe())
ages = df["Age"].dropna()
print(ages.mean())
print(ages.median())
print(ages.std())
print(ages.min())
print(ages.max())

# ------- Exericse 2 ------
plt.hist(ages, bins=10)
plt.xlabel("Age")
plt.ylabel("Number of Passengers")
plt.title("Distribution of Passenger Ages")
plt.show()

# Most passengers are concentrated around the younger adult ages.
# The distribution has a noticeable right tail, so it is not perfectly symmetric.
# ------- Exercise 3 ------
mean_age = ages.mean()
median_age = ages.median()

print("Mean:", mean_age)
print("Median:", median_age)

difference = mean_age - median_age
print("Difference:", difference)

# The mean and median are different, showing that the center of the distribution
# is not identical under the two measures. The histogram also helps us understand
# whether the difference is associated with the shape of the distribution.

# ------- Exercise 4 -------
population = np.random.normal(loc=50, scale=10, size=1000)

population_mean = np.mean(population)
population_std = np.std(population)

print(population_mean)
print(population_std)

sample = np.random.choice(population, size=50, replace=False)

sample_mean = np.mean(sample)
sample_std = np.std(sample)

print(sample_mean)
print(sample_std)

# The sample mean and standard deviation are not exactly the same as the
# population values because the sample contains only 50 randomly selected observations.

# -------- Exercise 5 ------
sample_means = []

for i in range(20):
    sample = np.random.choice(population, size=50, replace=False)
    sample_means.append(np.mean(sample))

print(sample_means)
print("Mean of sample means:", np.mean(sample_means))

# The individual sample means vary because each sample contains different
# randomly selected observations. The mean of the sample means is generally
# close to the population mean, but it is not expected to be exactly equal.
# ------ Exericse 6 -------
sample_means = np.array(sample_means)
print("Mean:", np.mean(sample_means))
print("Std:", np.std(sample_means))
plt.hist(sample_means, bins=8)
plt.xlabel("Sample Mean")
plt.ylabel("Frequency")
plt.title("Distribution of Sample Means")
plt.show()

# ------ Exercise 7 ------
sample_means = []

for i in range(1000):
    sample = np.random.choice(population, size=50, replace=False)
    sample_means.append(np.mean(sample))

sample_means = np.array(sample_means)

print("Population mean:", np.mean(population))
print("Mean of sample means:", np.mean(sample_means))
print("Std of sample means:", np.std(sample_means))

plt.hist(sample_means, bins=10)
plt.xlabel("Sample Mean")
plt.ylabel("Frequency")
plt.title("Distribution of Sample Means")
plt.show()

# The sample means form a distribution centered close to the population mean.
# Individual sample means vary because different random samples contain different
# observations. With many samples, the distribution of sample means becomes more
# stable and approximately bell-shaped, demonstrating the intuition behind the
# Central Limit Theorem.