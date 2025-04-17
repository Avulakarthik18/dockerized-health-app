import os
import pickle
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# Ensure model directory exists
os.makedirs("app/models", exist_ok=True)

# Load Parkinson's disease dataset
df = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/parkinsons/parkinsons.data")

# Preprocess
X = df.drop(['name', 'status'], axis=1)
y = df['status']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Save model
with open("app/models/parkinsons.pkl", "wb") as f:
    pickle.dump(model, f)
