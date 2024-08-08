import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import accuracy_score, classification_report
import pickle

# Load the dataset
data = pd.read_csv('y.csv', encoding='ISO-8859-1')

# Vectorize the complaint text
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(data['Complin'])

# Target variable
y = data['Department']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the decision tree classifier
clf = DecisionTreeClassifier()

# Train the model
clf.fit(X_train, y_train)

# Make predictions on the test set
y_pred = clf.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred)

print(f'Accuracy: {accuracy}')
print(f'Classification Report:\n{report}')

# Function to classify new complaints
def classify_complaint(complaint):  
    complaint_vec = vectorizer.transform([complaint])
    department = clf.predict(complaint_vec)
    return department[0]

# Example usage

new_complaint = "The internet is not working in my room"
print(f'The complaint should go to the {classify_complaint(new_complaint)} department')

new_complaint1 = "WE DON'T HAVE ENOUGH BOOK"
print(f'The complaint should go to the {classify_complaint(new_complaint1)} department')

# 1) Model save (pickle)
# 2) Vectorizer save (pickle)


# Save the CountVectorizer and model using pickle
with open('vectorizer.pkl', 'wb') as f:
    pickle.dump(vectorizer, f)

with open('model.pkl', 'wb') as f:
    pickle.dump(clf, f)