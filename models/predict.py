

import pickle
import pandas as pd

with open("model.pkl", "rb") as f:
    model = pickle.load(f)

MODEL_version = "1.0.0"

def predict_output(user_input):

    input_df = pd.DataFrame([user_input])

    print("\nInput DataFrame:")
    print(input_df)
    print("\nColumns:")
    print(input_df.columns.tolist())
    prediction = model.predict(input_df)[0]
    return prediction
