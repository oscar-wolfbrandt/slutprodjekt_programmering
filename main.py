import os
import time
import json
import msvcrt
from funktions import newtest
from funktions import forward
from funktions import backward
from funktions import showquestion
from colors import bcolors

y = 0
on = True
qnum = 0
inputs = ["p","o","a","b","c","d","h","q"]
do = "."
first = True
currentnum = 0
point = 0 


while on == True:
    #meny
    while first == True:
        os.system("cls")
        print(bcolors.PURPLE+"-------------------------------------------------------------\n\n"+bcolors.CYAN+"                       P O P\n                         Q U I Z"+bcolors.PURPLE+"\n\n-------------------------------------------------------------\n"+bcolors.CYAN+"f = open test\ns = start new test\na,b,c,d = answer question\np = forward\no = backward")
        testtype = msvcrt.getwch().lower()

        #skapar ett nytt test
        if testtype == "s":
            with open("question.json", "r") as getnum:
                l = json.load(getnum)
            testnum = l[0]["testnum"] + 1 
            newtest()
            first = False
        
        #öpnar ett gamalt test
        elif testtype == "f":
            print(bcolors.GREEN+"Input test number")
            testnum = input(":")
            try:
                with open("test"+str(testnum)+".json", "r") as check:
                    testing = json.load(check) 
                os.system("cls")
                print(bcolors.CYAN+"Opening test nr", testing[0]["testnum"] + 1)
                time.sleep(1)
                first = False
            except:
                os.system("cls")
                print(bcolors.RED+"Invalid number")
                time.sleep(2)
                first = True

    #avslutingn efter sista fråga 
    if y == 20: 
        os.system("cls")
        print(bcolors.GREEN+"Hand in test y/n:")
        stop = msvcrt.getwch().lower()
        if stop == "y":
            print(bcolors.CYAN+"quiting test")
            on = False
            break
        elif stop == "n":
            y = y - 1
            continue
        elif stop != "y" or "n":
            print(bcolors.CYAN+"press y to quit or n to look over answers")
            time.sleep(2)
            continue
        time.sleep(1)
        y = y- 1 

    #visar frågor och tar input 
    y,testnum = showquestion(y,testnum)
    do = msvcrt.getwch().lower()

    #går mellan frågor 
    if do not in inputs:
        print(bcolors.RED+"giva a valid input") 
        time.sleep(2)
        continue
    elif do == "p":
        y = forward(y)
    elif do == "o":
        y = backward(y)
    elif do == "h":
        os.system("cls")
        print(bcolors.CYAN+"a,b,c,d = answer question\np = forward\no = backward\nh= help\nq = quit")
        time.sleep(5)
    
    #avslutnig mitt i 
    elif do == "q":
        print(bcolors.GREEN+"quit? y/n:")
        quitnow = msvcrt.getwch().lower()
        if quitnow == "y": 
            break
        elif quitnow == "n":
            continue
        elif quitnow != "y"or "n":
            print(bcolors.RED+"giva a valid input")

    elif do == "a" or "b" or "c" or "d":
        l[y]["q"+str(y+1)+"input"] = do
        with open("test"+str(testnum)+".json", "w") as file:
            json.dump(l,file)

with open("test"+str(testnum)+".json", "r") as ressult:
    r = json.load(ressult)

    for y in range (0,20):
        print(bcolors.CYAN+"Question:",r[y]["question"+str(y+1)],"\ncorrect ans:",r[y]["q"+str(y+1)+"ans"],"\n""Your ans:",r[y]["q"+str(y+1)+"input"],"\n")
        if r[y]["q"+str(y+1)+"ans"] == r[y]["q"+str(y+1)+"input"]:
            point = point + 1 

print(bcolors.GREEN+"You got: ",point,"/20")