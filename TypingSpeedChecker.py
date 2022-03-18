"""
Create a program to help the user type faster. Give him a word and ask him to write it five 
times. Check how many seconds it took him to type the word at each round.
In the end tell the user how many mistakes were made and show a chart with the typing speed evolution during the 5 rounds
"""

import time
# import matplotlib.pyplot as plt
TimeTaken=[]
WordTyped = []
mistakes= 0
print("###############################\n You will be asked to type a string\n this will help us check your typing speed\n#######################################")
input("Press enter to continue")
checkingString = "bananaflakes"       #input("Type what you want to use to check your typing speed here: ")#
while len(TimeTaken) < 5:
    start = time.time()
    word = input("Type " + checkingString+ ": ")
    finish = time.time()
    TimeTaken.append(time.localtime(finish-start).tm_sec)
    WordTyped.append(word)
    if word.lower() != checkingString:
        mistakes += 1


print("You made "+ str(mistakes)+ " mistake(s).")
print('Now lets See your Evolution')
input("press Enter")

x = [1,2,3,4,5]
y = TimeTaken
plt.plot(x,y)
legend = ['1','2','3','4','5']
plt.xticks(x,legend)
plt.ylabel("Time in seconds")
plt.xlabel("Attempts")
plt.title("Your evolution attempts")
plt.show()
























# def getWordsAndTime(): 
#     TimeTaken=[]
#     WordTyped = []
#     print("###############################\n You will be asked to type a string\n this will help us check your typing speed")
#     checkingString = input("Type what you want to use to check your typing speed here: ")
#     for i in range(0, 4):
#         initialTime = float(time.time())
#         typed = input("Type '%d'", checkingString)
#         finalTime = float(time.time())
#         TimeTaken.append(str(time.localtime(finalTime-initialTime).tm_min)+"." +str(time.localtime(finalTime-initialTime).tm_sec))
#         WordTyped.append(typed)
#     return(TimeTaken,WordTyped)

# def checkMistakes(giveList): 
#     giveList = getWordsAndTime().WordTyped



# print(TimeTaken)
# print(WordTyped)




