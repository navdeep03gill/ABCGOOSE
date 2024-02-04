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


def fetchNewWords():
    medium_word_list = [
        "benevolent",  # altruistic
        "capitulate",  # surrender
        "disparate",  # distinct
        "ephemeral",  # fleeting
        "equivocal",  # ambiguous
        "exacerbate",  # worsen
        "furtive",  # secretive
        "gregarious",  # sociable
        "hackneyed",  # cliché
        "insidious",  # deceitful
        "juxtapose",  # compare
        "lament",  # mourn
        "myriad",  # countless
        "nostalgia",  # longing
        "obfuscate",  # confuse
        "paradox",  # contradiction
        "quell",  # suppress
        "resilient",  # tenacious
        "sycophant",  # flatterer
        "taciturn",  # reserved
    ]
    allSyns = {}
    for word in medium_word_list:
        defn = definition(word)
        defin = defn["definition"]
        syn = synonyms(word)
        syns = syn["synonyms"]
        allSyns[word] = {"definition": defin, "synonyms": syns}
        print(word, ": ", allSyns[word])
        print("\n")

    return allSyns


# synonyms("righteous")
fetchNewWords()
