from nltk.corpus import wordnet as wn
from sklearn.feature_extraction.text import TfidfVectorizer
import re

def clean_definition(definition):
    return re.sub(r'[^a-zA-Z ]', '', 
                 definition.split(';')[0].lower())

def calculate_definition_similarity(word1, word2):
    def1 = ' '.join([clean_definition(s.definition())
                    for s in wn.synsets(word1)])
    def2 = ' '.join([clean_definition(s.definition())
                    for s in wn.synsets(word2)])
    
    vectorizer = TfidfVectorizer(ngram_range=(1,2))
    tfidf = vectorizer.fit_transform([def1, def2])
    return (tfidf[0] * tfidf[1].T).toarray()[0][0]

