from nltk.corpus import wordnet as wn

def wordnet_features(word1, word2):
    synsets1 = wn.synsets(word1)
    synsets2 = wn.synsets(word2)
    path_sim = wup_sim = 0
    for s1 in synsets1:
        for s2 in synsets2:
            current_path = s1.path_similarity(s2) or 0
            current_wup = s1.wup_similarity(s2) or 0
            if current_path > path_sim:
                path_sim = current_path
            if current_wup > wup_sim:
                wup_sim = current_wup
    return path_sim, wup_sim
