import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn import metrics

# Sample data
data = {
    'Complaint Text': [
        'The library books are often overdue.',
        'The computer lab equipment is outdated.',
        'There are issues with the air conditioning.',
        'The email server is down frequently.'
    ],
    'Department': ['Library', 'IT Support', 'Facilities', 'IT Support']
}

df = pd.DataFrame(data)

# Preprocess and split data
X = df['Complaint Text']
y = df['Department']

vectorizer = TfidfVectorizer()
X_transformed = vectorizer.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X_transformed, y, test_size=0.3, random_state=42)

# Train the model
model = MultinomialNB()
model.fit(X_train, y_train)

# Predict and evaluate
y_pred = model.predict(X_test)
print(metrics.classification_report(y_test, y_pred))
