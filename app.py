from flask import Flask, render_template, request, redirect, url_for, session
import numpy as np
from pymongo import MongoClient
#import flash
import joblib
import os

app = Flask(__name__)
app.secret_key = 'supersecretkey'

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["petHealthDB"]
users_collection = db["users"]

# Dummy user storage (in-memory dictionary)
users = {
        "manaswi@example.com": {
        "username": "Manaswi Shinde",
        "password": "your_password"  # replace with your actual password
    }
}

# Load model
model_path = 'dog_disease_model.pkl'
if not os.path.exists(model_path):
    raise FileNotFoundError(f"Model not found at {model_path}")
model = joblib.load(model_path)

# Load the LabelEncoder
label_encoder = joblib.load('label_encoder.pkl')

encoded_classes = label_encoder.classes_
print("Encoded Classes:", encoded_classes)

# Your disease_mapping should now align with this order
disease_mapping = {i: label for i, label in enumerate(encoded_classes)}
print("Corrected Disease Mapping:", disease_mapping)


@app.route('/')
def home():
    return render_template('index.html')  # Optional home page

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = users.get(email)  

        if user and user['password'] == password:
            session['email'] = email
            session['username'] = user['username']
            return redirect(url_for('profile')) 
        
            return "Invalid credentials!"

    return render_template('sign_in.html')


@app.route('/test')
def test():
    return render_template('sign_in.html')


@app.route('/profile', methods=['GET', 'POST'])
def profile():
    if 'email' not in session:
        return redirect(url_for('login'))

    if request.method == 'POST':
        session['pet_name'] = request.form.get('pet_name')
        session['pet_breed'] = request.form.get('pet_breed')
        session['pet_age'] = request.form.get('pet_age')
        return redirect(url_for('health'))  

    return render_template('profilee.html',
                           username=session['username'],
                           email=session['email'],
                           pet_name=session.get('pet_name'),
                           pet_breed=session.get('pet_breed'),
                           pet_age=session.get('pet_age'))


@app.route('/health', methods=['GET', 'POST'])
def health():
    if request.method == 'POST':
        past_diseases = request.form.get('past_diseases')
        medications = request.form.get('medications')
        allergies = request.form.get('allergies')

        # Optional: store these in session if needed
        session['past_diseases'] = past_diseases
        session['medications'] = medications
        session['allergies'] = allergies

        return redirect(url_for('form'))  # Go to next form

    return render_template('health.html')



@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        symptoms = [
            request.form.get('paralysis') == 'true',
            request.form.get('discharge_eyes') == 'true',
            request.form.get('keratosis') == 'true',
            request.form.get('dehydration') == 'true',
            request.form.get('sneezing') == 'true',
            request.form.get('gagging') == 'true',
            request.form.get('salivation') == 'true',
            request.form.get('foaming') == 'true',
            request.form.get('pica') == 'true',
            request.form.get('jaundice') == 'true',
            request.form.get('gums') == 'true',
            request.form.get('ulcers') == 'true'
        ]
        input_array = np.array([symptoms]).astype(int)
        prediction = model.predict(input_array)[0]
        disease = disease_mapping.get(prediction, "Unknown Disease")
        return redirect(url_for('result', disease=disease))

    return render_template('form.html')


@app.route('/predict', methods=['POST'])
def predict():

    # Symptoms (you may have more or fewer depending on your model)
    symptom_names = [
        'paralysis', 'discharge_eyes', 'keratosis', 'dehydration', 'sneezing',
        'gagging', 'salivation', 'foaming', 'pica', 'jaundice', 'gums', 'ulcers'
    ]
    symptom_values = [1 if request.form.get(symptom) == 'true' else 0 for symptom in symptom_names]

    # Convert to 2D array as expected by sklearn models
    input_array = np.array([symptom_values]).astype(int)

    # Predict
    prediction = model.predict(input_array)[0]  # e.g., "Canine Distemper", or a class index
    predicted_disease_name = label_encoder.inverse_transform([prediction])[0]
    print("Predicted Numerical Label:", prediction)
    print("Predicted Disease Name:", predicted_disease_name)

    return render_template('result.html', disease=predicted_disease_name)

if __name__ == '__main__':
    app.run(debug=True)
