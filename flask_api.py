from flask import Flask, request, jsonify
import pickle

# Load the vectorizer and model
with open('vectorizer.pkl', 'rb') as f:
    vectorizer = pickle.load(f)

with open('model.pkl', 'rb') as f:
    clf = pickle.load(f)

# Initialize Flask application
app = Flask(__name__)

# Function to classify new complaints
def classify_complaint(complaint):
    complaint_vec = vectorizer.transform([complaint])
    department = clf.predict(complaint_vec)
    return department[0]

# Define API route
@app.route('/classify', methods=['POST'])
def classify():
    # Get complaint from POST request
    data = request.get_json()
    complaint = data.get('complaint')
    
    if not complaint:
        return jsonify({'error': 'No complaint provided'}), 400
    
    # Classify the complaint
    department = classify_complaint(complaint)
    
    # Return the classification result
    return jsonify({'department': department})

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
