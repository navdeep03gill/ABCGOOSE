import sys
import os
from dotenv import load_dotenv
import psycopg2 

load_dotenv()

"""
This is using the DATABASE_DEV instead of production database.
Make sure to change back when module is fine tuned.


We don't enable deletion from the thesaurus database.
It's schema is robust. If that becomes a need, db admin will
handle it. Seems unlikely we need db or table delete methods.
"""

class WordDatabase:
    def __init__(self):
        self.conn = psycopg2.connect(
            database=os.getenv("DATABASE_DEV"), 
            user=os.getenv("DB_USER"), 
            password=os.getenv("DB_USER_PASSWORD"), 
            host=os.getenv("HOST"),
            port=os.getenv("PORT")
        )
        self.cur = self.conn.cursor()

    def delete_all_rows(self):
        self.cur.execute("DELETE FROM WORDS WHERE word_id IS NOT NULL")
        self.cur.execute("DELETE FROM SYNONYMS WHERE synonym_id IS NOT NULL")

    def delete_word_by_word_name(self, word_name) -> None:
        self.cur.execute("SELECT word_id FROM WORDS WHERE word_name = ?", (word_name,))
        result = self.cur.fetchall()
        if len(result) == 0:
            return
        word_id = result[0][0]
        print(word_id)
        self.cur.execute(
            '''
            DELETE FROM Synonyms
            WHERE word_id = %s''', (word_id,),
        )
        self.cur.execute(
            '''
            DELETE FROM WORDS 
            WHERE word_id = %s''', (word_id,),
        )
        self.conn.commit()
        return

    def delete_word_by_word_id(self, word_id) -> None:
        self.cur.execute(
            '''
            DELETE FROM Synonyms
            WHERE word_id = %s''', (word_id,),
        )
        self.cur.execute(
            '''
            DELETE FROM WORDS 
            WHERE word_id = %s''', (word_id,),
        )
    
    def add_word(self, word_name, definition, synonyms):
        self.cur.execute(
            '''
            INSERT INTO Words (word_name, definition) 
            VALUES (%s, %s) RETURNING word_id''',
            (word_name, definition),
        )
        word_id = self.cur.fetchone()[0] # Get the ID of the inserted word
        # Insert synonyms into Synonyms table
        for synonym in synonyms:
            self.cur.execute(
                '''
                INSERT INTO Synonyms (word_id, synonym) 
                VALUES (%s, %s)''',
                (word_id, synonym),
            )
        # Commit changes and close the connection
        self.conn.commit()
    
    def get_word_with_synonyms(self, word_name):
        self.cur.execute(
            """
            SELECT Words.word_name, Words.definition, Synonyms.synonym
            FROM Words
            INNER JOIN Synonyms ON Words.word_id = Synonyms.word_id
            WHERE Words.word_name = ?
        """,
            (word_name,),
        )
        result = self.cur.fetchall()
        print(result)
        return result
    
    def preview_random_words(self, limit=10) -> None:
        self.cur.execute(
            """
            SELECT Words.word_name
            FROM Words
            ORDER BY RANDOM()
            LIMIT %s""", (limit,),
        )
        result = self.cur.fetchall()
        word_list = []
        for item in result:
            word_list.append(item[0])
            self.preview_word_and_synonym(item[0])
        return
    
    def preview_word_and_synonym(self, word_name):
        self.cur.execute(
            """
            SELECT Words.word_name, Words.definition, Synonyms.synonym
            FROM Words
            INNER JOIN Synonyms ON Words.word_id = Synonyms.word_id
            WHERE Words.word_name = %s
            """, (word_name,),
        )
        query = self.cur.fetchall()
        result = {}
        for row in query:
            word_name, definition, synonym = row
            if word_name not in result:
                result[word_name] = {"definition": definition, "synonyms": []}
            result[word_name]["synonyms"].append(synonym)
        print(result)
        print()
        return result
    
    def get_some_words_with_synonyms(self, limit):
        if limit < 2:
            print("At least two words need to be fetched")
            return
        self.cur.execute(
            """
            SELECT Words.word_id, Words.word_name
            FROM Words
            ORDER BY RANDOM()
            LIMIT %s
            """, (limit,),
        )
        initial_words = self.cur.fetchall()
        word_ids = tuple(row[0] for row in initial_words)
        self.cur.execute(
            """
            SELECT Words.word_id, Words.word_name, Words.definition, Synonyms.synonym
            FROM Words
            INNER JOIN Synonyms ON Words.word_id = Synonyms.word_id
            WHERE Words.word_id IN {}
            """.format(str(word_ids))
        )
        query = self.cur.fetchall()
        result = {}
        for row in query:
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


    def get_all_words_with_synonyms(self):
        self.cur.execute(
            """
            SELECT Words.word_id, Words.word_name, Words.definition, Synonyms.synonym
            FROM Words
            INNER JOIN Synonyms ON Words.word_id = Synonyms.word_id
        """
        )
        query = self.cur.fetchall()
        result = {}
        for row in query:
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

    def get_cardinalities(self):
        self.cur.execute(
            """
            SELECT COUNT(*)
            FROM Words
            """
        )
        word_count = self.cur.fetchall()
        print("Word Table Count:", word_count)
        self.cur.execute(
            """
            SELECT COUNT(*)
            FROM Synonyms
            """
        )
        syn_count = self.cur.fetchall()
        print("Synonym Table Count:", syn_count)


    def populate_table(self, newData):
        for word in newData:
            self.cur.execute(
                """
                SELECT *
                FROM Words
                WHERE word_name = %s
                """,
                (word,),
            )
            result = self.cur.fetchall()
            if len(result) > 0:
                continue
            self.add_word(
                word, newData[word]["definition"], newData[word]["synonyms"]
            )


    def clean_tables(self):
        '''
        Remove duplicate words but keep the latest entry as distinct
        '''
        self.cur.execute(
            """
            SELECT w1.word_id, w1.word_name, w1.definition
            FROM Words w1
            WHERE EXISTS (
                SELECT 1
                FROM Words w2
                WHERE w1.word_id <> w2.word_id and w1.word_name = w2.word_name
            )
            """
        )
        result = self.cur.fetchall()
        print(result)
        for i in range(0, len(result) - 1):
            word_to_delete = str(result[i][0])
            self.delete_word_by_word_id(word_to_delete)

        '''
        Remove words that have less than 10 synonyms
        '''
        self.cur.execute(
            """
            SELECT word_id
            FROM Words
            WHERE NOT EXISTS (
                SELECT cnt
                FROM (
                    SELECT COUNT(*) as cnt
                    FROM Synonyms
                    WHERE Synonyms.word_id = Words.word_id
                    )
                WHERE cnt > 10
            )
            """
        )
        result = self.cur.fetchall()
        word_ids = tuple(row[0] for row in result)
        for word_id in word_ids:
            self.delete_word_by_word_id(word_id)
    
    def print_words_with_synonyms(self, results):
        for r in results:
            print("\nWord:", r['word'])
            print("Definition: ", r["definition"])
            print("Synonyms: ", r["synonyms"])

    def commit_changes(self):
        # Commit Connection
        self.conn.commit()
        # Close our connection
        self.conn.close()


def main():
    word_db = WordDatabase()
    # word_db.add_word("nav", "name", [])
    # word_db.clean_tables()
    # some_words = word_db.get_some_words_with_synonyms(5)
    # word_db.print_words_with_synonyms(some_words)
    # word_db.get_cardinalities()
    # word_db.commit_changes()
    return

if __name__ == "__main__":
    main()
