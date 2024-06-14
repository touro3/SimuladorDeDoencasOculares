from flask import Blueprint, request, jsonify
from app.models.disease_model.py import load_disease_model, predict_disease_effect

simulate_bp = Blueprint('simulate', __name__)
model = load_disease_model()

@simulate_bp.route('/simulate', methods=['POST'])
def simulate():
    image = request.files['image']
    # Pre-process the image
    prediction = predict_disease_effect(image, model)
    return jsonify({'prediction': prediction.tolist()})
