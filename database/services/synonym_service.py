from db.db import WordDatabase

class SynonymService:
    def __init__(self):
        self.word_db = WordDatabase()
    
    def get_words(self, limit=50):
        return self.word_db.get_some_words_with_synonyms(limit=limit)
    
    def create_words(self, word_list):
        self.word_db.populate_table(word_list)
    
    def get_training_words(self, limit=50):
        return self.word_db.fetch_ml_words(limit=limit)

