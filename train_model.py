import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import pickle
import os

# Create 'model' folder if it doesn't exist
if not os.path.exists('model'):
    os.makedirs('model')

# Load CSV
data = pd.read_csv("student_data.csv")

X = data[['hours','attendance','assignments','previous_marks']]
y = data['result']

# Split into training and testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = LogisticRegression()
model.fit(X_train, y_train)

# Save the model
with open('model/student_model.pkl', 'wb') as f:
    pickle.dump(model, f)

# Predict on test set
y_pred = model.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Model trained and saved successfully!")
print(f"Accuracy on test data: {accuracy*100:.2f}%")