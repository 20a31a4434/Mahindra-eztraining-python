#project-1-quiz game
#project-1:-
#Quiz preparations any 5 questions

q1="""Who is actor that played the major role in AVENGERS-ENDGAME?
a.ROBERT DOWNEY JR.
b.CHRIS HEMSWORTH
c.CHRIS EVANS
d.SAMUEL.L.JACKSON"""

q2="""Who is the main character of the anime OVERLORD?
a.MOMONGA
b.ANIZ
c.PANDORA'S ACTOR
d.DEMIURGE"""

q3="""Who killed most gods in the game G.O.W?
a.THOR
b.ZUES
c.KRATOS
d.ARES"""

q4="""What is the king of heroes in the fate series?
a.ARTORIA PENDRAGON
b.ALEXZANDER
c.JEANNE D'ARC
d.GILGAMESH"""

q5="""Who is the best manipulator in the following?
a.AYANOKOJI
b.KIRA
C.EREN
d.A.F.O"""

questions={q1:"a",q2:"a",q3:"c",q4:"d",q5:"a"}

name=input("Hi!What is your name:-")
print("Hello",name,"Welcome to the Quiz")
score=0
for i in questions:
    print()
    print(i)
    flag1=input("Do you want to skip this question(yes/no)")
    if(flag1=="yes"):
        continue
    ans=input("Enter your answer")
    if ans==questions[i]:
        print("Congratulations you got it right")
        print("you have gained 1 point")
        score=score+1
    else:
        print("Sorry you are wrong")
        score=score-1
    flag2=input("Do you want to quit? (Yes/No)")
    if(flag2=="Yes"):
        break
print("Your total score is:",score)
