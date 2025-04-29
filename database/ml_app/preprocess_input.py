import pandas as pd
from nltk.corpus import wordnet as wn
from ml_app.metrics.definition_similarity import calculate_definition_similarity
from ml_app.metrics.lexical_similarity import calculate_lexical_similarity
from ml_app.metrics.embedding_similarity import calculate_embedding_similarity
from ml_app.metrics.path_wup_similarity import wordnet_features

def preprocess_input(word1, word2, label_encoder_pos, scaler, feature_order):
    # Get POS for words
    word1_pos = get_pos(word1)
    word2_pos = get_pos(word2)
    # Use persisted encoder
    try:
        word1_pos_encoded = label_encoder_pos.transform([word1_pos])[0]
        word2_pos_encoded = label_encoder_pos.transform([word2_pos])[0]
    except ValueError as e:
        print(f"Unknown POS tag: {e}")
        word1_pos_encoded = -1
        word2_pos_encoded = -1
    # Calculate similarity features
    lexical_similarity = calculate_lexical_similarity(word1, word2)
    vector_cosine_similarity = calculate_embedding_similarity(word1, word2)
    path_similarity, wup_similarity = wordnet_features(word1, word2)
    definition_similarity = calculate_definition_similarity(word1, word2)
    
    features = pd.DataFrame([[
        lexical_similarity,
        vector_cosine_similarity, 
        path_similarity,
        wup_similarity, 
        definition_similarity,
        word1_pos_encoded, 
        word2_pos_encoded
    ]], columns=feature_order)
    return scaler.transform(features)

def get_pos(word):
    synsets = wn.synsets(word)
    if synsets:
        pos = synsets[0].pos()
        return {'n': 'Noun', 'v': 'Verb', 'a': 'Adjective', 's': 'Adjective', 'r': 'Adverb'}.get(pos, pos)
    return 'Unknown'
