import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import joblib
import os

# Load dataset from the same directory
base_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(base_dir, "hdi.csv")

if not os.path.exists(csv_path):
    # Try copying from original path if not present yet
    import shutil
    orig_path = os.path.join(base_dir, "..", "4. Project Planning Phase", "hdi.csv")
    if os.path.exists(orig_path):
        shutil.copy(orig_path, csv_path)
        print("Copied hdi.csv from original folder.")
    else:
        raise FileNotFoundError(f"Could not find hdi.csv at {csv_path} or {orig_path}")

df = pd.read_csv(csv_path)

# Select required columns
df = df[[
    'Life Expectancy at Birth (2021)',
    'Expected Years of Schooling (2021)',
    'Mean Years of Schooling (2021)',
    'Gross National Income Per Capita (2021)',
    'Human Development Index (2021)'
]]

# Remove rows with missing values
df.dropna(inplace=True)

print(df.head())
print("\nDataset Shape:", df.shape)

# Features
X = df[[
    'Life Expectancy at Birth (2021)',
    'Expected Years of Schooling (2021)',
    'Mean Years of Schooling (2021)',
    'Gross National Income Per Capita (2021)'
]]

# Target
y = df['Human Development Index (2021)']

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("Training data:", X_train.shape)
print("Testing data:", X_test.shape)

# Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Calculate accuracy
score = r2_score(y_test, y_pred)
print("R2 Score:", score)

# Save the trained model in the same folder
model_path = os.path.join(base_dir, "model.pkl")
joblib.dump(model, model_path)
print(f"Model saved successfully to {model_path}!")
