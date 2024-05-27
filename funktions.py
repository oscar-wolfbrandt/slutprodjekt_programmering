import json
import time 
import os 
from colors import bcolors
import msvcrt

# funktion för att skapa nytt test eller öpna gamalt 

def newtest():
    #ökar testnum med 1 
    with open("question.json", "r") as test:
        l = json.load(test)
    l[0]["testnum"] = l[0]["testnum"] + 1 

    currentnum =  l[0]["testnum"]
    with open("question.json", "w") as file:
        json.dump(l,file)

    with open("test"+str(currentnum)+".json", "w") as new:
        json.dump(l,new)
    return currentnum


def forward(y):
    if y < 21: 
        y = y +1
    elif y == 10:
        print("last question")
        time.sleep(2)
    return y 

def backward(y):
    if y > 0:
        y = int(y - 1)
    elif y == 0:
        print("Cant go back more")
        time.sleep(2)
    return(y)

def showquestion(y,testnum):
    with open("test"+str(testnum)+".json", "r") as test:
        l = json.load(test)
    os.system("cls")
    print(bcolors.PURPLE+"Testnumber:",testnum,"/press h to see controls")
    print(bcolors.CYAN+str(y+1),"/20:",l[y]["question"+str(y+1)])
    print(bcolors.GREEN+"Current answer:",l[y]["q"+str(y+1)+"input"])
    return y, testnum
