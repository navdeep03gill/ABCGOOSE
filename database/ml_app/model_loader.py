import joblib

_model_cache = None

def load_model(model_path='ml_app/models/logistic_regression_model.pkl'):
    global _model_cache
    if _model_cache is None:
        model_data = joblib.load(model_path)
        return (
            model_data['model'],
            model_data['label_encoder_pos'],
            model_data['scaler'],
            model_data['feature_order']
        )
    else:
        print("⚡ Reusing cached model in memory.")
    return _model_cache
    
