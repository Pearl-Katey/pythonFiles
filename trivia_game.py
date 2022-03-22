#a trivia game

import requests
import json


r = requests.get("https://opentdb.com/api.php?amount=10&category=20&difficulty=easy&type=multiple")
question = json.loads(r.text)
category = question['results'][0]['category']
print(category)