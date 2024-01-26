from ntpath import realpath
from synonyms import allSynonyms

import sqlite3

class WordDatabase:
    conn = sqlite3.connect('words.db')
    c = conn.cursor()
    def dropTable(self, table):
        query = 'DROP TABLE IF EXISTS {}'.format(table)
        self.c.execute(query)
    
    def createTables(self):
        # Words table
        self.c.execute('''
            CREATE TABLE IF NOT EXISTS Words (
                word_id INTEGER PRIMARY KEY,
                word_name TEXT NOT NULL,
                definition TEXT NOT NULL
            );
        ''')
        # Synonyms table
        self.c.execute('''
            CREATE TABLE IF NOT EXISTS Synonyms (
                synonym_id INTEGER PRIMARY KEY,
                word_id INTEGER,
                synonym TEXT NOT NULL,
                score INTEGER,
                FOREIGN KEY(word_id) REFERENCES Words(word_id)
            );
        ''')
    
    def addWord(self, word_name, definition, synonyms):
        conn = sqlite3.connect('words.db')
        c = conn.cursor()
        # Insert word into Words table
        c.execute('INSERT OR IGNORE INTO Words (word_name, definition) VALUES (?, ?)', (word_name, definition))
        word_id = c.lastrowid  # Get the ID of the inserted word
        # Insert synonyms into Synonyms table
        for synonym in synonyms:
            c.execute('INSERT INTO Synonyms (word_id, synonym, score) VALUES (?, ?, ?)', (word_id, synonym, synonyms[synonym]))
        # Commit changes and close the connection
        conn.commit()
        conn.close()
        
    def get_word_with_synonyms(self, word_name):
        conn = sqlite3.connect('words.db')
        c = conn.cursor()
        # Get word details along with synonyms for the given word_name
        c.execute('''
            SELECT Words.word_name, Words.definition, Synonyms.synonym, Synonyms.score
            FROM Words
            LEFT JOIN Synonyms ON Words.word_id = Synonyms.word_id
            WHERE Words.word_name = ?
        ''', (word_name,))
        result = c.fetchall()
        conn.close()
        return result

    def get_word_with_syn_and_score(self, word_name):
        conn = sqlite3.connect('words.db')
        c = conn.cursor()
        # Get word details along with synonyms and scores for the given word_name
        c.execute('''
            SELECT Words.word_name, Words.definition, Synonyms.synonym, Synonyms.score
            FROM Words
            LEFT JOIN Synonyms ON Words.word_id = Synonyms.word_id
            WHERE Words.word_name = ?
        ''', (word_name,))
        result = {}
        for row in c.fetchall():
            word_name, definition, synonym, score = row
            if word_name not in result:
                result[word_name] = {'definition': definition, 'synonyms': {}}
            result[word_name]['synonyms'][synonym] = score
        conn.close()
        return result

    def get_all_words_with_synonyms(self):
        conn = sqlite3.connect('words.db')
        c = conn.cursor()
        c.execute('''
            SELECT Words.word_id, Words.word_name, Words.definition, Synonyms.synonym, Synonyms.score
            FROM Words
            LEFT JOIN Synonyms ON Words.word_id = Synonyms.word_id
        ''')
        result = {}
        for row in c.fetchall():
            word_id, word_name, definition, synonym, score = row
            if word_id not in result:
                result[word_id] = {'word': word_name, 'definition': definition, 'synonyms': {}}
            result[word_id]['synonyms'][synonym] = score

        toret = []
        for word_id, word_info in result.items():
            toret.append(word_info)

        for word_id, word_info in result.items():
            print(f" {word_id}:")
            print(f"  Word: {word_info['word']}:")
            print(f"  Definition: {word_info['definition']}")
            print("  Synonyms:")
            for synonym, score in word_info['synonyms'].items():
                print(f"    {synonym}: {score}")
            print()
        conn.close()
        return toret
    

    def populateTable(self):
        for word in allSynonyms:
            self.addWord(word, allSynonyms[word]["definition"], allSynonyms[word]["synonyms"])
    
    def commitChanges(self):
        # Commit Connection
        self.conn.commit()
        # Close our connection
        self.conn.close()


wordDb = WordDatabase()
wordDb.dropTable("Words")
wordDb.dropTable("Synonyms")
wordDb.createTables()
wordDb.populateTable()
wordDb.get_all_words_with_synonyms()


