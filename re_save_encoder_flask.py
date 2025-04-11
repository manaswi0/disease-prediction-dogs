import joblib
from sklearn.preprocessing import LabelEncoder
import pandas as pd

# --- VERY IMPORTANT: CHANGE THESE LINES TO MATCH YOUR FILES! ---
training_data_file = 'C:/Users/Manaswi/Desktop/cep/dogfinal3.csv'  # Replace 'your_training_data.csv' with the actual name of your file
disease_column = 'diseases'  # Replace 'diseases' with the actual name of the column with disease names
output_file = 'label_encoder.pkl' # This will update your existing label encoder file
# --- DO NOT CHANGE ANYTHING BELOW THIS LINE UNLESS YOU KNOW WHAT YOU'RE DOING ---

try:
    # Load your training data
    data = pd.read_csv(training_data_file)
    # Get the column with the disease names
    disease_labels = data[disease_column]
except FileNotFoundError:
    print(f"Error: Training data file '{training_data_file}' not found. Make sure the path is correct.")
    exit()
except KeyError:
    print(f"Error: Column '{disease_column}' not found in the training data. Check the column name.")
    exit()

# Create a new LabelEncoder
le = LabelEncoder()
# Train the LabelEncoder on your disease names
le.fit(disease_labels)

# Save the *newly trained* LabelEncoder to the same file
joblib.dump(le, output_file)

print(f"Successfully updated the label encoder in '{output_file}'.")