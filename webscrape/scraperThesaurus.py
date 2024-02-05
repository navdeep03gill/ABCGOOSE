from threading import main_thread
import requests
from bs4 import BeautifulSoup

# URL = "https://www.powerthesaurus.org/happy/synonyms"
# URL = "https://www.thesaurus.com/browse/happy"
# page = requests.get(URL)


def definition(word):
    URL = f"https://www.dictionary.com/browse/{word}"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    result = {"definition": ""}
    def_matches = soup.find_all("div", class_="ESah86zaufmd2_YPdZtq")
    for match in def_matches:
        definition = match.find("p")
        result["definition"] = definition.text
        if len(result["definition"]) > 0:
            break
    # print(result)
    return result


def synonyms(word):
    URL = f"https://www.thesaurus.com/browse/{word}"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find(id="ResultsContainer")

    results_json = {"synonyms": []}
    # strongest_matches = soup.find_all("p", string="Strongest matches")
    # for match in strongest_matches:
    #     print(match, end="\n" * 2)

    best_words = soup.find_all("div", class_="nMW14nFcYlw7pQJdjUvt")

    for section in best_words:
        strongest_matches = section.find_all("a", class_="KmScG4NplKj_3H5E3oA_")
        for match in strongest_matches:
            synonym = match.text
            results_json["synonyms"].append(synonym)
            # print("Strongest match: ", synonym)

        strong_matches = section.find_all("a", class_="kJDOl0PkCieROgWADccb")

        for match in strong_matches:
            synonym = match.text
            results_json["synonyms"].append(synonym)
            # print("Strong match: ", synonym)

        weak_matches = section.find_all("a", class_="g4U8AOuTWDHycT1H9v01")
        for match in weak_matches:
            synonym = match.text
            results_json["synonyms"].append(synonym)
            # print("Weak match: ", synonym)

    return results_json


def genNewWord():
    rand_word_url = "https://random-word-api.vercel.app/api?words=1"
    response = requests.get(rand_word_url)
    response_json = response.json()
    print(response_json)
    word = response_json[0]
    return word


def fetchNewWords():
    wordList = []
    for i in range(0, 10):
        wordList.append(genNewWord())

    allSyns = {}
    for word in wordList:
        defn = definition(word)
        defin = defn["definition"]
        if len(defin) == 0:
            print(word, "definition missing")
            continue
        syn = synonyms(word)
        syns = syn["synonyms"]
        if len(syns) == 0:
            print(word, "synonym missing")
            continue

        allSyns[word] = {"definition": defin, "synonyms": syns}
        print(word, ": ", allSyns[word])
        print("\n")

    return allSyns


# synonyms("righteous")
