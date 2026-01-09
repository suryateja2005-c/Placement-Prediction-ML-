# ============================================================
# STUDENT PLACEMENT PREDICTION - FLASK APPLICATION
# ============================================================

import numpy as np
import pandas as pd
from flask import Flask, request, render_template
import joblib
import os

# Initialize Flask app
app = Flask(__name__)

# ============================================================
# LOAD MODEL
# ============================================================
try:
    # Load the model from current directory
    model = joblib.load('logistic_regression_model (1).joblib')
    print("✓ Model loaded successfully!")
    print(f"✓ Model expects {model.n_features_in_} features")
except FileNotFoundError:
    print("✗ Error: Model file not found!")
    print(f"✗ Looking in: {os.getcwd()}")
    print(f"✗ Files available: {os.listdir('.')}")
    model = None
except Exception as e:
    print(f"✗ Error loading model: {e}")
    model = None

# ============================================================
# ROUTES
# ============================================================

@app.route('/')
def home():
    """Home page route"""
    return render_template('home.html')


@app.route('/prediction', methods=['POST', 'GET'])
def prediction():
    """Prediction form page"""
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    """Handle prediction request"""
    try:
        if model is None:
            return "Error: Model not loaded. Please check server console."
        
        # Get input values from form
        cgpa = float(request.form['cgpa'])
        iq = float(request.form['iq'])
        
        print(f"\n{'='*50}")
        print(f"Prediction Request:")
        print(f"CGPA: {cgpa}")
        print(f"IQ: {iq}")
        
        # Create feature array
        # If model expects 3 features (index, cgpa, iq):
        if model.n_features_in_ == 3:
            features = np.array([[0, cgpa, iq]])
            print(f"Using 3 features: [0, {cgpa}, {iq}]")
        # If model expects 2 features (cgpa, iq):
        else:
            features = np.array([[cgpa, iq]])
            print(f"Using 2 features: [{cgpa}, {iq}]")
        
        print(f"Features shape: {features.shape}")
        
        # Make prediction
        prediction = model.predict(features)[0]
        
        print(f"Prediction: {prediction} ({'Placed' if prediction == 1 else 'Not Placed'})")
        print(f"{'='*50}\n")
        
        # Return result page
        return render_template('result.html', prediction=int(prediction))
        
    except ValueError as ve:
        error_msg = "Invalid input! Please enter valid numbers."
        print(f"✗ ValueError: {ve}")
        return f"<h2>Error: {error_msg}</h2><a href='/prediction'>Go Back</a>"
        
    except Exception as e:
        print(f"✗ Prediction Error: {e}")
        import traceback
        traceback.print_exc()
        return f"<h2>Error: {str(e)}</h2><a href='/prediction'>Go Back</a>"


@app.route('/home', methods=['POST', 'GET'])
def my_home():
    """Alternative home route"""
    return render_template('home.html')


# ============================================================
# RUN APPLICATION
# ============================================================
if __name__ == '__main__':
    print("\n" + "="*70)
    print("🎓 STUDENT PLACEMENT PREDICTION SYSTEM")
    print("="*70)
    
    if model:
        print(f"✓ Status: READY")
        print(f"✓ Model Features: {model.n_features_in_}")
    else:
        print(f"✗ Status: MODEL NOT LOADED")
        
    print(f"\n🌐 Server URLs:")
    print(f"   • http://127.0.0.1:5000")
    print(f"   • http://localhost:5000")
    print(f"\nPress CTRL+C to quit")
    print("="*70 + "\n")
    
    app.run(debug=True, host='127.0.0.1', port=5000)
