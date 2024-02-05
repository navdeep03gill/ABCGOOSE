from ntpath import realpath
from synonyms import allSynonyms
import sys

sys.path.append("../")
from webscrape.scraperThesaurus import fetchNewWords

import sqlite3


class WordDatabase:
    def __init__(self):
        self.conn = sqlite3.connect("words.db")
        self.c = self.conn.cursor()

    def dropTable(self, table):
        query = "DROP TABLE IF EXISTS {}".format(table)
        self.c.execute(query)

    def createTables(self):
        # Words table
        self.c.execute(
            """
            CREATE TABLE IF NOT EXISTS Words (
                word_id INTEGER PRIMARY KEY,
                word_name TEXT NOT NULL,
                definition TEXT NOT NULL
            );
        """
        )
        # Synonyms table
        self.c.execute(
            """
            CREATE TABLE IF NOT EXISTS Synonyms (
                synonym_id INTEGER PRIMARY KEY,
                word_id INTEGER,
                synonym TEXT NOT NULL,
                FOREIGN KEY(word_id) REFERENCES Words(word_id)
            );
        """
        )

    def deleteWord(self, word_name):
        self.c.execute("SELECT word_id FROM WORDS WHERE word_name = ?", (word_name,))
        result = self.c.fetchall()
        if len(result) == 0:
            return
        word_id = result[0][0]
        print(word_id)

        self.c.execute("DELETE FROM WORDS WHERE word_id = ?", (word_id,))
        self.c.execute(
            "DELETE FROM Synonyms WHERE word_id = ? ",
            (word_id,),
        )
        self.conn.commit()
        self.conn.close()

    def addWord(self, word_name, definition, synonyms):
        self.c.execute(
            "INSERT OR IGNORE INTO Words (word_name, definition) VALUES (?, ?)",
            (word_name, definition),
        )
        word_id = self.c.lastrowid  # Get the ID of the inserted word
        # Insert synonyms into Synonyms table
        for synonym in synonyms:
            self.c.execute(
                "INSERT INTO Synonyms (word_id, synonym) VALUES (?, ?)",
                (word_id, synonym),
            )
        # Commit changes and close the connection
        self.conn.commit()

    def get_word_with_synonyms(self, word_name):
        self.c.execute(
            """
            SELECT Words.word_name, Words.definition, Synonyms.synonym
            FROM Words
            INNER JOIN Synonyms ON Words.word_id = Synonyms.word_id
            WHERE Words.word_name = ?
        """,
            (word_name,),
        )
        result = self.c.fetchall()
        print(result)
        return result

    def get_word_with_syn_and_score(self, word_name):
        self.c.execute(
            """
            SELECT Words.word_name, Words.definition, Synonyms.synonym
            FROM Words
            INNER JOIN Synonyms ON Words.word_id = Synonyms.word_id
            WHERE Words.word_name = ?
        """,
            (word_name,),
        )
        result = {}
        for row in self.c.fetchall():
            word_name, definition, synonym = row
            if word_name not in result:
                result[word_name] = {"definition": definition, "synonyms": []}
            result[word_name]["synonyms"].append(synonym)
        print(result)
        return result

    def get_all_words_with_synonyms(self):
        # conn = sqlite3.connect("words.db")
        # c = conn.cursor()
        self.c.execute(
            """
            SELECT Words.word_id, Words.word_name, Words.definition, Synonyms.synonym
            FROM Words
            INNER JOIN Synonyms ON Words.word_id = Synonyms.word_id
        """
        )
        result = {}
        for row in self.c.fetchall():
            word_id, word_name, definition, synonym = row
            if word_id not in result:
                result[word_id] = {
                    "word": word_name,
                    "definition": definition,
                    "synonyms": [],
                }
            result[word_id]["synonyms"].append(synonym)

        toret = []
        for word_id, word_info in result.items():
            toret.append(word_info)
        return toret

    def populateTable(self, newSynonyms):
        for word in newSynonyms:
            self.c.execute(
                """
                SELECT *
                FROM Words
                WHERE word_name = ?
                """,
                (word,),
            )
            result = self.c.fetchall()
            if len(result) > 0:
                continue
            self.addWord(
                word, newSynonyms[word]["definition"], newSynonyms[word]["synonyms"]
            )

    def checkDuplicates(self):
        self.c.execute(
            """
                SELECT word_name, COUNT(*)
                FROM WORDS 
                GROUP BY word_name
                HAVING COUNT(*) > 1
            """
        )
        result = self.c.fetchall()

    def cleanTables(self):
        self.c.execute(
            """
            SELECT * FROM Words
            WHERE NOT EXISTS (
                    SELECT 1
                    FROM Synonyms
                    WHERE Synonyms.word_id = Words.word_id
                )
            """
        )
        result = self.c.fetchall()
        print(result)
        self.c.execute(
            """
            DELETE FROM Words
            WHERE NOT EXISTS (
                    SELECT 1
                    FROM Synonyms
                    WHERE Synonyms.word_id = Words.word_id
                )
            """
        )

    def wordCount(self):
        self.c.execute(
            """
            SELECT COUNT(*)
            FROM Words
        """
        )
        result = self.c.fetchall()
        print(result)
        return result

    def commitChanges(self):
        # Commit Connection
        self.conn.commit()
        # Close our connection
        self.conn.close()


# TEST SUITE
def main():
    wordDb = WordDatabase()
    # wordDb.dropTable("Words")
    # wordDb.dropTable("Synonyms")
    # wordDb.createTables()

    newWords = fetchNewWords()
    print(newWords)
    wordDb.populateTable(newWords)
    wordDb.checkDuplicates()
    # print("wordDB word count: ")
    wordDb.wordCount()
    wordDb.commitChanges()


if __name__ == "__main__":
    main()
