import pickle
import pandas as pd

# Load the trained model
with open("forex_model.pkl", "rb") as f:
    model = pickle.load(f)

# Example input (ensure it has only the features used in training)
example_input = pd.DataFrame({
    "Exchange Rate": [0.9216]  # Use actual test values
})

# Predict
prediction = model.predict(example_input)
print("Predicted exchange rate:", prediction[0])

