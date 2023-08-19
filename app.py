# app.py

from flask import Flask, render_template, request, jsonify
from joblib import load

app = Flask(__name__)

# Load the model
model = load('models/model_filename1.pkl')


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    # Get data from the form
    features = [float(x) for x in request.form.values()]

    # Predict the sale price
    prediction = model.predict([features])[0]

    return render_template('index.html', prediction_text=f'The House Price is : ${prediction:,.2f}')


if __name__ == '__main__':
    app.run()



