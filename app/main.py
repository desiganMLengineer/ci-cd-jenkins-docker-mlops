
from flask import Flask, render_template_string, jsonify
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import numpy as np
import datetime

app = Flask(__name__)

# Load industry-standard dataset and train Random Forest model
iris = load_iris()
X, y = iris.data, iris.target
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)

# High-end, modern SaaS UI Dashboard template
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>MLOps Production Dashboard</title>
    <style>
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background: #0f172a; color: #f8fafc; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }
        .card { background: #1e293b; padding: 40px; border-radius: 16px; box-shadow: 0 10px 25px rgba(0,0,0,0.4); width: 480px; border: 1px solid #334155; }
        h2 { margin-top: 0; color: #38bdf8; font-size: 22px; display: flex; align-items: center; gap: 10px; }
        .badge { background: #065f46; color: #34d399; padding: 4px 12px; border-radius: 20px; font-size: 11px; font-weight: bold; text-transform: uppercase; float: right; letter-spacing: 0.5px; }
        .metric { background: #0f172a; padding: 16px; border-radius: 10px; margin: 16px 0; border: 1px solid #334155; }
        .label { color: #94a3b8; font-size: 12px; text-transform: uppercase; letter-spacing: 0.8px; }
        .value { font-size: 18px; font-weight: bold; color: #e2e8f0; margin-top: 6px; }
        .footer { font-size: 11px; color: #64748b; text-align: center; margin-top: 24px; border-top: 1px solid #334155; padding-top: 14px; }
        a { color: #38bdf8; text-decoration: none; font-weight: 600; }
        a:hover { text-decoration: underline; }
    </style>
</head>
<body>
    <div class="card">
        <span class="badge">Live Production</span>
        <h2>🚀 MLOps Model Inference</h2>
        <div class="metric">
            <div class="label">Model Architecture</div>
            <div class="value">Random Forest Classifier (Iris Dataset)</div>
        </div>
        <div class="metric">
            <div class="label">Input Vector Features</div>
            <div class="value" style="font-size: 14px; font-family: monospace; color: #38bdf8;">{{ features }}</div>
        </div>
        <div class="metric">
            <div class="label">Inference Result</div>
            <div class="value" style="color: #34d399; text-transform: uppercase;">{{ prediction }} <span style="font-size: 13px; color: #94a3b8; font-weight: normal;">(Confidence: {{ confidence }}%)</span></div>
        </div>
        <div class="footer">
            Automated via Jenkins CI/CD & Docker &bull; <a href="/api/predict" target="_blank">View JSON API</a>
        </div>
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    sample_input = np.array([[5.1, 3.5, 1.4, 0.2]])
    prediction_idx = model.predict(sample_input)[0]
    predicted_species = iris.target_names[prediction_idx]
    
    # Calculate confidence percentage from model probabilities
    probabilities = model.predict_proba(sample_input)[0]
    confidence = round(float(probabilities[prediction_idx]) * 100, 2)
    
    return render_template_string(
        HTML_TEMPLATE,
        features=str(list(sample_input[0])),
        prediction=predicted_species,
        confidence=confidence
    )

@app.route('/api/predict', methods=['GET'])
def api_predict():
    sample_input = np.array([[5.1, 3.5, 1.4, 0.2]])
    prediction_idx = model.predict(sample_input)[0]
    probabilities = model.predict_proba(sample_input)[0]
    
    return jsonify({
        "status": "success",
        "model": "Random Forest Classifier",
        "dataset": "Iris",
        "input_features": list(sample_input[0]),
        "prediction": iris.target_names[prediction_idx],
        "confidence_score": round(float(probabilities[prediction_idx]) * 100, 2),
        "timestamp": datetime.datetime.utcnow().isoformat()
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
