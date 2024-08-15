from flask import Flask, request, render_template
import pickle
import pandas as pd

# Load the trained model and the OneHotEncoder
model = pickle.load(open('final_model2.pkl', 'rb'))
ohe = pickle.load(open('encoder.pkl', 'rb'))  # Load the OneHotEncoder used during training

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get the data from the form
    input_data = {
        'runs_left': int(request.form.get('runs_left', '0') or 0),
        'balls_left': int(request.form.get('balls_left', '0') or 0),
        'wickets_left': int(request.form.get('wickets_left', '0') or 0),
        'total_runs_x': int(request.form.get('total_runs', '0') or 0),
        'crr': float(request.form.get('crr', '0.0') or 0.0),
        'rrr': float(request.form.get('rrr', '0.0') or 0.0),
        'batting_team': request.form.get('batting_team', ''),
        'bowling_team': request.form.get('bowling_team', ''),
        'city': request.form.get('city', '')
    }

    print(input_data)  # Debugging step to check if data is being captured correctly

    # Convert the input data into a DataFrame
    input_df = pd.DataFrame([input_data])

    # Ensure the feature order matches the training data
    feature_order = model.feature_names_in_

    # One-hot encode categorical features
    ohe_features = ohe.transform(input_df[['batting_team', 'bowling_team', 'city']])
    ohe_df = pd.DataFrame(ohe_features, columns=ohe.get_feature_names_out())

    # Drop the original categorical columns and add the one-hot encoded columns
    input_df = input_df.drop(['batting_team', 'bowling_team', 'city'], axis=1)
    input_df = pd.concat([input_df, ohe_df], axis=1)

    # Ensure all expected features are present
    for feature in feature_order:
        if feature not in input_df.columns:
            input_df[feature] = 0  # Add missing features with a default value

    # Reorder columns to match model input
    input_df = input_df[feature_order]

    # Make the prediction
    prediction = model.predict(input_df)[0]
    result = "Win" if prediction else "Lose"
    winning_team = input_data['batting_team'] if prediction else input_data['bowling_team']

    # Return the prediction result
    return render_template('result.html', result=f"{winning_team} wins the match")

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8080)
