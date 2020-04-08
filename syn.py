#!/usr/bin/env python

import requests
import sys
import re
from bs4 import BeautifulSoup



def getSynonyms(word, recursive):
    w = word
    page = requests.get('https://www.thesaurus.com/browse/' + word)
    soup = BeautifulSoup(page.content, 'html.parser')
    texts = soup.find_all('a')

    tt = []

    for t in texts:
        tt.append(t.get_text())
        # print(t.get_text())

    start = [ i for i, word in enumerate(tt) if word.startswith('SEE DEFINITION OF') ]
    try:
        end   = [ i for i, word in enumerate(tt) if word.startswith('PREVIOUS') ]
    except:
        end   = [ i for i, word in enumerate(tt) if word.startswith('OTHERS ARE READING') ]

    if end == []:
        end   = [ i for i, word in enumerate(tt) if word.startswith('OTHERS ARE READING') ]

    try:
        for t in reversed(tt[start[0]+1:end[0]]):
            print(t)
    except:
        print('Could not find synonyms, maybe the word is misspelled?')


try:
    word = str(sys.argv[1])
except:
    try:
        word = sys.stdin.read()
    except:
        print("No input arguments")
    
getSynonyms(word, True)
# print(start)
# print(end)
