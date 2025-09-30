import random
print("=>*ROCK PAPER SCISSORS*<=")
while True:
    print("1:Rock")
    print("2:Paper")
    print("3:Scissors")
    user=input("ENTER THROUGH:").upper()
    print("User Through is:",user)
    sys=["Rock","Paper","Scissors"]
    sc=random.choice(sys).upper()
    print("System Through is:",sc)
    if(user==sc):
        print("GAME DRAW")
    elif(user=='ROCK'):
        if(sc=='PAPER'):
            print("System win")
        else:
            print("User win")
    elif(user=="PAPER"):
        if(sc=="ROCK"):
            print("User win")
        else:
            print("System win")
    elif(user=="SCISSORS"):
        if(sc=="ROCK"):
            print("System win")
        else:
            print("User wim")
    print("1:play again")
    ag=int(input("enter the option:"))
    if(ag!=1):
        break
