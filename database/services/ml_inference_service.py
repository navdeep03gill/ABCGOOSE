from ml_app.model_loader import load_model
from ml_app.preprocess_input import preprocess_input

class MLInferenceService:
    def __init__(self):
        self.model, self.label_encoder_pos, self.scaler, self.feature_order = load_model()
        return
    
    def predict(self, word1: str, word2: str):
        try:
            # Load the model
            if None in (self.model, self.label_encoder_pos, self.scaler):
                raise RuntimeError("Model components not loaded")
            # Get data from request
            
            # Format words (replace spaces with underscores)
            word1 = "_".join(word1.split())
            word2 = "_".join(word2.split())
            
            features_scaled = preprocess_input(
                word1,
                word2,
                self.label_encoder_pos,
                self.scaler,
                self.feature_order
            )
            # Make prediction
            prediction = self.model.predict(features_scaled)
            prediction_proba = self.model.predict_proba(features_scaled)
            
            is_synonym = bool(prediction[0])
            confidence = float(prediction_proba[0][1])  # Probability of being a synonym

            # Return results
            return {
                'word1': word1,
                'word2': word2,
                'is_synonym': is_synonym,
                'confidence': confidence,
                'result': 'synonyms' if is_synonym else 'not synonyms'
            }
        except Exception as e:
            return {'error': str(e)}
