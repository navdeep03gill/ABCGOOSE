from threading import main_thread
import requests
from bs4 import BeautifulSoup
import re


def genNewWord():
    rand_word_url = "https://random-word-api.vercel.app/api?words=1"
    response = requests.get(rand_word_url)
    response_json = response.json()
    print(response_json)
    word = response_json[0]
    return word


def wordHippoProcess(word):
    URL = f"https://www.wordhippo.com/what-is/another-word-for/{word}.html"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find(id="maintable")
    results_json = {"definition": "", "synonyms": []}
    # wordVerify = results.find(id="titleHeader")
    # print(wordVerify.b.text)
    wordMetaData = results.find_all("div", class_="wordtype")
    s = wordMetaData[0].text.replace("\n", "")
    wordType = re.sub("[^a-zA-Z]+", "", s)
    wordMetaData = results.find_all("div", class_="tabdesc")
    if wordMetaData == None or wordMetaData == []:
        return None
    definition = wordType + ". " + wordMetaData[0].text
    results_json["definition"] = definition
    synsDiv = results.find("div", class_="relatedwords")
    synsList = synsDiv.find_all("div", class_="wb")
    wordCount = 0
    synonyms = []
    for syn in synsList:
        if wordCount == 35:
            break
        synonym = syn.find("a").text.replace("\n", "")
        synonyms.append(synonym)
        wordCount += 1
    results_json["synonyms"] = synonyms
    return results_json


def fetchNewWords():
    wordList = []
    for i in range(0, 5):
        wordList.append(genNewWord())

    allSyns = {}
    for word in wordList:
        results = wordHippoProcess(word)
        if results == None:
            continue
        if len(results["synonyms"]) < 10:
            continue
        allSyns[word] = results
    for word in allSyns:
        print(word + ": ")
        print(allSyns[word])
    return allSyns
