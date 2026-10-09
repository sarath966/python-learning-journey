import numpy as np
import pandas as pd

np.random.seed(42)

n = 1000

visits = np.random.randint(1, 11, n)
time_on_site = np.random.uniform(1, 20, n)

# Create a probability of purchase for each customer.
logit = -3 + 0.25 * visits + 0.12 * time_on_site
probability = 1 / (1 + np.exp(-logit))

purchased = np.random.binomial(1, probability)

df = pd.DataFrame({
    "visits": visits,
    "time_on_site": time_on_site,
    "purchased": purchased
})

print(df.head())
print(df.info())
print(df["purchased"].value_counts())
print(df["purchased"].mean())

X = df[["visits", "time_on_site"]]
y = df["purchased"]

print("Features shape:", X.shape)
print("Target shape:", y.shape)

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

print("Training rows:", len(X_train))
print("Testing rows:", len(X_test))

from sklearn.linear_model import LogisticRegression

model = LogisticRegression()

model.fit(X_train, y_train)

print("Coefficients:", model.coef_)
print("Intercept:", model.intercept_)


y_pred = model.predict(X_test)
y_prob = model.predict_proba(X_test)[:, 1]

print("Predicted classes:", y_pred[:10])
print("Predicted probabilities:", y_prob[:10])

from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report
)

print("Accuracy:", accuracy_score(y_test, y_pred))
print("Confusion matrix:")
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))

threshold = 0.70

y_pred_strict = (y_prob >= threshold).astype(int)

print("Default-threshold accuracy:", accuracy_score(y_test, y_pred))
print(
    "Strict-threshold accuracy:",
    accuracy_score(y_test, y_pred_strict)
)

print("Strict-threshold confusion matrix:")
print(confusion_matrix(y_test, y_pred_strict))

results = X_test.copy()

results["actual"] = y_test
results["predicted"] = y_pred
results["purchase_probability"] = y_prob

print(results.head(15))

# ---- Exercise ----

def train_purchase_model(df):
    X = df[["visits", "time_on_site"]]
    y = df["purchased"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )

    model = LogisticRegression()
    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    return model, X_test, y_test, predictions


model, X_test, y_test, predictions = train_purchase_model(df)

print("\nExercise 9")
print("Accuracy:", accuracy_score(y_test, predictions))
print(classification_report(y_test, predictions))

# ---- Business Interpretation ----

# 1. Compare the model's test accuracy with a majority-class baseline.
# Accuracy alone is not enough; compare precision, recall, and F1 too.

# 2. For a marketing campaign, precision may matter more if contacting
# unlikely buyers is expensive. Recall may matter more if the goal is
# to reach as many potential buyers as possible.

# 3. A false positive can waste marketing costs and annoy a customer
# who was unlikely to purchase.

# 4. Additional features could include purchase history, device type,
# traffic source, discount exposure, and customer tenure.