from flask import Flask, render_template, request, jsonify
from fluxgan_core import load_model, predict_flux
import os

app = Flask(__name__)
MODEL_CACHE = {}

CHECKPOINT_DIR = "checkpoints"
REACTOR_MAP = {
    "phwr": "phwr.tar",
    "lwr": "lwr.tar",
    "pwr": "pwr.tar",
    "bwr": "bwr.tar",
    "fbr": "fbr.tar",
    "htgr": "htgr.tar"
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    reactor_type = data.get("reactor_type")
    enrichment = float(data.get("enrichment", 0.0))

    if reactor_type not in REACTOR_MAP:
        return jsonify({"error": "Invalid reactor type"}), 400

    checkpoint_path = os.path.join(CHECKPOINT_DIR, REACTOR_MAP[reactor_type])
    
    try:
        if reactor_type not in MODEL_CACHE:
            MODEL_CACHE[reactor_type] = load_model(checkpoint_path)
        model = MODEL_CACHE[reactor_type]
        flux = predict_flux(model, enrichment)
        return jsonify({"flux": flux})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

<<<<<<< HEAD
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 500))  # PORT env var is provided by Render
    app.run(host='0.0.0.0', port=port, debug=True)
=======
if __name__ == "__main__":
    app.run(debug=True)
>>>>>>> 2fc6a65 (Initial commit)
