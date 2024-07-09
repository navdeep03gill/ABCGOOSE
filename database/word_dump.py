import requests
import json
from db import WordDatabase
import sqlite3
import sys
sys.path.append("../")
from webscraper.scraperWordHippo import fetchNewWords


class wordAddCron:
    def __init__(self):
        self.word_db = WordDatabase()

    def makeLower(self, synonyms):
        for i in range(len(synonyms)):
            synonyms[i] = synonyms[i].lower()
        return synonyms
    
    def removeSynonymsInDefinition(self, definition, synonyms):
        definition_words = definition.lower().split()
        final_synonyms = []
        synonyms = self.makeLower(synonyms)
        final_synonyms = [syn for syn in synonyms if syn not in definition_words]
        return final_synonyms

    def preProcessSynonyms(self, newData):
        changedData = newData.copy()
        for data in newData:
            definition = changedData[data]["definition"]
            synonyms = changedData[data]["synonyms"]
            changedData[data]["synonyms"] = self.removeSynonymsInDefinition(definition, synonyms)
        return changedData

    def singleDataDump(self):
        newData = fetchNewWords()
        updatedData = self.preProcessSynonyms(newData)

        for word in updatedData:
            print(word + ": ")
            print(updatedData[word])

        self.word_db.populateTable(updatedData)

    def bulkDataDump(self):
        for i in range(0, 10):
            self.singleDataDump()
        return


wordCron = wordAddCron()
wordCron.bulkDataDump()
