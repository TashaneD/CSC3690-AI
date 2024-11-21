import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# use pandas library to read csv
data = pd.read_csv('cleaned_merged_heart_dataset.csv')

# Display the dataset
print(data.head())

# Split the dataset
X = data.drop(columns=['cp'])  # Columns = is the target to predict
y = data['cp']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Train the Decision Tree Model
model = DecisionTreeClassifier(criterion='entropy')
model.fit(X_train, y_train)

# Predict using the model
predictions = model.predict(X_test)

# Calculate Accuracy using sklearn metrics
accuracy = accuracy_score(y_test, predictions)
print(f"Model Accuracy: {accuracy * 100:.2f}%")
