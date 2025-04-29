## Embedding Similarity
import gensim.downloader
from scipy.spatial.distance import cosine

glove_vectors = gensim.downloader.load('glove-wiki-gigaword-100')

def calculate_embedding_similarity(word1, word2):
    try:
        vec1 = glove_vectors[word1]
        vec2 = glove_vectors[word2]
        return 1 - cosine(vec1, vec2)
    except KeyError:
        return 0 # handle OOV words
