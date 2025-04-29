from nltk.corpus import wordnet as wn
from nltk import ngrams
from nltk.stem import SnowballStemmer


def calculate_lexical_similarity(word1, word2):
    stemmer = SnowballStemmer('english')
    stem1 = stemmer.stem(word1)
    stem2 = stemmer.stem(word2)
    tri1 = set(ngrams(stem1, 3, pad_left=True, pad_right=True))
    tri2 = set(ngrams(stem2, 3, pad_left=True, pad_right=True))
    intersection = tri1 & tri2
    union = tri1 | tri2
    return len(intersection) / len(union) if union else 0
