import requests
import json
from db import WordDatabase
import sqlite3


class wordAddCron:
    conn = sqlite3.connect("words.db")
    c = conn.cursor()
    x_api_key = "cpo6D+MjDB+z5l+xFpU1zA==fsxZubMRPNpRZZ5l"

    def extractDef(self, dictionary_text):
        toret = ""
        periodCount = 0
        for i in range(len(dictionary_text)):
            if dictionary_text[i] == "2":
                break
            toret += dictionary_text[i]
        print(toret)
        return toret

    def makeLower(self, synonyms):
        for i in range(len(synonyms)):
            synonyms[i] = synonyms[i].lower()
        return synonyms

    def addOneWord(self):
        rand_word_url = "https://random-word-api.vercel.app/api?words=1"
        response = requests.get(rand_word_url)
        response_json = response.json()
        print(response_json)
        word = response_json[0]
        print(word)

        dictionary_url = "https://api.api-ninjas.com/v1/dictionary?word={}".format(word)
        response = requests.get(dictionary_url, headers={"X-Api-Key": self.x_api_key})
        response_json = response.json()
        if response.status_code == requests.codes.ok:
            print(response_json)
        else:
            print("Error:", response.status_code, response.text)
        dictionary_text = response_json["definition"]
        print(dictionary_text)
        if dictionary_text == "":
            return False

        synonyms_url = "https://api.api-ninjas.com/v1/thesaurus?word={}".format(word)
        response = requests.get(synonyms_url, headers={"X-Api-Key": self.x_api_key})
        response_json = response.json()
        if response.status_code == requests.codes.ok:
            print(response_json)
        else:
            print("Error:", response.status_code, response.text)
        synonym_text = response_json["synonyms"]

        synonym_status = True
        if synonym_text == []:
            synonym_status = False
            return synonym_status

        synonym_text = self.makeLower(synonym_text)

        dictionary_text = self.extractDef(dictionary_text)
        newWordEntry = {word: {"definition": dictionary_text, "synonyms": synonym_text}}
        print(newWordEntry)
        return newWordEntry

    def checkWordExists(self, word):
        self.c.execute(
            "SELECT word_name FROM WORDS WHERE word_name = ?",
            (word,),
        )
        result = self.c.fetchall()
        if len(result) > 0:
            print("found")
            return True
        print("unfound")
        return False

    def singleDataDump(self):
        result = self.addOneWord()
        if result == False:
            print("bad api response")
            return
        wordDb = WordDatabase()

        for word in result:
            wordExists = self.checkWordExists(word)
            if wordExists:
                continue
            print(word, result[word]["definition"], result[word]["synonyms"])
            wordDb.addWord(word, result[word]["definition"], result[word]["synonyms"])
        wordDb.wordCount()
        wordDb.commitChanges()

    def bulkDataDump(self):
        for i in range(0, 10):
            self.singleDataDump()
        return


wordCron = wordAddCron()
wordCron.bulkDataDump()
