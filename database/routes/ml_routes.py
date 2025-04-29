from flask import Blueprint, jsonify, request
from middleware.auth import token_required
from services.ml_inference_service import MLInferenceService
from services.synonym_service import SynonymService

ml_blueprint = Blueprint('ml', __name__)
mlInferenceService = MLInferenceService()
synonym_service = SynonymService()

@ml_blueprint.route('/get_inference', methods=['POST'])
@token_required
def get_inference():
    data = request.get_json()
    response = mlInferenceService.predict(data['word1'], data['word2'])
    return jsonify(response)

@ml_blueprint.route('/get_ml_words', methods=['GET'])
@token_required
def get_ml_words():
    try:
        ml_words = synonym_service.get_training_words()
        return jsonify(ml_words)
    except Exception as e:
        return jsonify({'error': str(e)}), 500
