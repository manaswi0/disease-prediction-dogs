import joblib

try:
    label_encoder = joblib.load('label_encoder.pkl')
    print("LabelEncoder loaded successfully:", label_encoder.classes_)
except Exception as e:
    print("Error loading LabelEncoder:", e)