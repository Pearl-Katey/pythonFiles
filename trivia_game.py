#a trivia game

import requests
import json


endGame = ""
count = 0

r = requests.get("https://opentdb.com/api.php?amount=10&category=20&difficulty=easy&type=multiple")

while endGame !="quit":
    endGame = input("Press enter to continue or 'quit' to end game ")
    if r.status_code == 200:
        data = json.loads(r.text)
        category = data['results']
        for i in range(len(category)):
            question =  category[i]['question']
            possible_answers = category[i]['incorrect_answers'] 
            answer = category[i]["correct_answer"]
            possible_answers.append(answer)
            print("Round "+ str(i+1))
            print(question)
            print(possible_answers)
            ans = input("please enter your answer: ")
            if (ans.lower() == answer.lower()):
                count += 1
                print("Correct✅✅✅✅✅")
            else:
                print("Wrong❌❌❌❌")
        print("You got "+ str(count) +" correct answers")



# print(len(category)) 
