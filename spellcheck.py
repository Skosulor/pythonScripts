import requests
import json
import sys

word = str(sys.argv[1])

#word = input("Enter a word: ")
requestSpellcheck = "https://montanaflynn-spellcheck.p.mashape.com/check/?text=" + word

response = requests.get(requestSpellcheck, headers={ "X-Mashape-Key": "YOUR-KEY", "Accept": "application/json"
  })

jResponse = response.json()

#print(response.status_code)
#print("-------------------")
#print(response.content)
#print("-------------------")
print("Suggestion: " + jResponse["suggestion"])
try:
	if (sys.argv[2] == '-m'):
		print("-------------------")
		corrDict = ((jResponse["corrections"])) #Hämta från rubrik "corrections"
		corrList = corrDict.get(word)
		for i in corrList:
			print(i)
		print("-------------------")
except: IndexError
