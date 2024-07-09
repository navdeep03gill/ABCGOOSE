import sys
import os

from scraperWordHippo import fetchNewWords

def test_fetchNewWords():
    words = fetchNewWords()
    print(words)

if __name__ == "__main__":
    test_fetchNewWords()
    print("Test passed")