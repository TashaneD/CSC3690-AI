import pandas as pd
import math

# Data used for training
data = pd.DataFrame({
    'Toothed': ['Toothed', 'Not Toothed', 'Toothed', 'Not Toothed', 'Toothed'],
    'Hair': ['Hair', 'Hair', 'No Hair', 'No Hair', 'Hair'],
    'Breathes': ['Breathes', 'Breathes', 'not Breathes', 'Breathes', 'not Breathes'],
    'Legs': ['legs', 'no legs', 'legs', 'no legs', 'legs'],
    'Species': ['Mammal', 'Reptile', 'Reptile', 'Mammal', 'Mammal']
})

# Calculate entropy
def calculate_entropy(data):
    counts = data.value_counts()  # Counts each unique value
    total = len(data)  # Total number of samples
    entropy = 0.0

    # Loops through each unique value and its count to calculate entropy
    for count in counts:
        probability = count / total
        entropy -= probability * math.log2(probability) if probability > 0 else 0


    return entropy


# Calculate information gain
def calculate_information_gain(data, attribute, target_name="Species"):
    # Calculate entropy of the target
    total_entropy = calculate_entropy(data[target_name])

    # Calculate weighted entropy after splitting by the attribute
    values = data[attribute].unique()  # Unique values of the attribute
    weighted_entropy = 0.0

    for value in values:
        subset = data[data[attribute] == value]
        weight = len(subset) / len(data)
        entropy_of_subset = calculate_entropy(subset[target_name])
        weighted_entropy += weight * entropy_of_subset

    # The reduction in entropy id the information gain
    info_gain = total_entropy - weighted_entropy
    return info_gain


# Algorithm in order to build a decision tree
def build_tree(data, features, target_name="Species"):
    target_values = data[target_name].unique()

    # Base cases
    if len(target_values) == 1:
        return target_values[0]  # If only one class, return it

    if len(features) == 0:
        return data[target_name].mode()[0]  # Return most common class if no features left

    # Find the best feature by information gain
    best_feature = None
    best_gain = 0
    for feature in features:
        gain = calculate_information_gain(data, feature, target_name)
        if gain > best_gain:
            best_gain = gain
            best_feature = feature

    # Create the tree node with the best feature
    tree = {best_feature: {}}

    # Split the data and build subtrees for each value of the best feature
    remaining_features = [f for f in features if f != best_feature]
    for value in data[best_feature].unique():
        subset = data[data[best_feature] == value]
        tree[best_feature][value] = build_tree(subset, remaining_features, target_name)

    return tree


# Runs the algorithm
features = list(data.columns[:-1])
tree = build_tree(data, features)
print("Decision Tree:", tree)


# Prediction
def predict(query, tree):
    for attribute, subtree in tree.items():
        value = query.get(attribute)
        if value in subtree:
            result = subtree[value]
            if isinstance(result, dict):
                return predict(query, result)  # Recursively predict if result is a subtree
            else:
                return result  # Final predicted class
        else:
            return "Unknown"  # If value is not in the subtree, return unknown

query = {'Toothed': 'Toothed', 'Hair': 'Hair', 'Breathes': 'not Breathes', 'Legs': 'legs'}
prediction = predict(query, tree)
print("Predicted species:", prediction)
