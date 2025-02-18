import random
print("Welcome to Snake Water Gun Game.\nHere are the rules:\nEnter 1 for Snake.\nEnter 2 for Water.\nEnter 3 for Gun.")
i=userwins=computerwins=0
numberofturns=int(input("How many rounds you want to play:"))
while(numberofturns>i):
    computer=(random.randint(0,1000000000))%3+1
    print(computer)
    user=int(input("Take your turn:"))
    if(user>=1 and user<=3):
        if(user==computer):
            print("Both Gussed Same! Try Again")
        elif((user==1 and computer==2) or (user==2 and computer==3) or (user==3 and computer==1)):
            userwins+=1
            i+=1
        else:
            computerwins+=1
            i+=1
    else:
        print("Please Enter a Valid Number")
if(computerwins>userwins):
    print("The Computer Won !\nBetter Luck Next Time.")
elif(computerwins==userwins):
    print("Its a Draw!\nBetter Luck Next Time.")
else:
    print("Congratulations You Won!")