from db import WordDatabase
import sys
sys.path.append("../")
from webscraper.scraperWordHippo import fetchNewWords


class WordAddCron:
    def __init__(self):
        self.word_db = WordDatabase()

    def make_lower(self, synonyms):
        for i, synonym in enumerate(synonyms):
            synonyms[i] = synonym.lower()
        return synonyms
    
    def remove_synonyms_in_definition(self, definition, synonyms):
        definition_words = definition.lower().split()
        final_synonyms = []
        synonyms = self.make_lower(synonyms)
        final_synonyms = [syn for syn in synonyms if syn not in definition_words]
        return final_synonyms

    def pre_process_synonyms(self, new_data):
        changed_data = new_data.copy()
        for data in new_data:
            definition = changed_data[data]["definition"]
            synonyms = changed_data[data]["synonyms"]
            changed_data[data]["synonyms"] = self.remove_synonyms_in_definition(definition, synonyms)
        return changed_data

    def single_data_dump(self):
        new_data = fetchNewWords()
        updated_data = self.pre_process_synonyms(new_data)
        for word, word_data in updated_data.items():
            print(word + ": ")
            print(word_data)
        self.word_db.populate_table(updated_data)

    def bulk_data_dump(self):
        for i in range(0, 10):
            self.single_data_dump()
        return


word_cron = WordAddCron()
word_cron.bulk_data_dump()
