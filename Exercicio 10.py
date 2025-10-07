import random
print("\t Guess the number!!!")
guesses=0
Num = random.randint(1,100)
Guess = int(input())
difference = int(Num - Guess)
while difference !=0:
    guesses +=1
    if abs(difference) <=10 : print ("boiling Hot")
    if abs(difference) <=30 and abs(difference) >10 : print ("getting there")
    if abs(difference) <=40 and abs(difference) >30 : print ("bit off but lukewarm")
    if abs(difference) <=60 and abs(difference) >40 : print ("wayyy off")
    if abs(difference) <=100 and abs(difference) >60 : print ("frozen solid")
    print("ammount of guesses :",guesses)
    Guess = int(input())
    difference= int(Num - Guess)
print ("You did it!!!")
print("total guesses: ", guesses)
